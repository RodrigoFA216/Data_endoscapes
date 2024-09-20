import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def process_images_in_folder_incremental(folder_path, batch_size=50):
    # Verifica si la carpeta existe
    if not os.path.exists(folder_path):
        print(f"La carpeta {folder_path} no existe.")
        return

    # Histograma acumulado de intensidades de grises
    cumulative_histogram = np.zeros(256)

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

            # Calcular el histograma de la imagen (256 niveles de gris)
            hist, _ = np.histogram(gray_img.flatten(), bins=256, range=(0, 255))

            # Sumar el histograma al acumulado
            cumulative_histogram += hist

        print(f"Procesadas {i + len(batch_files)} imágenes de {len(image_files)}")

    # Normalizar el histograma acumulado (si es necesario)
    cumulative_histogram = cumulative_histogram / cumulative_histogram.sum()

    # Mostrar el histograma acumulado
    plt.figure(figsize=(10, 6))
    plt.bar(range(256), cumulative_histogram, color='red', alpha=0.7)
    plt.title('Histograma Acumulado de Intensidades de Grises')
    plt.xlabel('Intensidad de Gris')
    plt.ylabel('Frecuencia (Normalizada)')
    plt.show()
    return cumulative_histogram

# Define la ruta de la carpeta
folder_path = "GROUND_TH"

# Llama a la función
x = process_images_in_folder_incremental(folder_path)
