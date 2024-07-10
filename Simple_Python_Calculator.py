#This adds two numbers
def add(x,y):
    return x+y
#This Function will be Subtraction
def Subtract(x,y):
    return x-y
#This Function will be mulitipication
def Multiply(x,y):
    return x * y
#This Function will be Division
def Division(x,y):
    return x/y

print("Select Operation")
print("1.add")
print("2.Subtract")
print("3.Multiply")
print("4.Division")

while True:
    choice=input("Enter Your Choice 1 / 2 / 3 / 4 : ")
    if choice in( '1', '2','3' , '4'):
        try:
            num1=int(input("Enter First Number"))
            num2=int(input("Enter Seccond Number"))
        except valueError:
            print("Invalid Number , Please Enter The Right Number")
            continue
        if choice== '1':
            print(num1,"+",num2 ,"=" ,add(num1 , num2))
        elif choice== '2':
            print(num1,"-",num2 ,"=" ,Subtract(num1 , num2))
        elif choice== '3':
            print(num1,"*",num2 ,"=" ,Multiply(num1 , num2))
        elif choice== '4':
            print(num1,"/",num2 ,"=" ,Division(num1 , num2))
        
        next_calculation=input("Yess / No : ")
        if next_calculation == "no":
            break
        else:
            print("invalid inpuut")