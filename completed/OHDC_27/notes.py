import tkinter as tk

window = tk.Tk()
window.title("GUI Program")
window.minsize(width=500,height=500)

def gen_label(): 
    new_text = entry.get()
    my_label.config(text=new_text)
    my_label.pack()
    
text = {"text":"click me"}
my_label = tk.Label(text="Gui Fuckaround", font=("ariel",24))
my_label.grid(column=0,row=1)
button = tk.Button(text="Click me",command=gen_label)
button.grid(column=2,row=2)
button2 = tk.Button(text="new button")
button2.grid(column=3,row=1)
entry = tk.Entry()
entry.grid(column=4,row=4)

window.mainloop()

