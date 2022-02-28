from PIL import Image, ImageFont, ImageDraw
import random

# surname_arr = ["Santos", "Quinto", "Rosales"]
# givenname_arr = ["Alfred", "Roberto", "Russell"]
# middlename_arr = ["Magantos", "Disquitado", "Consultado"]

#Test
    # id_template.paste(png_1, (3360, 954), mask=png_1)
    # id_template.paste(png_2, (3430, 954), mask=png_2)
    # id_template.paste(png_9, (3510, 960), mask=png_9)
    # id_template.paste(png_7, (3580, 958), mask=png_7)
id_template = Image.open("umid_real.jpg")
index = [0,1,2,9,7,6]
rand = random.sample(index, len(index))
var1, var2, var3, var4, var5 = [rand[i] for i in (0,1,2,3,4)]

png1 = Image.opyen("1.png")
png2 = Image.open("0.png")
png3 = Image.open("9.png")
png4 = Image.open("6.png")
png5 = Image.open("2.png")

id_template.paste(png1, (3280, 960), mask=png1)
id_template.paste(png2, (3360, 960), mask=png2)
id_template.paste(png3, (3430, 960), mask=png3)
id_template.paste(png4, (3510, 960), mask=png4)
id_template.paste(png5, (3580, 960), mask=png5)

# id_template.save(str(var1) + str(var2) + str(var3) + str(var4) + str(var5) + 'result_image.jpg')
id_template.save('result_image.jpg')

