from PIL import Image

image = Image.open("monro.jpg")

red, green, blue = image.split()

width, height = image.size

shift = 10

red_shifted = Image.new("L", (width, height))
blue_shifted = Image.new("L", (width, height))

red_shifted.paste(red.crop((0, 0, width - shift, height)), (shift, 0))
red_shifted.paste(red.crop((width - shift, 0, width, height)), (0, 0))

blue_shifted.paste(blue.crop((shift, 0, width, height)), (0, 0))
blue_shifted.paste(blue.crop((0, 0, shift, height)), (width - shift, 0))

green_cropped = green.crop((shift, 0, width - shift, height))

final_width = width - shift * 2
red_final = red_shifted.crop((shift, 0, shift + final_width, height))
blue_final = blue_shifted.crop((shift, 0, shift + final_width, height))

shifted_image = Image.merge("RGB", (red_final, green_cropped, blue_final))

shifted_image.save("red_blue_shifted_fixed.jpg")

shifted_image.thumbnail((80, 80))

shifted_image.save("avatar.jpg")

