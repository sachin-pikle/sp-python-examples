# Imports
from uuid import UUID, uuid4
from fastapi import FastAPI
from pydantic import BaseModel, Field

# FastAPI app
app = FastAPI()

# Pydantic models
class Todo(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    category: str
    isDone: bool = False

class TodoOutBase(BaseModel):
    msg: str
    error: str = None

class TodoCreateOut(TodoOutBase):
    todo: Todo
    
class TodoGetOut(TodoOutBase):
    todos: list[Todo]

# Local variable for DB
db: list[Todo] = []

# Create a new Todo
@app.post("/todos", response_model=TodoCreateOut)
def create_todo(todo: Todo) -> TodoCreateOut:
    db.append(todo)
    return TodoCreateOut(todo=todo, msg="Todo created.")

# List all Todos
@app.get("/todos", response_model=TodoGetOut)
def fetch_todos() -> TodoGetOut:
    return TodoGetOut(todos=db, msg="Fetched all Todos")

# Get a single Todo by it's unique Id
@app.get("/todo/{id}", response_model=TodoCreateOut | TodoOutBase)
def get_todo_by_id(id: str) -> TodoCreateOut | TodoOutBase:
    try:
        id = UUID(id)
    except Exception as ex:
        return TodoOutBase(msg="Wrong UUID", error=str(ex))

    for todo in db:
        if todo.id == id:
            return TodoCreateOut(todo=todo, msg="Todo fetched")
        
    return TodoOutBase(msg=f"Todo {id} not found")

# Update a todo
@app.put("/todo/{id}", response_model=TodoCreateOut | TodoOutBase)
def update_todo(id: str, todo: Todo) -> TodoCreateOut | TodoOutBase:
    
    try:
        id = UUID(id)
    except Exception as ex:
        return TodoOutBase(msg="Wrong UUID", error=str(ex))
    
    for _todo in db:
        if _todo.id == id:
            _todo.name = todo.name
            _todo.category = todo.category
            return TodoCreateOut(todo=_todo, msg="Todo updated")
        
    return TodoOutBase(msg=f"Todo with UUID {id} not available")

# Delete a todo
@app.delete("/todo/{id}", response_model=TodoOutBase)
def delete_todo(id: str) -> TodoOutBase:

    try:
        id = UUID(id)
    except Exception as ex:
        return TodoOutBase(msg="Wrong UUID", error=str(ex))
    
    for i, _todo in enumerate(db):
        if _todo.id == id:
            del db[i]
            return TodoOutBase(msg=f"Todo {id} deleted")
        
    return TodoOutBase(msg=f"Todo with UUID {id} not available")

# Get todos by category
@app.get("/todo", response_model=TodoGetOut | TodoOutBase)
def get_todos_by_category(category: str) -> TodoGetOut | TodoOutBase:
    todos: list[Todo] = []
    for todo in db:
        if todo.category == category:
            todos.append(todo)
    
    if not todos:
        return TodoOutBase(msg=f"Todos with category {category} not found")
    
    return TodoGetOut(todos=todos, msg="Todos found")
