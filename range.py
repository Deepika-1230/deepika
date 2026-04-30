for i in range(6):
    print(i,end="")

    num1 =int(input("enter the number"))
    for i in range(1,num1+6):
        print(i)

        num2=int(input("enter the number"))
        count=0
        if(num2 <=1):
            print("not prime")
        else:
            for i in range(1,num2+1):
                if(num2 % i== 0):
                    count +=1

                if count == 2:
                    print("prime")
                else:
                    print("not prime")

for i in range(6):
    if i== 3:
        break
    print(i)

correct_password="hellokitty@123"
for i in range(6):
    password=input("enter the password")
    if (password=="correct_password"):
        print("successfull")
        break
    else:
        print("wrong password")
