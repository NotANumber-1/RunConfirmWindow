import tkinter as tk
import tkinter.ttk as ttk
import os
root = tk.Tk()
root.title("Allow app to run")
root.attributes("-topmost", True)
root.attributes("-toolwindow", True)
root.geometry("400x180")
root.resizable(False, False)
allowed = False
def read():
    global allowed
    try:
        reader = open("pref.data", "r").read()
        if float(reader) == 100:
            allowed = True
            root.destroy()
        else:
            allowed = False
            deslbl.config(text="The app stopped running. ")
            desmni.config(text="Delete pref.data file to change the preference.")
            allowlbl.destroy()
            denylbl.destroy()
            slider.destroy()
            rempref.config(text="Delete pref.data")
            root.update()
            for i in range(0, 250):
                root.after(1)
                root.update()
            if remprefint.get() == 1:
                os.remove("pref.data")
            root.destroy()
    except:
        pass
def genpref():
    if remprefint.get() == 1:
        gen = open("pref.data", "w+")
        gen.write(str(slider.get()))
        gen.close()
def checkifallow(_=any):
    global allowed
    if slider.get() == 100:
        allowed = True
        genpref()
        root.destroy()
    elif slider.get() == 0:
        allowed = False
        genpref()
        root.destroy()
    elif slider.get() < 10:
        denylbl.config(fg="red")
        root.update()
    elif slider.get() > 90:
        allowlbl.config(fg="green")
        root.update()
    else:
        allowlbl.config(fg="black")
        denylbl.config(fg="black")
        root.update()       
deslbl = tk.Label(text="Would you like to allow this app to run?", font=("Arial", 16))
deslbl.pack()
deslbl.place(x=12, y=12)
desmni = tk.Label(text="Push the slider to the right to allow", font=("Arial", 12))
desmni.pack()
desmni.place(x=12, y=48)
slider = ttk.Scale(from_=0, to=100, orient=tk.HORIZONTAL, length=300, command=checkifallow)
slider.pack()
slider.place(x=12, y=80)
slider["value"] = 20
denylbl = tk.Label(text="Deny", font=("Arial", 12))
denylbl.pack()
denylbl.place(x=12, y=108)
allowlbl = tk.Label(text="Allow", font=("Arial", 12))
allowlbl.pack()
allowlbl.place(x=278, y=108)
remprefint = tk.IntVar()
rempref = tk.Checkbutton(text="Remember choices", variable=remprefint)
rempref.pack()
rempref.place(x=12, y=132)
read()
root.mainloop()