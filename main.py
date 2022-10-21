from tkinter import *

my_window = Tk()
my_window.title("Miles to Km Converter")
my_window.minsize(width=500, height=300)
#padding the my_window:
my_window.config(padx=20, pady=20)

def convert():
    print("hi")

def button_clicked():
    pass



#Label: "is equal to"
my_label = Label(text="is equal to", font=("Arial", 16, ""))
my_label.grid(column=0, row=1)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)
input.config(width=7)

#Label: gets output from a function:
converted_value = Label(text="", font=("Arial", 16, ""))
converted_value.grid(column=1, row=1)
converted_value.config(text="0")

#Label: "Miles"
my_label = Label(text="Miles", font=("Arial", 16, ""))
my_label.grid(column=2, row=0)

#Button: "Calculate"
my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(column=1, row=2)

#Label: "Km"
my_calculate_label = Label(text="Km", font=("Arial", 16, ""))
my_calculate_label.grid(column=2, row=1)






















my_window.mainloop()