import csv #импортируем библиотеку для чтения таблицы(Строчка 1)

#Открываем файл для чтения таблицы(Строчка 4-6)
with open('vacancy_new.csv','r') as table:
    inf = csv.reader(table)
    next(inf)

#Создаем цикл , который будет считывать данные из файла и добавлять в список. (Строчка 9-14)
vacancy = ()

for row in inf:
    salary,role,company = row
    salary = int(salary)
    vacancy.append({'company':company,'role':role,'salary':salary})
#Сортируем список по зарплате(Строчка 16)
vacancy.sort(key = lambda x: x(salary),reverse = True)
#Выводим топ 3 компании по зарплате
for i in range(3):
    print(f"company:{vacancy'Company'},role:{vacancy'role'},salary:{vacancy'salary'}")