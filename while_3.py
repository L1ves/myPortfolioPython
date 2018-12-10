# Начинаем с двух списков: пользователей для проверки
# и пустого списка для хранения проверенных пользователей.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Проверяем каждого пользователя, пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных.
while unconfirmed_users:
    curent_user = unconfirmed_users.pop()
    print("Verified users "  + curent_user.title())
    confirmed_users.append(curent_user)
    print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses = {}
# Установка флага продолжения опроса.
polling_active = True
while polling_active:
# Запрос имени и ответа пользователя.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
# Ответ сохраняется в словаре:
    responses[name] = response
# Проверка продолжения опроса.Использование цикла while со списками и словарями   133
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Опрос завершен, вывести результаты.
    print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

sandwich_order = ['bacon', 'chicken', 'pork', 'fish', 'pastrami', 'pastrami', 'pastrami']
finished_sandwich = []
print("\nI made your tuna sandwich" + str(sandwich_order))
print("pastrami is not defined")
while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')
print(sandwich_order)
while sandwich_order:
    sandwich = sandwich_order.pop()
    finished_sandwich.append(sandwich)
print("All sandwiches is finished " + str(finished_sandwich))

dream_travels = {}
polling_active = True
while polling_active:
#запрос имени и ответа пользователя
    name = input("\nWhat is youre name? ")
    responses = input("What youre favorite country ")
# Ответ сохраняется в словаре:
    dream_travels[name] = response
# Проверка продолжения опроса.Использование цикла while со списками и словарями   133
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        print("\n--- Poll Results ---")
for name, dream_travel in dream_travels.items():
    print(name + " favorite country is : " + dream_travel)
