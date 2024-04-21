import tkinter as tk

window = tk.Tk()
window.title("Miles to KM converter")
window.config(padx=20,pady=20)

def calc_conversion(mile:float, km:float=1.60934):
    return mile * km

def change_label():
    new_entry = m_entry.get()
    try:
        mile = float(new_entry)
        result = calc_conversion(mile=mile)
        result_label.config(text=result)
    except Exception as e:
        print(e)

m_entry = tk.Entry(width=10) 
m_entry.grid(column=1,row=0)
m_label = tk.Label(text="miles")
m_label.grid(column=2,row=0)
is_equal = tk.Label(text="Is equal to")
is_equal.grid(column=0,row=1)
result_label = tk.Label(text=0)
result_label.grid(column=1,row=1)
result_km = tk.Label(text="km")
result_km.grid(column=2,row=1)
calc_button = tk.Button(text="calculate", command=change_label)
calc_button.grid(column=1,row=2)

window.mainloop()