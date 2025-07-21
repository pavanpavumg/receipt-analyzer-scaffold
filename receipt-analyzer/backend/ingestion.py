import os
from pathlib import Path

ALLOWED_EXTENSIONS = ['.jpg', '.png', '.pdf', '.txt']

def save_file(file, upload_dir='data/uploads/'):
    Path(upload_dir).mkdir(parents=True, exist_ok=True)
    filepath = os.path.join(upload_dir, file.name)
    with open(filepath, 'wb') as f:
        f.write(file.getbuffer())
    return filepath

def validate_file(filename):
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS
