import os 
from pathlib import Path


project_name="mask_detection"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    f"config/config.yaml",
    f"params.yaml",
    f"requirements.txt",
    f"setup.py",
    f"research/trails.ipynb"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    dir_name,dir_file=os.path.split(filepath)
    
    if dir_name!="":
        os.makedirs(dir_name,exist_ok=True)
    
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
    
    
    

    
    