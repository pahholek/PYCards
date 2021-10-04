def errMSG(ErrTitle, ErrText, winsize):
    import tkinter as tk
    errTK = tk.Tk()
    errTK.title(ErrTitle)
    errTK.geometry(winsize)
    
    errLabel = tk.Label(master = errTK, text = 'ERROR!!!')
    errLabel.config(font=("Courier", 21, 'bold'))
    errLabel.pack(side='top')

    errTXTLabel = tk.Label(master = errTK, text = ErrText)
    errTXTLabel.config(font=("Courier", 15))
    errTXTLabel.pack( side = 'top')

    quitButton = tk.Button(master = errTK, text = '   Ok   ', command =lambda: errTK.destroy())
    quitButton.pack( side = 'bottom')


    errTK.mainloop()
