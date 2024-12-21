spisok = []
num = int(input("введите количество чисел"))
for i in range(num): #запрашивает числа num раз и добавляет их в список
    a = int(input("chislo "))
    spisok.append(a)
print(spisok)
spisok2 = [x ** 2 for x in spisok] #каждое число в списке возводит в квадрат
print(spisok2)
