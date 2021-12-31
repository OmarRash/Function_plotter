from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from backend import plot_function, clear_plot

#GUI window setup
root = Tk()
root.title("Function Plotter")
root.geometry("950x500")
root.resizable(False, False)
root.iconphoto(False, PhotoImage(file='logo.png'))

#graph setup
figure = Figure(figsize=(5, 5), dpi=100)
subplot = figure.add_subplot(111)
subplot.set(xlabel='X(unit)', ylabel='y (unit)', title='Equation plotter')
subplot.grid()
canvas = FigureCanvasTkAgg(figure)
canvas.get_tk_widget().grid(row=0, rowspan=10, columnspan=5, column=4, ipadx=10)

#minmum value label and input field
Enter_min = Label(root, text="Enter minimum value of (x)")
Enter_min.grid(row=0, column=0, columnspan=3,
               sticky="S" + "W", padx=10, pady=5)
input_min = Text(root, height=2, width=50)
input_min.grid(row=1, column=0, columnspan=3, sticky="N", padx=10, pady=5)

#maximum value label and input field
Enter_max = Label(root, text="Enter maximum value of (x)")
Enter_max.grid(row=2, column=0, columnspan=3,
               sticky="S" + "W", padx=10, pady=5)
input_max = Text(root, height=2, width=50)
input_max.grid(row=3, column=0, columnspan=3, sticky="N", padx=10, pady=5)

#function label and input field
Enter_equ = Label(root, text="Enter function of (x)")
Enter_equ.grid(row=4, column=0, columnspan=3,
               sticky="S" + "W", padx=10, pady=5)
input_equ = Text(root, height=2, width=50)
input_equ.grid(row=5, column=0, columnspan=3, sticky="N", padx=10, pady=5)

#plot function button
button_plot = Button(root, height=1, width=25, text="plot function",
                     command=lambda: plot_function(input_min,input_max,input_equ,subplot, canvas,figure))
button_plot.grid(row=6, column=0, columnspan=3,
                 sticky="N"+"E", padx=10, pady=5)

#clear graph button
button_clear = Button(root, height=1, width=25, text="clear",
                     command=lambda: clear_plot(subplot, canvas))
button_clear.grid(row=6, column=0, columnspan=3,
                 sticky="N"+"w", padx=10, pady=5)
root.mainloop()
