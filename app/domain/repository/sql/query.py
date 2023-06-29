import os

def get(filepath: str) -> str:
    """
        filepath: sql filepath from 'sql' directory
    """
    with open(os.path.join(os.path.dirname(__file__), filepath), "r") as f:
        return f.read()