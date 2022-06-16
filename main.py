import random
from tkinter.messagebox import NO
from generatorLogic import choice
from database import connection, cursor


def default_chance_generator():     # В данном генераторе источником энтропии
    result1 = random.randint(1,12)  # будет выступать стандартная для ЭВМ схема
    result2 = random.randint(1,12)  # в которой за основу будет браться системное
    result3 = random.randint(1,12)  # время
    result4 = random.randint(1,12)
    result5 = random.randint(1,12)
    result6 = random.randint(1,12)
    return result1, result2, result3, result4, result5, result6


def cicle(i):            # Данная функцция выполняет симуляцию генерации необходимого количества рядов из 6 случайных элементов, с последующим
    while i > 0:         # занесением их в базу данных для будущего анализа. Для генерации испальзуется стандартный ГСЧ
        i -= 1
        results = default_chance_generator()
        cursor.execute("INSERT INTO DefaultNumbers VALUES (?,?,?,?,?,?)",  results)
        connection.commit()


def modified_chance_generator():        # Данный генератор предполагает использование случайно сгенерированных сид-фраз,
        resultsum = choice()            # полученных в результате неоднократной генерации случайных чисел, а также их математического
        random.seed(resultsum[0])       # преобразования, следовательно в некотором смысле меняется источник энтропии, а следовательно мы имеем
        result1 = random.randint(1,12)  # модифицированный стандартный ГСЧ
        random.seed(resultsum[1])
        result2 = random.randint(1,12)
        random.seed(resultsum[2])
        result3 = random.randint(1,12)
        random.seed(resultsum[3])
        result4 = random.randint(1,12)
        random.seed(resultsum[4])
        result5 = random.randint(1,12)
        random.seed(resultsum[5])
        result6 = random.randint(1,12)
        return result1, result2, result3, result4, result5, result6


def modified_cicle(i):                  # Данная функцция выполняет симуляцию генерации необходимого количества рядов из 6 случайных элементов, с последующим
    while i > 0:                        # занесением их в базу данных для будущего анализа. Для генерации испальзуется модифицированный ГСЧ
        i -= 1
        results = modified_chance_generator()
        cursor.execute("INSERT INTO ModifiedNumbers VALUES (?,?,?,?,?,?)",  results)
        connection.commit()

tries = int(input("Введите количество бросков: "))

cicle(tries)
modified_cicle(tries)