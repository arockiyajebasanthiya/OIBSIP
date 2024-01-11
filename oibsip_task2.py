                 #BMI Calculator

#import needed modules
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime

bmi_data=[]
def BMI_Calculator():
    try:
        height=float(entry1.get())
        weight=int(entry2.get())
        bmi=weight/float(height*height)
        result_text = f"Your BMI is {bmi:.2f} - {get_bmi_category(bmi)}"
        result_label.config(text=result_text)
        # Save BMI data for analysis
        bmi_data.append({"Date": datetime.date.today(), "BMI": bmi})

    except ValueError:
        messagebox.showinfo("Alert","Please enter Valid Height and Weight")

def get_bmi_category(bmi):
    if bmi < 18.5:
       return "Underweight!Amplify your strength!"
    elif bmi>=18.5 and bmi<25:
        return "Normal!Balance Achieved!"
    elif bmi >= 25 and bmi< 30:
        return "Overweight!Shed Weight,Ignite Vitality"
    elif bmi >= 30:
        return "Obesity!Bid Farewell to Excess weight"

def clear_data():
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)
    
def save_data():
    messagebox.showinfo("Saved", "Data saved successfully.")

def plot_bmi_trends():
    if not bmi_data:
        messagebox.showwarning("No Data", "No BMI data available for plotting.")
        return

    dates = [entry["Date"] for entry in bmi_data]
    bmis = [entry["BMI"] for entry in bmi_data]
    fig, ax = plt.subplots()
    ax.plot(dates, bmis, marker='*', linestyle='--', color='b')
    ax.set_xlabel('Date')
    ax.set_ylabel('BMI')
    ax.set_title('BMI Trends')
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    plt.show()

root=tk.Tk()
root.title("BMI CALCULATOR")

entry1_label=tk.Label(root,text="Enter your Height(in Meter):")
entry1_label.pack(pady=10)
entry1=tk.Entry(root)
entry1.pack(pady=5)

entry2_label=tk.Label(root,text="Enter your Weight(in Kg):")
entry2_label.pack(pady=10)
entry2=tk.Entry(root)
entry2.pack(pady=5)

calc_button=tk.Button(root,text="Evaluate BMI",command=BMI_Calculator)
calc_button.pack(pady=10)

result_label=tk.Label(root,text="")
result_label.pack(pady=10)

clear_button=tk.Button(root,text="Clear Data",command=clear_data)
clear_button.pack(pady=5)

save_button = tk.Button(root, text="Save Data", command=save_data)
save_button.pack(pady=10)

plot_button = tk.Button(root, text="View BMI Trends", command=plot_bmi_trends)
plot_button.pack(pady=10)
#Start the main loop
root.mainloop()


