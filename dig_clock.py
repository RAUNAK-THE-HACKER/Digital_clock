from time import strftime 
from tkinter import Label, Tk

# ======= Configuring window =========
window = Tk()
window.title("digital clock")
window.geometry("800x400")
window.configure(bg="black")  # =======Background of the clock=====
window.resizable(False, False)  # =====setting a fixed window size =======

clock_label = Label(
    window, bg="black", fg="blue", font=("Arial", 40, "bold"), relief="flat"
)
clock_label.place(x=20, y=20)


def update_label():
    """
    This function will update the clock

    every 80 milliseconds
    """
    current_time = strftime("\n\n%H: %M: %S\n\n %d-%m-%Y ")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)
    clock_label.pack(anchor="center")


update_label()
window.mainloop()
