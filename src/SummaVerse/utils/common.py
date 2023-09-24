import os
from box.exceptions import BoxValueError
import yaml
from SummaVerse.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_yaml_file :Path) -> ConfigBox:
    """Read yaml file and return"""

    try:
        with open(path_yaml_file) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_yaml_file} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """ get size in KB"""

    size_kb = round(os.path.getsize(path)/1024)
    return f'~ {size_kb} KB'
                        
