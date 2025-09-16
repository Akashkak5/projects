import pandas as pd
from fastapi import UploadFile
import os

UPLOAD_FOLDER = "uploads/"

def save_upload_file(upload_file: UploadFile) -> str:
    """Save uploaded CSV to uploads folder"""
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    file_path = os.path.join(UPLOAD_FOLDER, upload_file.filename)
    with open(file_path, "wb") as f:
        f.write(upload_file.file.read())
    return file_path

def read_csv(file_path: str) -> pd.DataFrame:
    """Read CSV into pandas DataFrame"""
    return pd.read_csv(file_path)
