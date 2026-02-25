fio = input("Введите Фамилию Имя Отчество: ").split()
if len(fio) >= 3:
    initials = f"{fio[0]} {fio[1][0]}.{fio[2][0]}."
    print("Инициалы:", initials)
else:
    print("Пожалуйста, введите ФИО полностью через пробел.")
