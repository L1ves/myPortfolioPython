january = 'январь'
february = 'февраль'
march = 'март'
april = 'апрель'
may = 'май'
june = 'июнь'
jule = 'июль'
awguste = 'август'
september = 'сентябрь'
october = 'октябрь'
november = 'ноябрь'
december = 'декабрь'
message1 = input("Введите месяц от 1 до 12 или введите  (exit)")
if message1 == '1':
    print(january)
if message1 == '2':
    print(february)
if message1 == '3':
    print(march)
if message1 == '4':
    print(april)
if message1 == '5':
    print(may)
if message1 == '6':
    print(june)
if message1 == '7':
    print(jule)
if message1 == '8':
    print(awguste)
if message1 == '9':
    print(september)
if message1 == '10':
    print(october)
if message1 == '11':
    print(november)
if message1 == '12':
    print(december)
elif message1 == "exit":
    exit("buy")

password = 12345
message3 = input("Введите пароль --> ")
if message3 == '12345':
    print("Password is correct! ")
else:
    print("Пароль введен не верно! \n Экстренный выход!")

age = 18
older = 55
question = input("введите свой возраст: ")
if int(question) <= 18:
    answer = "younger "
if int(question) <= 55:
    question = "normal! "
else:
    question = "older man! "
print("You age is: + " + question + ".")

a = input("Угадай число: ")
if  int(a)%3 == 0:
    print("Поздравляю ваше число кратно трем, вы заработали миллиард! ")
else:
    print("Game over, повезет в любви!")
