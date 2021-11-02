algebraic_equation = input("Please insert the equation in ax+b=c, where x is to be solved and a, b, and c are numbers. \n")
ae = algebraic_equation
ael = list(ae)

plus = True
divide = False

def reverseOrder(tr):
    tr = str(tr)
    d = tr[::-1]
    return d

#et

et = 0
b = ""
while True:
    a = ael.pop()
    if(a == "="):
        break
    if(a != "="):
        b += a
et = int(reverseOrder(b))

#constant

constant = 0
bc = ""
while True:
    ac = ael.pop()
    if(ac == "+"):
        break
    if(ac == "-"):
        plus = False
        break
    if(ac != "+" and ac != "-"):
        bc += ac
        
constant = int(reverseOrder(bc))
if(plus == False):
    constant *= -1

#coefficient

coefficient = 0
bcc = ""
while True:
    if(len(ael) == 0):
        break
    acc = ael.pop()
    if(acc != "+" and acc != "x" and acc != "/"):
        bcc += acc
    if(acc == "/"):
        divide = True
coefficient = int(reverseOrder(bcc))

#solution

ans1 = et - constant
if(divide == False):
    ans2 = ans1 / coefficient
elif(divide == True):
    ans2 = coefficient * ans1
fa = ans2

#prints
'''
print("coefficient: ", coefficient)
print("constant: ", constant)
print("et: ", et)
----------
print(coefficient)
print(constant)
'''
print(fa)
