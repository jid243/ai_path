# renamer.py
import os

def safe_rename_folder(folder="."):
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    
    for i, f in enumerate(files, start=1):
        name, ext = os.path.splitext(f)
        new_name = f"file_{i}{ext}"
        print(f"Renaming: {f} -> {new_name}")
        os.rename(os.path.join(folder, f), os.path.join(folder, new_name))

if __name__ == "__main__":
    folder = input("Folder (press Enter for current folder): ").strip() or "."
    safe_rename_folder(folder)

