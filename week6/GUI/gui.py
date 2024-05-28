import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import math


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of a circle")
    frm_main.pack(padx=5, pady=5, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "formula a = π r2"
    lbl_title = Label(frm_main, text="a = πr2")

    # Create a label that displays "Age:"
    lbl_r = Label(frm_main, text="Input a R value")

    # Create an integer entry box where the user will enter r value.
    ent_r = IntEntry(frm_main, width=4, lower_bound=0)

    # Create labels that will display the results.
    lbl_result = Label(frm_main, width=3)

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_title.grid(row=0, column=1, padx=0, pady=0)
    lbl_r.grid(row=2, column=1, padx=0, pady=3)
    ent_r.grid(row=2, column=2, padx=3, pady=3)
    

    lbl_result.grid(row=1, column=1, padx=35, pady=35)

    btn_clear.grid(row=3, column=1, padx=3, pady=3, columnspan=4, sticky="w")


    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the r from user.
            r = ent_r.get()

            # Compute the user's maximum heart rate.
            circle_area = math.pi*(r**2)
            print(circle_area)
            # Display the slowest and fastest benficial
            # heart rates for the user to see.
            lbl_result.config(text=f"{circle_area:.2f}")

        except ValueError:
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and fastest labels.
            lbl_result.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_r.clear()
        lbl_result.config(text="")
        ent_r.focus()

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_r.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_r.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
