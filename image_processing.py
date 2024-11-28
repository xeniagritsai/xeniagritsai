import cv2
import numpy as np

def process_image_opencv(file_path):
    # Загрузка изображения
    image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    
    # Проверяем, содержит ли изображение альфа-канал
    if image.shape[2] == 4:  # Альфа-канал присутствует
        # Отделяем альфа-канал
        b, g, r, alpha = cv2.split(image)
        
        # Создаем белый фон
        white_background = np.ones_like(alpha) * 255
        
        # Добавляем белый фон к прозрачным участкам
        alpha_normalized = alpha / 255.0
        b = b * alpha_normalized + white_background * (1 - alpha_normalized)
        g = g * alpha_normalized + white_background * (1 - alpha_normalized)
        r = r * alpha_normalized + white_background * (1 - alpha_normalized)
        
        # Объединяем каналы в итоговое изображение
        image = cv2.merge((b, g, r)).astype(np.uint8)
    
    # Возвращаем обработанное изображение
    return image

# Пример использования
file_path = "your_image.png"  # Путь к вашему файлу
processed_image = process_image_opencv(file_path)
cv2.imshow("Processed Image", processed_image)  # Покажем результат
cv2.imwrite("processed_image.jpg", processed_image)  # Сохраним в новый файл
cv2.waitKey(0)
cv2.destroyAllWindows()
