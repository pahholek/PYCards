class ticketfill():

    def getcode(filename, lenght):
        import string
        import os
        import random
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for i in range(lenght))
        if os.path.isfile(filename):
            pass
        else:
            b = open(filename, 'w')
            b.close()

        a = open(filename, 'r')
        for i in range(len(open(filename).readline()) - 1):
            while a.readlines(i) == code:
                code = ''.join(random.choice(characters) for i in range(lenght))
                print(code)

        return code

    def run(code, date, i_num):
        import math
        import qrcode
        import os.path
        from PIL import Image, ImageDraw, ImageFont
        import pathlib
        import PIL
        import shutil
        from os import path

        codes = open("codeDB.txt", 'a')
        codes.write(code)
        codes.write("\n")
        codes.close()
        img = qrcode.make(code, border=0, box_size=7)
        img.save('tempcode.png')
        codeimg = Image.open('tempcode.png')
        teplateimg = Image.open('ticketsaple.png')
        sample_size = teplateimg.size
        merged = Image.new('RGB', (sample_size[0], sample_size[1]))
        merged.paste(teplateimg, (0, 0))
        merged.paste(codeimg, (15, 25))
        merged.save("cardtemp.png")
        img2 = Image.open('cardtemp.png')
        editimg = ImageDraw.Draw(img2)
        font = ImageFont.truetype('ShareTechMono-Regular.ttf', 17)
        editimg.text((280, 90), code, font=font, fill=(0))
        editimg.text((280, 150), date, font=font, fill=(0))
        """if os.path.isfile("card.pdf") == True:
            img2.save("card.pdf", append=True)
        else:
            img2.save("card.pdf")"""

        print((math.ceil(i_num + 1 / 6)))
        if os.path.exists(str('data/' + str(i_num + 1))):
            pass
        else:
            print(str('data/' + str(int(math.ceil((i_num + 1) / 6)))))
            try:
                os.mkdir(str('data/' + str(int(math.ceil((i_num + 1) / 6)))))
            except FileExistsError:
                print("Plik istnieje niczego nie utworzono")
        img2.save(str('data/' + str(int(math.ceil((i_num + 1) / 6))) + '/' + code + '.png'))
