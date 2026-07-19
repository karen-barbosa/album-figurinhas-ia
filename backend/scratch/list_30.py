import os

path = r"c:\Users\Karen Barbosa\Downloads\backend\figurinhas"
files = os.listdir(path)
for f in files:
    if f.startswith("30"):
        print(f"Name: {repr(f)}, Length: {len(f)}")
