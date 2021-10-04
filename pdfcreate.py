class pdfC:
    @staticmethod
    def run():
        import os
        from PIL import Image
        a = os.listdir('data')
        import shutil
        shutil.rmtree('imgdata')
        os.mkdir('imgdata')
        for b in range(len(a)):
            last = False
            directory = 'data/' + str(b + 1) + '/'
            SampleImg = Image.open('ticketsaple.png')
            SampleImgSize = SampleImg.size
            imgOut = Image.new('RGB', (int(SampleImgSize[0] * 2), int(SampleImgSize[1] * 3)))

            dirList = os.listdir(directory)

            def imgPaste(ImgDir, pos1, pos2):
                import os
                from PIL import Image

                if os.path.isfile("imgdata/temp" + str(b) + '.png'):
                    imgOutput = Image.open("imgdata/temp" + str(b) + '.png')
                else:
                    imgOutput = Image.new('RGB', (int(SampleImgSize[0] * 2), int(SampleImgSize[1] * 3)))
                imgOpen = Image.open(str(ImgDir))
                imgOutput.paste(imgOpen, (pos1, pos2))
                imgOutput.save("imgdata/temp" + str(b) + '.png')


            for i in range(len(dirList)):
                if i == 0:
                    tempimg = Image.new('RGB', (int(SampleImgSize[0] * 2), int(SampleImgSize[1] * 3)))
                    tempimg2 = Image.open('white_source.png')
                    tempimg.paste(tempimg2, (0, 0))
                    tempimg.save("imgdata/temp" + str(b) + '.png')

                    imgPaste(directory + str(dirList[i]), 0, 0)

                if i == 1:
                    imgPaste(directory + str(dirList[i]), 420, 0)
                if i == 2:
                    imgPaste(directory + str(dirList[i]), 0, 198)
                if i == 3:
                    imgPaste(directory + str(dirList[i]), 420, 198)
                if i == 4:
                    imgPaste(directory + str(dirList[i]), 0, 396)
                if i == 5:
                    imgPaste(directory + str(dirList[i]), 420, 396)

        
        imglist = []
        dirlistPdf = os.listdir('imgdata')
        first = 0  
        for i in range(len(dirlistPdf)):
            if first == 0:
                first = Image.open('imgdata/' + str(dirlistPdf[i]))
            else:
                imglist.append(Image.open('imgdata/' + str(dirlistPdf[i])))
        first.save('codesToPrint.pdf', save_all=True, append_images=imglist)
        os.system('codesToPrint.pdf')