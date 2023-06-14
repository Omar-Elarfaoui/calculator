print('1_ la multiplication ')
print("2_ l'addition ")
print("3_ la soustraction")
print("4_ la division")
choise = int(input("choise your operation :"))
num1 = int(input('enter the 1ere number :'))
num2 = int(input('enter the 2eme number :'))
if choise == 1 :
    print(num1 * num2 )
elif choise == 2 :
    print(num1+num2)
elif choise == 3:
    print(num1-num2)
elif choise == 4 :
    print(num1/num2)
else :
    print("sorry")