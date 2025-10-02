def read_file_exp(read_type: bool) -> None:
    try:
        if read_type:
            # Чтение всего файла
            with open('example.txt', 'r') as file:
                content = file.read()
                print(content)
            return

        # Построчное чтение
        with open('example.txt', 'r') as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print("Не найден файл example.txt! Создайте его")


# Здесь используется битик(bool type) для аргумента функции
# 0 - построчно, 1 - весь файл
read_file_exp(0)
print()
read_file_exp(1)
