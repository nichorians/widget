from pathlib import Path
import os

root = '/data12t/ucf101/frames'
root_path = Path(root)

for filepath in root_path.rglob('*.jpg'):
    filename = filepath.name
    parts = filename.split('pic')
    if len(parts) > 1:
        new_name = 'image_0'+parts[1]
        new_name = filepath.with_name(new_name)
        filepath.rename(new_name)
