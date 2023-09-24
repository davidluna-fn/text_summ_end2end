import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'SummaVerse'

list_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/common.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yalm',
    'params.yalm',
    'app.py',
    'main.py',
    'DockerFile',
    'requirements.txt',
    'setup.py',
    'research/trial.ipynb'
]

for filepath in list_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for file: {filename}')

    if (not os.path.exists(filedir)) or (not os.path.getsize(filedir) == 0):
        with open(filepath, 'w') as f:
            logging.info(f'Created empty file: {filepath}')

    else:
        logging.info(f'{filename} is already exists')
            