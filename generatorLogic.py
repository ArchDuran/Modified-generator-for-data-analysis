import random

numbers = list(range(0,100000000))


def choice():
    a = random.choice(numbers) ** random.randint(1, 1000)       # Данная функция позволяет вытянуть 6 "случайных" значений из списка от 0 до десяти миллионов, с последующим
    b = random.choice(numbers) ** random.randint(1, 1000)       # возведением их в случайную степень от 1 до тысячи, что позволяет внести большее количество переменных в генерацию
    c = random.choice(numbers) ** random.randint(1, 1000)       # сид-фразы, а также увеличить длинну самой фразы. Это необходимо для уменьшения вероятности ее повторной генерации
    d = random.choice(numbers) ** random.randint(1, 1000)
    e = random.choice(numbers) ** random.randint(1, 1000)
    f = random.choice(numbers) ** random.randint(1, 1000)
    resultsum1 = (a * b * c * d * e * f ** 2) // 2
    resultsum2 = resultsum1 // 2
    resultsum3 = resultsum2 // 2
    resultsum4 = resultsum3 // 2
    resultsum5 = resultsum4 // 2
    resultsum6 = resultsum5 // 2
    return resultsum1, resultsum2, resultsum3, resultsum4, resultsum5, resultsum6