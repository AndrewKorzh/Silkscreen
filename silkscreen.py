import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.image import imsave
from PIL import Image

def get_top_colors(image_path, clustered_img_path, num_colors=10):

    image = plt.imread(image_path)

    pixels = np.reshape(image, (-1, 3))

    # Нужно получить основные цвета - используем для этого кластеризацию методом К средних
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    # Основной цвет - как центроид кластера
    colors = kmeans.cluster_centers_
    pixel_labels = kmeans.predict(pixels)
    clustered_pixels = np.array([colors[label] for label in pixel_labels])
    clustered_image = np.reshape(clustered_pixels, image.shape)
    # Восстановление исходного диапазона значений пикселей
    clustered_image = np.clip(clustered_image, 0, 255).astype(np.uint8)


    #Сохраняем и выводим изображение
    image = Image.fromarray(clustered_image)
    image.save(clustered_img_path)
    saved_image = Image.open(clustered_img_path)
    saved_image.show()


    return clustered_image, colors



def save_color_layers(image_path, output_folder, clustered_img_path, num_colors = 10):
    # Папка для слоёв
    os.makedirs(output_folder, exist_ok=True)
    # Получение кластеризованного изображения и цветов
    clustered_image, colors = get_top_colors(image_path, clustered_img_path = clustered_img_path, num_colors = num_colors)

    # Проход по каждому уникальному цвету
    for i, color in enumerate(colors):
        color_name = '_'.join(str(int(c)) for c in color)
        # Создание маски для пикселей, соответствующих текущему цвету
        mask = np.all(np.isclose(clustered_image, color, atol=10), axis=-1)

        # Создание слоя с белым фоном и черными объектами
        layer = np.ones_like(clustered_image) * 255
        layer[mask] = 0

        # Сохранение слоя в папку
        layer_path = os.path.join(output_folder, f'layer_{color_name}.png')
        imsave(layer_path, layer, cmap='gray')




# Пример использования
image_path = 'C:\\Users\\korzh\\Downloads\\GP5SoQzRa4A.jpg'
output_folder = 'color_layers'
clustered_img_path = "clustered_im.jpg"
num_colors = 10
save_color_layers(image_path, output_folder, clustered_img_path, num_colors)





#
