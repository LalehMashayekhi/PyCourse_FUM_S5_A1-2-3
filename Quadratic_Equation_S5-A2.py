#  ax**2+bx+c=0
# delta= b**2-4ac
# if delta > 0:
    # x1=(-b-sqrt delta)/a*2   OR  (-b+sqrt delta)/a*2
#if delta =0 
    #x1=x2
    
import math
def solve_quadric_equation(A,B,C):
    delta=(B**2)-(4*A*C)
    if delta>0:
        x1=(((-B)- (math.sqrt (delta)))/(2*A))
        x2=(((-B)+( math.sqrt (delta)))/(2*A))
        print("your results are: ", x1 ,"And" , x2)
    elif delta==0:
        x=((-B)/(2*A))
        print("you only have one answere: ", x)
    else:
         print("the Delta is less than Zero you will have complex roots")
         print("your answers are: " ,(-B)/(2*A), "+i" , math.sqrt(abs(delta)) , "And" , (-B)/(2*A) , "-i" , math.sqrt(abs(delta)))

a= float(input("Enter a number as a: "))
b=float(input("Enter a number as b: "))
c=float(input("Enter a number as c: "))
if a==0:
    print("You have entered 0 as a, which is unvalid, try again")
solve_quadric_equation(a,b,c)


        
    