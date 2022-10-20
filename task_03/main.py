# Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, 
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр1", "Илья", "Марина", "Петр2", "Алина", "Бибочка", "Ян", "Яна"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

alphabet='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
string = input("Введите сортируемые имена с большой буквы, в кавычках и через запятую : ")
arr = string.replace('"',"").replace("'","").split(', ')
print(arr)
# def SortByFirstLetter(array, alph):
#     res = {}
#     names = []
#     while len(array) > 0:
#         for j in alph:
#             for i in array:
#                 if i[0] == j:
#                     names.append(i)
#                     array.remove(i)
#                     #print(names)
#             if names != []:
#                 res[j] = names
#             names = []
#     return res
def SortByFirstLetter(array):
    res = {}
    for i in array:
        try:
            res[i[0]].append(i)
        except:
            res[i[0]] = [i]
    return res
print(SortByFirstLetter(arr))
