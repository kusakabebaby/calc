operation = input('''
Пожалуйста введите математическую операцию, которую вы бы хотели выполнить:
+ для сложения
- для вычитания
* для умножения
/ для деления
''')
num1 = int(input("введите первое число:"))
num2 = int(input("введите второе число:"))


if operation == '+':
    print('{} + {} = '.format(num1, num2))
    print("результат:", num1 + num2)
elif operation == '-':
    print('{} - {} = '.format(num1, num2))
    print("результат:", num1 - num2)
elif operation == '/':
    print('{} / {} = '.format(numb1, num2))
    print("результат:", num1 / num2)
elif operation == '*':
    print('{} * {} = '.format(num1, num2))
    print("результат:", num1 * num2)
else:
    print("вы неправильно ввели оператора, попробуйте еще раз")

