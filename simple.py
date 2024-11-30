#Осуществляем ввод переменных
a = int(input())
q = int(input())
n = int(input ())
#Присваиваем сумме значение первого элемента
sum = a
#С помощью цикла подсчитываем сумму и выводим ее
for i in range (1, n):
     sum = sum + a*(q**i)
print(sum)
