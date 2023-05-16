def Fibonacci (fib_elements):
    first_number=0
    second_number=1
    next_number=first_number+second_number
    print(first_number,second_number,end=" ")
    for i in range(fib_elements):
        print(next_number,end=" ")
        first_number=second_number
        second_number=next_number
        next_number=first_number+second_number
        i+=1
    print('\n')
   
repeat=1
while repeat==1:
    user_number = int(input("How many Fibonacci elements you want to see? : "))
    if user_number==0:
        print(" your list is empty...")     
    elif user_number==1:
        print(0)   
    Fibonacci(user_number)
    print("\n")
    repeat=bool(input("Do you want to continue(1/0): "))
