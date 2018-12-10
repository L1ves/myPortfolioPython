curent_user = ['user', 'admin', 'Noob', 'hacker', 'kracker', 'manager', 'ceo', 'military']
new_users = ['user', 'ADMIN', 'noob', 'Hacker', 'Kracker','bla', 'tratata']
for new_user in new_users:
    if new_user.lower() in curent_user or new_user.upper() in curent_user:
        print("Sorry, " + new_user + " choise a new users name!")
else:
    print("You are welcome " + new_user)
print("\nHi all")

numbers = ['1','2','3','4','5','6','7','8','9']
for number in numbers:
    if number == '1':
        print(number + "st")
    elif number == '2':
        print(number + "nd")
    elif number == '4':
        print(number + "th")
    elif number == '5':
            print(number + "th")
    elif number == '6':
        print(number + "th")
    elif number == '7':
        print(number + "th")
    elif number == '8':
        print(number + "th")
    elif number == '3':
        print(number + "rd")
else:
    print(number + "th")
