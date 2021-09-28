import tkinter as ttk

def StartGame():
    root = ttk.Tk()
    root.title("Maths Quiz - Trigonometry and Pythagoras' Theorem | Start The Game")
    root.geometry("640x480")
    root.configure(background = "gray92")
    TotScore = 0
    Count = 0
    while Count < 10:
        AnswerReply = None
        WorkingArea = ttk.Text(root, width = 70, height = 10, wrap = WORD).place(x = 38, y = 100)
        n = 10
        Question, RealAnswer = QuestionLibrary(Opposite,Adjacent,Hypotenuse,Angle,n)
        AskQuestion = Label(root, text = Question).place(x = 38, y = 300)
        PauseButton = ttk.Button(root, text = "Pause").place(x = 380, y = 10)
        HelpButton = ttk.Button(root, text = "Help", command = helpbutton_click).place(x = 460, y = 10)
        QuitButton = ttk.Button(root, text = "Quit", command = root.destroy).place(x = 540, y = 10)
        AnswerEntry = Entry(root)
        AnswerEntry.place(x = 252, y = 375)
        SubmitButton = ttk.Button(root, text = "Submit", command = submit_answer).place(x = 276, y = 400)
        Count += 1
    root.mainloop()
StartGame()