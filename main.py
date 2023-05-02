n = int(input('Количество чисел в списке: '))
index_num = []
index_summa = 0

for _ in range(n):
    num = int(input('введите число: '))
    index_num.append(num)
    k = int(input('Введите делитель: '))
for i in index_num :
    if i // k == 0:
        







nums_list = []
N = int(input('Кол-во чисел в списке: '))
for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)
maximum = 0
minimum = 0
for i in nums_list:
    if maximum < i:
        maximum = i
    if minimum > i:
        minimum = i
print('Максимальное число в списке:', maximum)
print('Минимальное число в списке:', minimum)



office_now = int(input('количество сотрудников в офисе: '))
id = []
for _ in range (office_now):
    now = int(input('Номер пропуска сотрудника: '))
    id.append(now)

searh = int(input('номер пропуска нужного сотрудника: '))

if searh not in id:
    print('сотрудника нет в офисе')
else:
    print('сотрудник  в офисе')









books_ID = [20, 39, 49, 12, -1, 45, -1 , - 1, -1, 1]
new_books_ID = []
reterned = 0

for _ in range(7):
    id = int(input('введите номер выданной книги: '))
    books_ID.append(id)

for id in books_ID:
    if id == -1:
        reterned += 1
    else:
        new_books_ID.append(id)
print('новый список выданных книг:', new_books_ID)
print('количество возврашенных книг:', reterned)















for i in range(100 + 1):
    numbers.append(i)
print(numbers)

numbers = [3,7,5]

while True:
    number = int(input('Новое число: '))
    numbers.append(number)
    print('Текущий список чисел:', numbers)
    for i in numbers:
        print(i ** 2, i ** 3, i ** 4)
print()



books_ID = [50, 34, -1, -1, 23, -1]
new_books_ID = []
returned = 0

for _ in range(10):
    id = int(input('Введите ID книги: '))
    books_ID.append(id)

for id in books_ID:
    if id == -1:
        returned += 1
    else:
        new_books_ID.append(id)

print('Новый список выданных книг:', new_books_ID)
print('Возврвщено за день:', returned, 'книг')