# Python Examples 

## Notes

1. This repository uses examples from a number of sources including,

    - Python Crash Course, 3rd Edition by Eric Matthes (https://ehmatthes.github.io/pcc_3e/)
    - Automate the Boring Stuff, 3rd Edition by Al Sweigart
    - Hugging Face Tranformers https://github.com/huggingface/transformers
    - https://code.visualstudio.com/docs/python/python-tutorial
    - Pandas https://pypi.org/project/pandas/
    - OpenPyXL https://pypi.org/project/openpyxl/
    - Requests https://pypi.org/project/requests/

2. Use pyenv to manage Python installations
    
    - Reference: pyenv without brew  https://github.com/pyenv/pyenv-installer?tab=readme-ov-file#install 

3. Install Python

    - List available python:
    
    ```
    pyenv install -l | grep 3.1
    ```
    
    - Installed 3.14.2 (on 3-Feb=2026)
    
    ```
    pyenv install 3.14.2
    ```

4. Virtual environments 

    - Reference: Fast API - Virtual Environments https://fastapi.tiangolo.com/virtual-environments/
    - One directory per project
    - Create a virtual environment in each project directory
    
    ```
    python -m venv .venv
    ```

    - Alternative: Follow the steps in https://code.visualstudio.com/docs/python/python-tutorial

5. VS Code Extensions

    - Python by Microsoft
    - Black Formatter by Microsoft
    - isort by Microsoft
    - Flake8 by Microsoft
    - REST Client https://marketplace.visualstudio.com/items?itemName=humao.rest-client

4. Install Hugging Face Transformers in the workspace venv

    ```
    pip install "transformers[torch]"
    ```

5. Install Pandas in the workspace venv

    ```
    pip install pandas
    ```

6. Install OpenPyXl in the workspace venv

    ```
    pip install openpyxl
    ```

7. Install Requests in the workspace venv

    ```
    pip install requests
    ```
