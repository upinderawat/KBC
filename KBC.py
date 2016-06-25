from Tkinter import *
import tkMessageBox
import KBCdb
import random

root = Tk()
root.title("Lets Play KBC")

def clearScreen():
  mainFrame.destroy()
# Generating 1st question
def ask_question(lvl):
  """ Generates a number and gets the question from the database """
  global q
  qnum = int (random.random() * 10)
  q = KBCdb.get_question(lvl, qnum)
  global mainFrame
  mainFrame= Frame(root,width=500,height=500)  #creating Frame
  mainFrame.pack()

  l1 = Label(mainFrame,text= q[0])
  l1.pack()
  b1 = Button(mainFrame,text="A. " + q[1],command=lambda:check_answer(lvl,q[1]))
  b1.pack()
  b2 = Button(mainFrame,text="B. " + q[2],command=lambda:check_answer(lvl,q[2]))
  b2.pack()
  b3 = Button(mainFrame,text="C. " + q[3],command=lambda:check_answer(lvl,q[3]))
  b3.pack()
  b4 = Button(mainFrame,text="D. " + q[4],command=lambda:check_answer(lvl,q[4]))
  b4.pack()



  global correct_answer
  correct_answer = q[5]

def farewell(cash):
  tkMessageBox.showinfo(message="You won %d\nSee you next time" %cash)
  sys.stdout.flush()

def check_answer(lvl,choice):
  """ Checks the answer """
  balance = [0,1000,2500, 5000, 10000, 25000, 50000, 100000, 300000, 600000, 1200000, 2500000, 5000000, 10000000, 30000000, 50000000, ]

  global correct_answer, q
  if (correct_answer == choice):
    if (lvl == 14):
      tkMessageBox.showinfo("CONGRATULATIONS","YOU WON $1,000,000! \n "
                                              "You reached the top! "
                                              "This was an excellent game! Once again, congratulations!")
      quit()
    else:
      tkMessageBox.showinfo("Correct Answer","\n You got it right, You now have Rs%d"
                                            "\n Let's proceed to question %d " %(balance[lvl+1], lvl+2))
      clearScreen()
      ask_question(lvl+1)


  else:
    tkMessageBox.showinfo("Wrong Answer","\n Ups. The answer you chose is incorrect."
                                          "\n The right answer is %s." % correct_answer)
    farewell(balance[lvl])
    quit()

def main():
  level = 0   # Current question number
  correct_answer = ""
  q = []
  ask_question(0)

if __name__ =="__main__":
  main()




root.mainloop()


