def check_password():
    correct_password = "12345"
    user_input = input("Введите пароль: ")  
    if user_input == correct_password:
        print("Пароль верный! Доступ разрешен.")
    else:
        print("Неверный пароль. Доступ запрещен.")
check_password()
