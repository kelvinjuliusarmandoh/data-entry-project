from tkinter import *
window = Tk()
#Radiobutton
def radio_used():
    print("X")
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radio_stat_val = radio_state
print(radio_state)
print(radio_stat_val.get())
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

window.mainloop()