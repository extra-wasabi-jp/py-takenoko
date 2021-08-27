from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()

frame1 = ttk.Frame(root, padding=10)

label1 = ttk.Label(frame1, text='Hello, World')

button1 = ttk.Button(frame1, text='OK', command=lambda: {
    messagebox.showinfo(title='ようこそ', message='ようこそ、py-takenoko へ')
})


def main():
    root.title('sample_gui')
    frame1.pack()
    label1.pack(side=LEFT)
    button1.pack(side=LEFT)
    root.geometry('800x600')
    root.mainloop()


if __name__ == '__main__':
    main()
