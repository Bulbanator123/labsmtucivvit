# Класс
class UserAccount():
    def __init__(self, username: str, email: str, password: int):
        # Конструктор
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        # Безопасно меняет пароль аккаунта
        if not new_password:
            raise ValueError("Пароль не может быть пустым")

        if len(new_password) < 8:
            raise ValueError("Пароль должен содержать минимум 8 символов")

        if new_password == self.password:
            raise ValueError("Вы ввели предыдущий пароль")
        self.password = new_password

    def check_password(self, password):
        # Проверка правильности пароля
        return self.password == password


Daniil = UserAccount("_Dank0", "123@aaaaaaaaaaa.aa", "1eirere")
print(Daniil.check_password("p1o"))
print(Daniil.check_password("1eirere"))
Daniil.set_password("evjecwjc1342")
print(Daniil.check_password("1eirere"))
print(Daniil.check_password("evjecwjc1342"))
