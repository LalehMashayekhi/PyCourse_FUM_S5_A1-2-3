def Fibonacci (endgoal):
    first_number=0
    second_number=1
    next_number=first_number+second_number
    print(first_number,second_number,end=" ")
    while next_number<endgoal:
        first_number=second_number
        second_number=next_number
        next_number=first_number+second_number
        if next_number<endgoal:
            print(next_number,end=" ")
    if next_number==endgoal:
        next_number=endgoal
        print(endgoal,end=" ")
    elif next_number>endgoal:
        print('\n')

repeat=1
count=1
while repeat==1:
    user_number=int(input("Enter your end goal number: "))        
    Fibonacci(user_number)
    print("Counter: ",count)
    print("\n")
    repeat=int(input("Do you want to continue(1/0): "))
    count+=1
