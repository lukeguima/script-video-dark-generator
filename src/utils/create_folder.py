import os

def create_folder(folder):
    """Create default folder to script running."""    
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Pasta '{folder}' criada com sucesso.")
    else:
        print(f"A pasta '{folder}' já existe.")
