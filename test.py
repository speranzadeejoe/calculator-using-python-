from tkinter import *

# Create the main window
root = Tk()
root.title("CALCULATOR")
txtinp = StringVar()
operator = ""
def btnclick (number):
  global operator
  operator += str(number)
  txtinp.set(operator)

def clrop ():
  global operator
  operator = ""
  txtinp.set(operator)

def beq():
  global operator
  total = str(eval(operator))
  txtinp.set(total)

# Display Entry Field
txtdisplay = Entry(root,
                   bd=30,
                   font=('arial', 20, 'bold'),
                   insertwidth=4,
                   bg="light blue",
                   justify='right',
                   textvariable= txtinp )

txtdisplay.grid(columnspan=4)  # Corrected 'columnspan'

# Clear Button
btnclear = Button(root,
                  padx=59,
                  pady=15,
                  bd=8,
                  font=('arial', 20, 'bold'),
                  text="C",  # Fixed missing comma
                  bg="light blue",
                  command= clrop)

btnclear.grid(row=1, columnspan=2)  # Corrected 'columnspan'

# Button 1 "("
btn1 = Button(root,
              padx=19,  # Fixed missing comma
              pady=15,
              bd=8,
              font=('arial', 20, 'bold'),
              text="(",
              bg="light blue",
              command= lambda:btnclick("("))
btn1.grid(row=1, column=2)

btn2 = Button(root,
              padx=19,  # Fixed missing comma
              pady=15,
              bd=8,
              font=('arial', 20, 'bold'),
              text=")",
              bg="light blue",
              command= lambda:btnclick(")"))

btn2.grid(row=1, column=3)

btn7 = Button(root,
              padx=16,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text="7",
              bg="light blue",
              command= lambda:btnclick(7))

btn7.grid(row=2, column=0)

btn8 = Button(root,
              padx=16,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text="8",
              bg="light blue",
              command= lambda:btnclick(8))

btn8.grid(row=2, column=1)

btn9 = Button(root,
              padx=16,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text="9",
              bg="light blue",
              command= lambda:btnclick(9))

btn9.grid(row=2, column=2)

division = Button(root,
              padx=19,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text="/",
              bg="light blue",
              command= lambda:btnclick("/"))

division.grid(row=2, column=3)

btn4 = Button(root,
              padx=16,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text="4",
              bg="light blue",
              command= lambda:btnclick(4))

btn4.grid(row=3, column=0)

btn5 = Button(root,
              padx=16,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text="5",
              bg="light blue",
              command= lambda:btnclick(5))
      
btn5.grid(row=3, column=1)

btn6 = Button(root,
              padx=16,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text="6",
              bg="light blue",
              command= lambda:btnclick(6))

btn6.grid(row=3, column=2)

minus = Button(root,
              padx=19,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text="-",
              bg="light blue",
              command= lambda:btnclick("-"))

minus.grid(row=3, column=3)

btn1= Button(root,
              padx=16,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text="1",
              bg="light blue",
              command= lambda:btnclick(1))

btn1.grid(row=4, column=0)

btn2 = Button(root,
              padx=16,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text="2",
              bg="light blue",
              command= lambda:btnclick(2))
      
btn2.grid(row=4, column=1)

btn3 = Button(root,
              padx=16,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text="3",
              bg="light blue",
              command= lambda:btnclick(3))

btn3.grid(row=4, column=2)

multi= Button(root,
              padx=19,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text="*",
              bg="light blue",
              command= lambda:btnclick("*"))

multi.grid(row=4, column=3)

btn0 = Button(root,
              padx=16,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text="0",
              bg="light blue",
              command= lambda:btnclick(0))

btn0.grid(row=5, column=0)

btnd = Button(root,
              padx=16,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text=".",
              bg="light blue",
              command= lambda:btnclick("."))
      
btnd.grid(row=5, column=1)

equi = Button(root,
              padx=16,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text="=",
              bg="light blue",
              command= beq)

equi.grid(row=5, column=2)

addi = Button(root,
              padx=19,  # Fixed missing comma
              pady=16,
              bd=8,
              font=('arial', 20, 'bold'),
              text="+",
              bg="light blue",
              command= lambda:btnclick("+"))

addi.grid(row=5, column=3)

  # Added missing 'column' argument

# Run the main event loop
root.mainloop()
