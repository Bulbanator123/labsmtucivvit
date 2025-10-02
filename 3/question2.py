text = input("Введите текст: ")
new_str = bool(input("На новой строчке(1 - да, 0 - нет)? "))
with open("user_input.txt", "a") as file:
    # в первом пункте задания достаточно и режима w
    if new_str:
        file.write("\n" + text)
    else:
        file.write(text)
