import os
from PIL import Image
import numpy as np

#Divide uma imagem em patches e salva cada patch em uma pasta de saída.
def salvar_patches(imagem_path, output_folder, tamanho_patch, classe):

    imagem = Image.open(imagem_path)
    largura, altura = imagem.size

    classe_folder = os.path.join(output_folder, classe)
    os.makedirs(classe_folder, exist_ok=True)

    contador = 0
    for y in range(0, altura, tamanho_patch):
        for x in range(0, largura, tamanho_patch):
            box = (x, y, x + tamanho_patch, y + tamanho_patch)
            patch = imagem.crop(box)
            patch_path = os.path.join(classe_folder,
                                      f"{os.path.basename(imagem_path).split('.')[0]}_patch_{contador}.jpg")
            patch.save(patch_path)
            contador += 1


input_folder = 'OurWelds'
output_folder = 'WeldPatches'
tamanho_patch = 256

for classe in ['Com_Defeito', 'Sem_Defeito']:
    classe_folder = os.path.join(input_folder, classe)
    for imagem_nome in os.listdir(classe_folder):
        imagem_path = os.path.join(classe_folder, imagem_nome)
        salvar_patches(imagem_path, output_folder, tamanho_patch, classe)
