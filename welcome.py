from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
#import openfilenew
main_screen = Tk()  # create a GUI window
fontStyle = tkFont.Font(family="Lucida Grande", size=50)

labelExample = tk.Label(main_screen, text="225", font=fontStyle)
def decrease_label_font():
    fontsize = fontStyle['size']
    labelExample['text'] = fontsize-2
    fontStyle.configure(size=fontsize-2)

def main_account_screen():
    global main_screen
    main_screen.geometry("250x100")  # set the configuration of GUI window
    main_screen.title("Account Login")  # set the title of GUI window

 

# create a Form label
l1=Label(main_screen,text="VIRTUAL TRIAL ROOM AND SIZE PREDICTION OF CLOTHES ", bg="sky blue", width="75", height="10",command=decrease_label_font())
l1.grid(row = 0, column = 0, sticky = W, pady = 2) 

#Label(text="").pack()
def run():
	print("hello from run!!!")
	import openfilenew
	openfilenew.get_folder()
	
	

# create select Button
b1=Button(main_screen,text="Select tshirt", height="2", width="30",command=lambda: run())
b1.grid(row = 1, column = 0, sticky = W, pady = 2)
#Label(text="").pack()
main_screen.resizable(True,True)
main_screen.mainloop()  # start the GUI

main_account_screen()


 # call the main_account_screen() function