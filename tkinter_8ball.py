# MAGIC 8-BALL (25pts)
# Create a tkinter app which acts as a "Magic 8-ball" fortune teller
# The user asks a yes/no question that they want an answer to.
# Then the user clicks a button, and your program displays
# the "magic" random answer to their question.
# Your program will have the following properties:
# - Use an App class to create the tkinter app
# - Add a proper title (appears in the window tab)
# - Add a Label widget at the top to give the user instructions/intro.
# - Add an Entry widget so the user can enter their question.
# - Add a Button widget which will trigger the answer.
# - Add a Label widget to display the answer (set to a initial value of "Your Fortune Here" or "--" or similar)
# - Get your random answer message from a list of at least 10 possible strings. (e.g. ["Yes", "No", "Most Likely", "Definitely", etc...])
# - Add THREE or more other style modifications to make your app unique (font family, font size, color, padding, image, borders, justification, whatever you can find in tkinter library etc.)  Make a comment at the top or bottom of your code to tell me your 3 things you did. (Just to help me out in checking your assignment)
from tkinter import *
from tkinter import font
import random


# noinspection PyBroadException
class App():



    def __init__(self,master):
        self.myString = StringVar()
        self.answer=StringVar()
        self.myString.set("------")

        self.title_font=font.Font(family="Comic Sans MS", size=17)
        self.new_font=font.Font(family="Comic Sans MS", size=23)

        self.question_button = Label(master, text="Type your question : ", font=self.title_font,bg="black",fg="gold")
        self.question_button.grid(row=3, column=0, sticky="e" + "w")

        self.enter = Entry(master, textvariable=self.myString,font=self.title_font,borderwidth=5,highlightcolor="black",justify="center")
        self.enter.grid(row=3, column=1,sticky="e"+"w")

        self.button = Label(master, text="ASK!", font=self.title_font,bg="black",fg="gold")
        self.button.bind("<Button-1>", self.concat)
        self.button.grid(row=3, column=2,sticky="e"+"w")

        self.answer_label = Label(master, textvariable=self.answer, font=self.new_font,fg="red", width=10, borderwidth=5)
        self.answer_label.grid(row=4, column=0,columnspan=3, sticky="w" + "e")

    def concat(self, event):
        answer_list=["Does not matter","Irrelevant","I do not care","Ehhh.... Whatever, Sure","No one cares","Leave me alone","Meh","Whatever","No.","Definitely No"]
        self.answer.set("Answer: "+answer_list[random.randrange(0,9)])


    #def concat(self,event):
       # try:
      #      self.grav.set(self.m1.get() * self.m2.get() / (self.r.get() * self.r.get()) * 0.0000000000667)
      #  except ZeroDivisionError:
      #      self.grav.set("Not divisible by 0")
       # except:
       #     self.grav.set("Type Error")
if __name__ == "__main__":
    root = Tk()
    root.title("Question Genie(Magic 8-Ball")
    my_app = App(root)

    img = PhotoImage(file="images/8_ball.gif")
    img.bg="white"

    Label(root, image=img).grid(row=0,column=1,sticky="w")


    root.mainloop()

