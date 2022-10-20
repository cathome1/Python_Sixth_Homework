# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
s = int(input('Введите число больше 20: '))
def MultipleTwentyAndTwentyOne (num):
    res = []
    if num > 20:
        for i in range(20,num+1):
            if i % 20 == 0 or i % 21 == 0:
                res.append(i)
        return res
    print('Число должно быть больше 20')
print(MultipleTwentyAndTwentyOne(s))