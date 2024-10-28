
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "TrimThatText"

list_of_files = [#It is the list of all files that are required for our project 
    ".github/workflows/.gitkeep", #This is required later on to add the eml or yaml file for cicd pipeline
    f"src/{project_name}/__init__.py",  #Creates a folder names projectname that is our TrimThatText inside the src. _init_.py is a constuctor file that is needed for installation of local package
    f"src/{project_name}/conponents/__init__.py", #components is another folder that is a local package and so inside that we again create a constructor file to that is used later to call it.
    f"src/{project_name}/utils/__init__.py",#keeps utility related code and inside it again we create a constructor file becz utils is a local package
    f"src/{project_name}/utils/common.py", #creates another file common.py in the utils folder
    f"src/{project_name}/logging/__init__.py", #creates a folder logging and inside that a constructor file
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", #creates a file configurtion.py inside config folder. So config folder now has 2 files init and configuration
    f"src/{project_name}/pipeline/__init__.py", #stores our training pipeline
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", 
    "params.yaml", #Here all model related parameters are kept
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb", #Contains the code in the notebooks (ml code basically)

]

#The code below is the logiv for the actual working and flow of the files or how they are to be stored



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)  #split the path into file directory that is the name of folder and the filename

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")
