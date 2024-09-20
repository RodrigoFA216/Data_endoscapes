# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 00:48:23 2024

@author: jorge
"""

import os
import cv2
import numpy as np

def modify_images_in_folder(folder_path, batch_size=50):
    # Verifica si la carpeta existe
    if not os.path.exists(folder_path):
        print(f"La carpeta {folder_path} no existe.")
        return

    # Lista para almacenar los nombres de las imágenes
    image_files = [f for f in os.listdir(folder_path) if f.endswith(".png")]

    # Procesar imágenes en lotes
    for i in range(0, len(image_files), batch_size):
        batch_files = image_files[i:i + batch_size]

        for filename in batch_files:
            # Ruta completa de la imagen
            img_path = os.path.join(folder_path, filename)
            
            # Cargar la imagen en escala de grises directamente
            gray_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            # Verificar si la imagen fue cargada correctamente
            if gray_img is None:
                print(f"No se pudo cargar la imagen {filename}.")
                continue

            # Aplicar las reglas de modificación:
            # - Valores <= 128 se hacen 0
            # - Valores > 128 se hacen 255
            modified_img = np.where(gray_img <= 128, 0, 255)

            # Guardar la imagen modificada sobrescribiendo la original
            cv2.imwrite(img_path, modified_img)

        print(f"Modificadas {i + len(batch_files)} imágenes de {len(image_files)}")

# Define la ruta de la carpeta
folder_path = "GROUND_TH"

# Llama a la función
modify_images_in_folder(folder_path)
