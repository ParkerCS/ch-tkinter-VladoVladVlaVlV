# Universal Gravity Calculator (30pts)
# In physics, the force of gravity between two objects
# can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a tkinter app with the following attributes:
# - use an App class
# - Add a title.
# - Make a label and entry widget for m1, m2, and r
# - Make a "Calculate" button widget to trigger a lambda function
# - Add a calculate label widget to display the answer
# - Make exceptions for division by zero and type conversion errors.
# - When "Calculate" is pushed, the result is displayed.  Yay!
# - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception)
# - Make your app unique by changing 3 or more DIFFERENT style attributes or kwargs for your app.  Perhaps consider: fonts, color, padding, widths, etc).  Put a comment in your code to tell me what you changed. If you change the font for all the widgets, that is ONE thing.  If you add padx to all your app widgets, that is ONE thing.  If you change the color of all your blocks, that is ONE thing.
from tkinter import *
from tkinter import font


# noinspection PyBroadException
class App():



    def __init__(self,master):
        self.m1 = DoubleVar()
        self.m2 = DoubleVar()
        self.grav = DoubleVar()
        self.r= DoubleVar()
        self.title_font=font.Font(family="Comic Sans MS", size=60)

        self.m2_label = Label(master, text="Mass 2:", font=self.title_font,fg="Black",bg="Gold")
        self.m2_label.grid(row=3, column=1, sticky="e"+'w')

        self.m2_entry = Entry(master, textvariable=self.m2, font=self.title_font, width=10, justify=CENTER,fg="White",bg="Black")
        self.m2_entry.grid(row=3, column=2, sticky="w"+"e")

        self.m1_label = Label(master, text="Mass 1:", font=self.title_font,fg="Black",bg="Gold")
        self.m1_label.grid(row=2, column=1, sticky="e"+"w")

        self.m1_entry = Entry(master, textvariable=self.m1, font=self.title_font, width=10, justify=CENTER,fg="White",bg="Black")
        self.m1_entry.grid(row=2, column=2, sticky="w"+"e")

        self.r_label = Label(master, text="Radius:", font=self.title_font,fg="Black",bg="Gold")
        self.r_label.grid(row=4, column=1, sticky="e"+"w")

        self.r_entry = Entry(master, textvariable=self.r, font=self.title_font, width=10, justify=CENTER,fg="White",bg="Black")
        self.r_entry.grid(row=4, column=2, sticky="w"+"e")

        self.grav_button = Label(master, text="Calculate : ",font=self.title_font,pady=2,borderwidth=5,relief="raised",height=1,fg="White",bg="Black")
        self.grav_button.grid(row=5, column=1, sticky="e"+"w")

        self.grav_button.bind("<Button-1>",self.concat)

        self.grav_label = Label(master, textvariable=self.grav, font=self.title_font, width=10, borderwidth=5,relief="raised",fg="Black",bg="Gold",justify=CENTER)
        self.grav_label.grid(row=5, column=2, sticky="w"+"e")

    def concat(self,event):
        try:
            self.grav.set("{:.2e}".format(self.m1.get() * self.m2.get() / (self.r.get() * self.r.get()) * 0.0000000000667))
        except ZeroDivisionError:
            self.grav.set("Not divisible by 0")
        except:
            self.grav.set("Type Error")


if __name__ == "__main__":
    root = Tk()
    root.title("Universal Gravity Calculator - UGC")
    my_app = App(root)
    root.mainloop()

