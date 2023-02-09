import tkinter as tk

class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x80")
        self.label = tk.Label(self.root, text = "Text to be read")

        self.button = tk.Button(self.root,
                                text="Read Label Text",
                                command=self.readLabelText)
        self.button.pack()
        self.label.pack()
        self.root.mainloop()

    def readLabelText(self):
        print(type(self.label.cget("text")))

app=Test()