## https://github.com/fastapi/fastapi?tab=readme-ov-file#requirements
## pip install "fastapi[standard]"
## Run the server in dev mode:
## fastapi dev main.py
## for production use:
## fastapi run
## 
## Yash Jain's Fast API playlist
## 

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict

app = FastAPI(
    title="FastAPI Example Swagger Docs",
    description="This is my FastAPI Swagger Documentation",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Hi from Fast API!"}

@app.get("/hello")
def hello():
    return {"message": "Hello!"}

@app.post("/books")
def create_book(book: dict):
    return {"data": book, "msg": "Book Created"}

@app.put("/books/{book_id}")
def update_book(book_id: str, book: dict):
    return {"book_id": book_id, "book": book, "msg": f"Book {book_id} updated"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    return {"msg": f"Book {book_id} deleted"}

@app.get("/books")
def get_book_by_title(title: str):
    book = {
        "title": "Python for AI (6th Edition)",
        "author": "Random Person"
    }
    return {"book": book, "msg": "Book lookup successful"}


class Book(BaseModel):
    title: str
    author: str

    model_config = ConfigDict(extra="forbid")

class BookOut(BaseModel):
    book: Book
    msg: str

@app.post("/book/create", response_model=list[BookOut])
def create_a_book(book: Book) -> list[BookOut]:
    return [{
        "book": book, 
        "msg": "Book Created"
        }]
    
@app.post(
        "/book/new/create", 
        response_model=BookOut, 
        summary="Create a new book.",
        description="This is a post API to create a new book."
        )
def create_a_new_book(book: Book) -> BookOut:
    return BookOut(book=book, msg="Book created")
    