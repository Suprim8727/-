numberOne = int(input("Введите число -"))
numberTwo = int(input("кратна чему -"))
sumResult = 0
finishNumber = numberOne

while sumResult < finishNumber:
    sumResult += numberTwo

if sumResult == finishNumber:
    print("Числа кратны!")
else:
    print("Числа не кратны!")
