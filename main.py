spisok = []
num = int(input("vvedite kolichestvo chisel "))
for i in range(num): #запрашивает числа num раз и добавляет их в список
    a = int(input("chislo "))
    spisok.append(a)
spisok2 = [x ** 2 for x in spisok] #каждое число в списке возводит в квадрат
print(spisok2)
