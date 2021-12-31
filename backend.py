import numpy as np
from tkinter import messagebox

#validate min and max inputs
def valid_input_num(input1,input2):
    try:
        min=float(input1)
        max=float(input2)
        try:
            assert(min<max)==True
        except AssertionError:
            messagebox.showerror("Invalid input","Maximum must be bigger than minimum")
            return False
        return True
    except Exception:
        messagebox.showerror("Invalid input","please enter a valid number")
    return False

#validate input function
def valid_input_equ(input,x):
    try:
        eval(input)
        return True
    except Exception:
        messagebox.showerror("Invalid input function","please enter a valid function")
    return False
#
def plot_function(input_min,input_max,input_equ,subplot,canvas,figure):
    try:
        assert (valid_input_num(input_min.get("1.0", "end-1c"),input_max.get("1.0", "end-1c")))==True
        Min = float(input_min.get("1.0", "end-1c"))
        Max = float(input_max.get("1.0", "end-1c"))
        
        x = np.arange(Min, Max, 0.01)
        result=x
        str_in = str(input_equ.get("1.0", "end-1c")).replace("^", "**")
        if (str_in.isnumeric()):
            result=[float(str_in)]*(x.size)
            subplot.plot(x, result)
        elif valid_input_equ(str_in,x):
            result=eval(str_in)
            subplot.plot(x, result)
        canvas.draw()    

    except AssertionError:
        clear_plot(subplot,canvas)

def clear_plot(plt,canvas):
    plt.cla()
    plt.set(xlabel='X(unit)', ylabel='y (unit)', title='Equation plotter')
    plt.grid()
    canvas.draw() 
    
            


