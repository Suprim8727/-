##numberOne=int(input("Введите число - "))
##numberTwo=int(input("ратно чему - "))
##sumresult= 0
##finishNumber = numberOne
##
##while sumresult < finishNumber:
##    sumresult += numberTwo
##
##if sumresult == finishNumber:
##    print("Числа кратны!")
##else:
##    print("Числа не кратны!")

name = input("Введите имя: ")
stars = "*" * (len(name) + 4)
print(stars + "\n" + name + "*\n" + stars)
