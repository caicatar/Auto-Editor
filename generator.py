from PIL import Image, ImageFont, ImageDraw
import random

# surname_arr = ["Santos", "Quinto", "Rosales"]
# givenname_arr = ["Alfred", "Roberto", "Russell"]
# middlename_arr = ["Magantos", "Disquitado", "Consultado"]

gen_amount = input("How many IDs you want to generate?:")
amount = int(gen_amount)
for i in range(amount):
    id_template = Image.open("updated_umid.jpg")
    index_crn = [0,1,2,9,7]
    index_sur = [1,4,5,7,9,14,15,18]
    rand = random.sample(index_crn, len(index_crn))
    rand2 = random.sample(index_sur, len(index_sur))
    var1, var2, var3, var4, var5 = [rand[i] for i in (0,1,2,3,4)]
    surs1, surs2, surs3, surs4, surs5 = [rand2[i] for i in (0,1,2,4,5)]

# CRN
    png1 = Image.open(str(var1) + ".png")
    png2 = Image.open(str(var2) + ".png")
    png3 = Image.open(str(var3) + ".png")
    png4 = Image.open(str(var4) + ".png")
    png5 = Image.open(str(var5) + ".png")

#Names
    sur1 = Image.open(str(var1) + ".png")
    sur2 = Image.open(str(var1) + ".png")
    sur3 = Image.open(str(var1) + ".png")
    sur4 = Image.open(str(var1) + ".png")
    sur5 = Image.open(str(var1) + ".png")

#Paste
#crn
    id_template.paste(png1, (3280, 954), mask=png1)
    id_template.paste(png2, (3360, 954), mask=png2)
    id_template.paste(png3, (3430, 954), mask=png3)
    id_template.paste(png4, (3510, 954), mask=png4)
    id_template.paste(png5, (3580, 954), mask=png5)



#surname
    id_template.paste(surs1, (3280, 954), mask=surs1)
    id_template.paste(surs1, (3280, 954), mask=surs1)
    id_template.paste(surs1, (3280, 954), mask=surs1)
    id_template.paste(surs1, (3280, 954), mask=surs1)    
    id_template.save('generated/' + str(var1) + str(var2) + str(var3) + str(var4) + str(var5) + 'result_image.jpg')
    print('Successfully Generated!')



