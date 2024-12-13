import os

def clean_temp_files(folder):
    """Clean up files temporary when script completes."""    
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f"Não foi possível deletar {file_path}. Erro: {e}")
