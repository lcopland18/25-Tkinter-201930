"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Lauren Copland.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------

    root = tkinter.Tk()

    # -------------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------

    frame1 = ttk.Frame(root,padding = 10,relief = 'groove')
    frame2 = ttk.Frame(root,padding = 10,relief = 'groove')
    frame1.grid()
    frame2.grid()

    # -------------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------

    hello_button = ttk.Button(frame1, text="Hello, todo4")
    goodbye_button = ttk.Button(frame2, text="Goodbye, todo4")
    goodbye_button.grid()
    hello_button.grid()

    # -------------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------

    hello_button['command'] = (lambda: print_hello())
    goodbye_button['command'] = (lambda: print_goodbye())


    # -------------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------

    frame3 = ttk.Frame(root, padding=20, relief='raised')
    frame3.grid()

    entry_box = ttk.Entry(frame3)
    hello2 = ttk.Button(frame3, text = "Hello, todo6")
    entry_box.grid()
    hello2.grid()

    hello2['command'] = (lambda: input_box(entry_box))


    # -------------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    entry2 = ttk.Entry(frame3)
    third_button = ttk.Button(frame3,text = "Number of Prints")
    entry2.grid()
    third_button.grid()

    third_button['command'] = (lambda: entry2_function(entry_box, entry2))

    # -------------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------


    root.mainloop()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------

def print_hello():
    print("Hello")

def print_goodbye():
    print('Goodbye')

def input_box(insides):
    contents = insides.get()
    if contents == 'ok':
        print('Hello')
    else:
        print('Goodbye')

def entry2_function(insides,inside):
    word = insides.get()
    integer = int(inside.get())
    for k in range(integer):
        print(word)




main()
