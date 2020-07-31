import tkinter


LARGE_FONT = ("Verdana, 12")


class App(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        # inherits arguments from super class.
        tkinter.Tk.__init__(self, *args, **kwargs)
        # creation of main frame and giving it parameters -> key values are self stands for App class
        main_frame = tkinter.Frame(self)
        main_frame.pack(side="top", fill="both", expand=True)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = StartPage(main_frame, self)
        self.frames[StartPage] = frame
        print(type(self.frames))
        print(self.frames)
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

