from Tkinter import *
import random
import KBCdb
import tkMessageBox

root = Tk()
quesWin = Toplevel(root)
bottomFrame= Frame(quesWin,width=500,height=100,bg="#330033")
bottomFrame.pack(side=BOTTOM)

def swapLifeline(lvl):
    prop={"fg":"white","bg":"#00FF00","activebackground":"orange"}

    b7= Button(bottomFrame,text="Swap the question",cnf=prop,width=20)
    b7.grid(row=3,column=2)
    b7.config(command=lambda:swap(b7,lvl))
    def swap(b7,lvl):
        global swaplife
        #print "lvl is ",lvl
        b7.config(state=DISABLED,bg="red")
        clearScreen()
        swaplife=False
        ask_question(lvl)

def audLifeline(lvl):
    prop={"fg":"white","bg":"#00FF00","activebackground":"orange"}
    b5 = Button(bottomFrame,text="Audience Poll",cnf=prop,width=20)
    b5.grid(row=3,column=0)
    b5.config(command=lambda :AudiencePoll(b5))

    def AudiencePoll(b5):
      global audlife
      audlife=False
      b5.config(state=DISABLED,bg="red")
      while True:
        Majority=random.random()
        if Majority>0.45:
          Majority *=100
          break
      tkMessageBox.showinfo(title="Audience Poll",message="%d percent of Audience Thinks the Answer is %s "%(Majority,q[5]))

def clearScreen(): #Used to clear the frame for the Next question
  mainFrame.destroy()

def farewell(cash):
  tkMessageBox.showinfo(message="You won %d\nSee you next time" %cash)

def check_answer(lvl,choice):
  """ Checks the answer """
  balance = [0,1000,2500, 5000, 10000, 25000, 50000, 100000, 300000, 600000, 1200000, 2500000, 5000000, 10000000, 30000000, 50000000 ]

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

def ask_question(lvl):

  """ Generates a number and gets the question from the database """

  global q , audlife, swaplife
  qnum = int (random.random() * 10)
  q = KBCdb.get_question(lvl, qnum)
  global mainFrame
  mainFrame= Frame(quesWin,width=500,height=500,bg="#330033")  #creating Frame
  mainFrame.pack()
  prop={"fg":"white","bg":"#330033","activebackground":"orange"}
  l1 = Label(mainFrame,text= q[0],cnf=prop)
  l1.grid(row=0,column=0,columnspan=2)
  b1 = Button(mainFrame,text="A. " + q[1],cnf=prop,width=20,command=lambda:check_answer(lvl,q[1]))
  b1.grid(row=1,column=0)
  b2 = Button(mainFrame,text="B. " + q[2],cnf=prop,width=20,command=lambda:check_answer(lvl,q[2]))
  b2.grid(row=1,column=1)
  b3 = Button(mainFrame,text="C. " + q[3],cnf=prop,width=20,command=lambda:check_answer(lvl,q[3]))
  b3.grid(row=2,column=0)
  b4 = Button(mainFrame,text="D. " + q[4],cnf=prop,width=20,command=lambda:check_answer(lvl,q[4]))
  b4.grid(row=2,column=1)

  global correct_answer
  correct_answer = q[5]
  if audlife:
      #print lvl,") audlife is still available"
      audLifeline(lvl)
  if swaplife:
      #print lvl,") swap is still available"
      swapLifeline(lvl)
  quesWin.mainloop()

def welcomeWin():
    mainWin = Frame(root,width=500,height=500,bg="#330033")
    mainWin.pack(fill=BOTH)
    logo= PhotoImage(file="kbc.png")
    Label(master= mainWin,image=logo).grid(row=0,column=0)
    bg1={'bg':"#330033",'fg':"white"}
    Label(mainWin,text="QUESTION 15---- RS 5 CRORES",cnf=bg1).grid(row=1,column=0)
    Label(mainWin,text="QUESTION 14---- RS 3 CRORES",cnf=bg1).grid(row=2,column=0)
    Label(mainWin,text="QUESTION 13---- RS 1 CRORES",cnf=bg1).grid(row=3,column=0)
    Label(mainWin,text="QUESTION 12---- RS 50 lakhs",cnf=bg1).grid(row=4,column=0)
    Label(mainWin,text="QUESTION 11---- RS 25 lakhs",cnf=bg1).grid(row=5,column=0)
    Label(mainWin,text="QUESTION 10---- RS 12 lakhs",cnf=bg1).grid(row=6,column=0)
    Label(mainWin,text="QUESTION 9 ---- RS 6 lakhs",cnf=bg1).grid(row=7,column=0)
    Label(mainWin,text="QUESTION 8 ---- RS 3 lakhs",cnf=bg1).grid(row=8,column=0)
    Label(mainWin,text="QUESTION 7 ---- RS 1 lakhs",cnf=bg1).grid(row=9,column=0)
    Label(mainWin,text="QUESTION 6 ---- RS 50,000",cnf=bg1).grid(row=10,column=0)
    Label(mainWin,text="QUESTION 5 ---- RS 25,000",cnf=bg1).grid(row=11,column=0)
    Label(mainWin,text="QUESTION 4 ---- RS 10,000",cnf=bg1).grid(row=12,column=0)
    Label(mainWin,text="QUESTION 3 ---- RS 5,000",cnf=bg1).grid(row=13,column=0)
    Label(mainWin,text="QUESTION 2 ---- RS 25,00",cnf=bg1).grid(row=14,column=0)
    Label(mainWin,text="QUESTION 1 ---- RS 1,000",cnf=bg1).grid(row=15,column=0)

    b1= Button(mainWin,text="Start",command=lambda :ask_question(0)).grid(row=16)

    root.mainloop()

def main():
  lvl = 0  # Current question number
  global correct_answer,q,swaplife,audlife
  correct_answer = ""
  q = []
  swaplife=True
  audlife=True

  welcomeWin()
if __name__ == "__main__":
  main()