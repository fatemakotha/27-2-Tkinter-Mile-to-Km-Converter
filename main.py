from tkinter import *

my_window = Tk()
my_window.title("Miles to Km Converter")
my_window.minsize(width=250, height=150)
#padding the my_window:
my_window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_input.get()) #gets hold of whatever is inserted by the user
    km = miles * 1.609
    km_result_label.config(text=km)

def button_clicked():
    miles_to_km()



#Label: "is equal to"
my_label = Label(text="is equal to", font=("Arial", 12, ""))
my_label.grid(column=0, row=1)

#Entry
miles_input = Entry(width=10)
print(miles_input.get())
miles_input.grid(column=1, row=0)
miles_input.config(width=7)

#Label: gets output from a function:
km_result_label = Label(text="0", font=("Arial", 12, ""))
km_result_label.grid(column=1, row=1)


#Label: "Miles"
my_label = Label(text="Miles", font=("Arial", 12, ""))
my_label.grid(column=2, row=0)

#Button: "Calculate"
my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(column=1, row=2)
#when button is clicked the function below is activated
# def button_clicked():
#     miles_to_km()

#Label: "Km"
my_calculate_label = Label(text="Km", font=("Arial", 12, ""))
my_calculate_label.grid(column=2, row=1)

#WHEN 20 miles is the INPUT the OUTPUT is 32.18 km **

my_window.mainloop()