import cv2
image_name = "img.png"
img = cv2.imread(image_name)
width = 700
height = 3000
k = 0
for r in range(0, img.shape[0], height):
  for c in range(0, img.shape[1], width):
    cv2.imwrite(f"img_{k}.png", img[r:r+height, c:c+width, :])
    k += 1
print(f"Успішно порізав зображення {image_name} на {k} шматочків")
