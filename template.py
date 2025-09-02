import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'

list_of_files = [
    "agent/__init__.py",
    "agent/agentic_workflow.py",
    "config/__init__.py",
    "config/config.yaml",
    "notebook/experiments.ipynb",
    "prompt_library/__init__.py",
    "prompt_library/prompt.py",
    "tools/__init__.py",
    "utils/__init__.py"
    ".env",
    ".env.name",
    "app.py",
    "requirements.txt",
    "setup.py",
    "templates/index.html",
    "static/css/style.css",
    "static/js/script.js"

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")
        