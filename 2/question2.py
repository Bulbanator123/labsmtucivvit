def describe_person(name: str, age: int = 30) -> str:
    years = "лет"
    if age < 0:
        print("Ваш человек ещё не родился")
        return
    elif age == 1:
        years = "год"
    elif age == 2 or age == 3 or age == 4:
        years = "года"
    print(f"Человек с именем {name}, ему {age} {years}")


describe_person("Илья", -1)
describe_person("Илья", 0)
describe_person("Илья", 10)
describe_person("Илья", 2)
describe_person("Илья", 1)
describe_person("Илья")

# ошибки

# describe_person("Илья", 2, 3)
# функция принимает только 2 аргумента или первый

# describe_person(1, 1)
# функция принимает первый аргумент только как строку,
# а второй только как целочисленное число
