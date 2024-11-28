import cv2

# Функция изменения размера изображения
def resize_image(image_path, width, height):
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, (width, height))
    return resized_image

# Функция конвертации в черно-белое
def convert_to_grayscale(image_path):
    image = cv2.imread(image_path)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

# Функция применения фильтра Гаусса
def apply_gaussian_blur(image_path, kernel_size=(5, 5)):
    image = cv2.imread(image_path)
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    return blurred_image

# Использование
file_path = "your_image.jpg"  # Путь к изображению

# Изменение размера
resized = resize_image(file_path, 800, 800)
cv2.imshow("Resized Image", resized)
cv2.imwrite("resized_image.jpg", resized)

# Конвертация в черно-белое
grayscale = convert_to_grayscale(file_path)
cv2.imshow("Grayscale Image", grayscale)
cv2.imwrite("grayscale_image.jpg", grayscale)

# Применение фильтра Гаусса
blurred = apply_gaussian_blur(file_path)
cv2.imshow("Blurred Image", blurred)
cv2.imwrite("blurred_image.jpg", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()
