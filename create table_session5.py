#ask user for rows and columns
    #print #* on even rows and *# on odd numbers of rows
    #r=int(input("Enetr the number of rows: "))
    #c=int(input("Enter the number of columns: "))
def create_table(r,c):
    for row in range (r):
        for colunm in range(c):
            if row%2==0:
                print("#*", end=" ")
            else:
                print("*#", end=" ")
            colunm+=1 #the programme works perfectly without it
        print(end="\n")
            
n=int(input("Enter the number of rows: "))
m=int(input("Enter the the number of columns: "))
create_table(n,m)               
     
        