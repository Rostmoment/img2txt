from PIL import Image
file = input("Enter file name: ")
image = Image.open(file).convert("L")

chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

width, height = image.size

with open(file + ".txt", "w") as f:

  for y in range(height):
    for x in range(width):
      pixel_value = image.getpixel((x, y))
      char_index = int((pixel_value / 255) * (len(chars) - 1))
      f.write(chars[char_index])
    f.write("\n")
