import os
import nbformat

def strip_metadata(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    for cell in notebook['cells']:
        if 'metadata' in cell:
            cell['metadata'] = {}

    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)

if __name__ == '__main__':
    folder_path = './'
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.ipynb'):
            notebook_path = os.path.join(folder_path, file_name)
            strip_metadata(notebook_path)
