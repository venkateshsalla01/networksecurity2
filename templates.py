import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')


list_of_files = [
    "networksecurity/cloud/__init__.py",
    "networksecurity/components/__init__.py",
    "networksecurity/constants/__init__.py",
    "networksecurity/entity/__init__.py",
    "networksecurity/exception/__init__.py",
    "networksecurity/logging/__init__.py",
    "networksecurity/pipeline/__init__.py",
    "networksecurity/utils/__init__.py",
    
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/table.html",
    "test_mongodb.py",
    "app.py"
    "push_data.py",
    ".gitignore"
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