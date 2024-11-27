from PIL import Image
import os

#Remove imagens corrompidas
def check_images_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                img = Image.open(file_path)
                img.verify()
            except (IOError, SyntaxError):
                print(f"Corrupted file found and removed: {file_path}")
                os.remove(file_path)

check_images_in_directory('directory')
