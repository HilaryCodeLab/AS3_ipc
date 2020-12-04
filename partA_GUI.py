import tkinter as tk
from itertools import cycle
from tkinter import *

filehandle = open('requirements.txt', 'w')
filebuffer = ["colorise==1.0.1\n", "grpcio==1.33.2\n", "grpcio-tools==1.33.2\n", "protobuf==3.13.0\n", "pywin32==228\n", "six==1.15.0\n", "colour==0.1.5"]
filehandle.writelines(filebuffer)
filehandle.close()


class Colour1:
    """
    GUI component of main window for actual colors
    """
    def __init__(self, master):
        """

        :param master:
        """
        self.master = master
        # self.frame = tk.Frame(self.master)
        self.btn1 = tk.Button(self.master, text="open new window", command=self.open_new_window)
        self.btn1.place(x=50, y=50)
        self.btn1.pack()
        self.btn2 = tk.Button(self.master, text="Change Colours", command=self.change_color_and_text)
        self.btn2.place(x=100, y=100)
        self.btn2.pack()
        self.lbl1 = Label(self.master)
        self.lbl1.pack()
        self.lbl2 = Label(self.master, text="For First User, please click on instruction button BELOW")
        self.lbl2.pack()
        self.btn3 = tk.Button(self.master, text="Instruction", bg="pink", command=self.open_instruction_window)
        self.btn3.pack(side=BOTTOM)
        # self.frame.pack()
        self.actual_colors = ['#f00', '#008000', '#ffa500', '#00f', '#8a2be2', '#deb887', '#5f9ea0', '#7fff00', '#0ff',
                                '#fa8072']
        self.color_gen = cycle(self.actual_colors[1:])
        self.color_hex = 0

    def open_new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('300x300')
        self.newWindow.title("Complementary Colours")
        self.app = Colour2(self.newWindow)

    def open_instruction_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('300x300')
        self.newWindow.title("Instruction")
        self.app = Instruction(self.newWindow)

    def change_color_and_text(self):
        self.color_hex += self.actual_colors.index('#f00') + 1
        try:
            self.master.config(bg=next(self.color_gen))
            self.lbl1.config(text=self.actual_colors[self.color_hex])
        except IndexError:
            pass
            print("start again for color hex code")


class Colour2:
    """GUI component of second window for complementary colours"""
    def __init__(self, master2):
        self.master2 = master2
        # self.frame = tk.Frame(self.master)
        self.closeBtn = tk.Button(self.master2, text="Close", command=self.close_window)
        self.closeBtn.pack()
        # self.frame.pack()
        self.btn2 = tk.Button(self.master2, text="Change Colours", command=self.change_color_and_text)
        self.btn2.place(x=100, y=100)
        self.btn2.pack()
        self.lbl1 = Label(self.master2)
        self.lbl1.pack()
        self.complementary_colors = ['#008000', '#f00', '#00f', '#ffa500', '#ffae42', '#72baf3', '#a25d5d',
                                     '#20f', '#f00', '#73ecfa']
        self.color_gen2 = cycle(self.complementary_colors[1:])
        self.color_hex = 0

    def close_window(self):
        self.master2.destroy()

    def change_color_and_text(self):
        self.color_hex += self.complementary_colors.index('#008000') + 1
        try:
            self.master2.config(bg=next(self.color_gen2))
            self.lbl1.config(text=self.complementary_colors[self.color_hex])
        except IndexError:
            pass
            print("start again for color hex code")


class Instruction:
    """
    GUI component for instruction window
    """
    def __init__(self, master3):
        """

        :param master3:
        """
        self.master3 = master3
        # self.frame = tk.Frame(self.master)
        self.closeBtn = tk.Button(self.master3, text="Close", command=self.close_window )
        self.closeBtn.pack()
        self.lst = ['1. On "Main Colours" window, click on "open new window to open "Complementary Colors" window ',
                    '2. On "Main Colours" window, click on "Change Colours" once to see the color',
                    '3. On Complementary Colors, click on "Change Colours" once '
                    'to see the complementary colour to the colors of Main Colours',
                    '4. Repeat when necessary. The hex codes will stop updating after 10 clicks']

        t = Text(self.master3)
        for x in self.lst:
            t.insert(END, x + '\n')
        t.pack()

    def close_window(self):
        self.master3.destroy()


def main():
    root = tk.Tk()
    root.geometry('350x350')
    root.title("Main Colours")
    app = Colour1(root)
    root.mainloop()


if __name__ == '__main__':
    main()