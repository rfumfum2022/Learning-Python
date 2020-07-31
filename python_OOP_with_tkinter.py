import tkinter


LARGE_FONT = ("Verdana, 12")


class App(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        # inherits arguments from super class.
        tkinter.Tk.__init__(self, *args, **kwargs)
        # creation of main frame and giving it parameters --> self stands for App class (where frame is placed)
        main_frame = tkinter.Frame(self)
        # placing of the main frame
        main_frame.pack(side="top", fill="both", expand=True)
        # setting priority
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        # creation of dictionary frames
        self.frames = {}
        # creating of new instance of StartPage
        frame = StartPage(main_frame, self)
        # Frame content = { }
        self.frames[StartPage] = frame
        # How does line above add StartPage object to self.frames ?
        # Frame content = {<class '__main__.StartPage'>: <__main__.StartPage object .!frame.!startpage>}
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="StartPage", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


class EndPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="EndPage", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()

