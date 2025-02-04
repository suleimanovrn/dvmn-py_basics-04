from PIL import Image

image = Image.open("monro.jpg")

red, green, blue = image.split()

width, height = image.size

shift = 10
half_shift = shift // 2

red_left_crop = red.crop((shift, 0, width, height))  # Режем слева
red_both_crop = red.crop((half_shift, 0, width - half_shift, height))  # Режем по бокам
red_blend = Image.blend(red_left_crop, red_both_crop, alpha=0.5)  # Смешиваем

blue_right_crop = blue.crop((0, 0, width - shift, height))  # Режем справа
blue_both_crop = blue.crop((half_shift, 0, width - half_shift, height))  # Режем по бокам
blue_blend = Image.blend(blue_right_crop, blue_both_crop, alpha=0.5)  # Смешиваем

green_cropped = green.crop((half_shift, 0, width - half_shift, height))  # Режем по бокам

shifted_image = Image.merge("RGB", (red_blend, green_cropped, blue_blend))

shifted_image.save("final_image.jpg")

shifted_image.thumbnail((80, 80))

shifted_image.save("avatar.jpg")
