# This line imports or includes the library we will need
from PIL import Image
print("The library is loaded")

image_original = Image.open("earth.jpg")
image_lay = Image.open("spaceshuttle.jpg")
print("New Image: ")

earth_pixels = image_original.load()

shuttle_pixels = image_lay.load()

new_image = Image.new("RGB", image_original.size)
for x in range(0, 799):
    for y in range(0, 599):
        (r, g, b) = earth_pixels[x, y]
        if shuttle_pixels[x, y] == (44, 207, 64):
            shuttle_pixels[x, y] = (r, g, b)
new_image.show()
new_image.save("week_8.jpg")



