import random 
def ask():
    a=int(input("Which tables do u want me to ask , sir ? , please type the table number : "))
    while True:
        for i in range(12):
            b=random.randint(0,11)
            print("Now",a,"X",b,"= ?")
            z=int(input("Enter your answer : "))
            if (z==a*b):
                print("The answer is correct!!")
            else:
                print("The answer is inncorrect,please retype the correct answer ,but Siri the correct answer is",a*b)
                c=int(input("Enter the correct answer : "))
                if (c==a*b):
                    print("The answer is correct!!")
                else :
                    print("Sorry , it was a wrong answer ,but Siri the correct answer is",a*b,"!!")
