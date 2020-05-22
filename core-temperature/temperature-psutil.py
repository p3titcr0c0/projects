from os import system
import psutil, time
from tkinter import*

##############################################
#           #                   #            #
#            #                 #             #
############### By petitcroco ################
#            #                 #             #
#           #                   #            #
##############################################


def actu(core1, core2, instant):
	instant.config(text=('At' + str(time.asctime()[10:20])))
	temp1 = int(str(psutil.sensors_temperatures()['coretemp'][0])[32:34])
	temp2 = int(str(psutil.sensors_temperatures()['coretemp'][1])[32:34])
	core1.config(text=(str(temp1)), fg='green')
	core2.config(text=(str(temp2)), fg='green')
	if temp1>=40:
		core1.config(fg='orange')
	if temp2>=40:
		core2.config(fg='orange')
	if temp1>=45:
		core1.config(fg='red')
	if temp2>=45:
		core2.config(fg='red')

window = Tk()
window.geometry("300x200")
window.resizable(0,0)
window.title("Core Temperature")

Label(window, text="Core temperature", font=("Times", "24", "bold italic underline")).grid(row=1, padx=30, pady=(5,20))
instant = Label(window, text='undefined')
instant.grid(row=2)
Label(window, text="temperature core 1 :").grid(row=3, sticky=W, padx=20)
core1 = Label(window, text="undefined")
core1.grid(row=3,  sticky=E, padx=40)
Label(window, text="temperature core 2 :").grid(row=4, sticky=W, padx=20)
core2 = Label(window, text="undefined")
core2.grid(row=4, sticky=E, padx=40)
Button(window, font = ("Helvetica", 10), text ='Actualiser', command = lambda : actu(core1, core2, instant)).grid(row=5, pady=(6, 3))
Button(window, font = ("Helvetica", 10), text ='Quitter', command = lambda : window.destroy()).grid(row=6)
Label(window, text="By petitcroco",font=("Times", 10)).grid(row=6, sticky=E)
actu(core1, core2, instant)

window.mainloop()
