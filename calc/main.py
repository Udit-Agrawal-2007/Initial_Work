
import tkinter as tk

window = tk.Tk()
window.title("The Old Gen Calculator")
window.geometry("300x400")

label = []
operator = []
num1 = []
num2 = []

def calculatingresult():
  num1str = ""
  num2str = ""

  for i in num1:
    num1str = num1str + str(i)
  for i in num2:
    num2str = num2str + str(i)

  num1num = float(num1str)
  num2num = float(num2str)

  if operator[0] == "+":
    number = num1num + num2num
  elif operator[0] == "-":
    number = num1num - num2num
  elif operator[0] == "*":
    number = num1num * num2num
  elif operator[0] == "/":
    number = num1num / num2num  

  return number


def calculate():
  global label,num1,num2,operator
  num2start = False

  try:
    for i in label:
      if i == "+" or i == "-" or i == "*" or i == "/":
        if operator == []:
          operator.append(i)
          num2start = True
        else:
          num1.clear() 
          num2.clear()
          operator.clear()
          return "Error"
      elif num2start:
        num2.append(i)
      else:
        num1.append(i)

    return calculatingresult()      


  except Exception as error:
    print(error)
    return "Error"


def Pnumbers(input):
  global PANS,label
  answer = "" 

  if input == "0.00":
    label.clear()
    label.append("0.00")

  elif input == "":
    label = label[:-1]

  elif input == "=":
    ans = calculate()
    label.clear()
    num1.clear()
    num2.clear()
    operator.clear()
    label.append(ans)

  else:
    label.append(input)

  for i in label:
    if i == "0.00":
        label.remove(i)

    elif label == "":
      label.remove(i)

    else:
      pass
    answer = answer + str(i)

  PANS["text"] = answer  



PANS = tk.Label(text = "0.00")
PANS.grid(row =0 ,column = 4)

CC = tk.Button(text = " C ",command = lambda: Pnumbers("0.00"))
CC.grid(row = 1,column = 3)

C0 = tk.Button(text = " 0 ",command = lambda: Pnumbers(0)) 
C0.grid(row = 1,column = 4)

CER = tk.Button(text = "⌫",command = lambda: Pnumbers(""))
CER.grid(row = 1,column = 5)

C1 = tk.Button(text = " 1 ",command = lambda: Pnumbers(1))
C1.grid(row = 2,column = 3)

C2 = tk.Button(text = " 2 ",command = lambda: Pnumbers(2))
C2.grid(row = 2,column = 4)

C3 = tk.Button(text = " 3 ",command = lambda: Pnumbers(3))
C3.grid(row = 2,column = 5)

C4 = tk.Button(text = " 4 ",command = lambda: Pnumbers(4))
C4.grid(row = 3,column = 3)

C5 = tk.Button(text = " 5 ",command = lambda: Pnumbers(5))
C5.grid(row = 3,column = 4)

C6 = tk.Button(text = " 6 ",command = lambda: Pnumbers(6))
C6.grid(row = 3,column = 5)

C7 = tk.Button(text = " 7 ",command = lambda: Pnumbers(7))
C7.grid(row = 4,column = 3)

C8 = tk.Button(text = " 8 ",command = lambda: Pnumbers(8))
C8.grid(row = 4,column = 4)

C9 = tk.Button(text = " 9 ",command = lambda: Pnumbers(9))
C9.grid(row = 4,column = 5)

CP = tk.Button(text = " + ",command = lambda: Pnumbers("+"))
CP.grid(row = 5,column = 3)

CF = tk.Button(text = "  . ",command = lambda: Pnumbers("."))
CF.grid(row = 5,column = 4)

CS = tk.Button(text = "  - ",command = lambda: Pnumbers("-"))
CS.grid(row = 5,column = 5)

CD = tk.Button(text = "  / ",command = lambda: Pnumbers("/"))
CD.grid(row = 6,column = 3)

CM = tk.Button(text = "  * ",command = lambda: Pnumbers("*"))
CM.grid(row = 6,column = 4)

CE = tk.Button(text = " = ",command = lambda: Pnumbers("="))
CE.grid(row = 6,column = 5)



tk.mainloop()
