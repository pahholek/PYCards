import tkinter as tk

import errorHandler
from cardsInset import ticketfill
import os.path
from os import path
import shutil
from pdfcreate import pdfC
from errorHandler import errMSG
import subprocess

#checks numbers in rootCodesInput
def CheckNumb(number):
    try:
        int(number)
        CodeGet(number)
        return True
    except:
        print('')
        #ErrorHandler
        print("pass")
        errorHandler.errMSG('This is not a Number', 'Number incorect / \n you didnt specified the number', "500x150")
        return False

def openPDF(toOpen):
    try:
        subprocess.run([toOpen], check = True)
    except:
        errorHandler.errMSG('There is no file', 'File was not created or \n you deleted the file', "500x150")
        
#generate the codes
def CodeGet(noCodes):
    if os.path.exists("data") == True:
        shutil.rmtree('data')
        os.mkdir('data')
    else:
        os.mkdir('data')

    for i in range(int(noCodes)):
        ticketfill.run(ticketfill.getcode("codeDB.txt", 8), "01-10-2021", i)
        print(i + 1, " of ", noCodes)
    pdfC.run()



root = tk.Tk()
root.geometry("700x140")
root.configure(background="white")
def genVisuals():
    MainLabel = tk.Label(master = root, text = "Wpisz ilość kodów:")
    MainLabel.config(font=("Courier", 15, 'bold'))
    MainLabel.pack( side = 'top')

    rootCodesInput = tk.Entry()
    rootCodesInput.config(justify = 'center')
    rootCodesInput.config(font=("Courier", 15, 'bold'))
    rootCodesInput.pack( side = 'top' )

    rootSpacing = tk.Label(master = root)
    rootSpacing.pack(side = 'top')
    
    
    rootOpenPDF = tk.Button(master = root, text = "Otwórz pdf", command =lambda: openPDF('codesToPrint.pdf'))
    rootOpenPDF.place(x = 600, y = 100)
    
    rootOpenDB = tk.Button(master = root, text = "Otwórz Bazę danych", command =lambda: openPDF('codeDB.txt'))
    rootOpenDB.place(x = 470, y = 100)
    
    rootCodesButton = tk.Button(root, text = "Generuj Kody", command =lambda: CheckNumb(rootCodesInput.get()))
    rootCodesButton.config(font=("Courier", 15, 'bold'))
    rootCodesButton.pack( side = 'top')


genVisuals()
root.mainloop()
