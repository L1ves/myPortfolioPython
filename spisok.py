bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() +  "."
print(message)

cars = ['mercedes', 'bmv', 'toyota']
print('I whant sell ' + cars[2])

name = ['Leva', 'Viktor', 'Anton']
print("My friend is " + name[0])

motocycles = ['honda', 'bmv', 'yamaha']
motocycles[0] = 'ducati'
print (motocycles)

motocycles = ['honda', 'bmv', 'yamaha']
motocycles.append('ducati')
print (motocycles)

motocycles = []
motocycles.append('honda')
motocycles.append('bmv')
motocycles.append('yamaha')
print(motocycles)

motocycles = ['honda', 'bmv', 'yamaha']
motocycles.insert(1, 'ducatti')
print(motocycles)

motocycles = ['honda', 'bmv', 'yamaha']
del motocycles[0]
print(motocycles)

motocycles = ['honda', 'bmv', 'yamaha']
del motocycles[1]
print(motocycles)

motocycles = ['honda', 'bmv', 'yamaha']
print(motocycles)
new_motocycle = motocycles.pop()
print(motocycles)
print(new_motocycle)

motocycles = ['honda', 'bmv', 'yamaha']
last_owned = motocycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

motocycles = ['honda', 'bmv', 'yamaha']
motocycles.remove('yamaha')
print(motocycles)

motocycles = ['honda', 'bmv', 'yamaha']
print(motocycles)
too_expensive = 'yamaha'
motocycles.remove(too_expensive)
print(motocycles)
print("\nA " + too_expensive.title() + " is too expensive for me ")

guess = ['Viktor', 'Lev', 'Anton', 'Andrei']
print('I chalenge ' + guess[0] + ' in my villa')

guess = ['Viktor', 'Lev', 'Anton', 'Andrei']
print('I chalenge ' + guess[1] + ' in my villa')

guess = ['Viktor', 'Lev', 'Anton', 'Andrei']
print(guess)

not_come = 'Andrei'
guess.remove(not_come)
print(guess)
print(not_come)
print( "\nA " + not_come.upper() +  " is not come in my villa")
guess.append('Katya')
print(guess)
print("\nI chalenge " + guess[3] + " in my villa")
print(guess)
print("I present " + guess[0] + ", " + guess[1] + ", " + guess[2] + ", " + guess[3] + " come to me")
print("I present " + guess[0] + " come to me")
print("I present " + guess[1] + " come to me")
print("I present " + guess[2] + " come to me")
print("I present " + guess[3] + " come to me")
print(guess)
guess.append('Irina')
print("\nI present " + guess[4] + " come to me")
print(guess)
guess.append('Olya')
print("\nI present " + guess[5] + " come to me")
print(guess)
guess.append('Natasha')
print("\nI present " + guess[6] + " come to me")
print(guess)

guess = ['Viktor', 'Lev', 'Anton', 'Andrei']
print(guess)
not_come = 'Andrei'
guess.remove(not_come)
print(guess)
print(not_come)
print( "\nA " + not_come.upper() +  " is not come in my villa")
guess.append('Katya')
print(guess)
print("\nI chalenge " + guess[3] + " in my villa")
print(guess)
print("I present " + guess[0] + ", " + guess[1] + ", " + guess[2] + ", " + guess[3] + " come to me")
print("I present " + guess[0] + " come to me")
print("I present " + guess[1] + " come to me")
print("I present " + guess[2] + " come to me")
print("I present " + guess[3] + " come to me")
guess.insert(0, 'Masha')
print(guess)
guess.insert(3, 'Ksysha')
print(guess)
guess.append('Marina')
print(guess)
print("\nSorry my frend but on lunch i be came only two frinds " + guess[0] + " and " + guess[1] + ".")
print(guess)
first_guess = guess.pop()
print("\nI am very sorry " +  first_guess + " for what happened")
print(guess)
second_guess = guess.pop()
print("\nI am very sorry " + second_guess + " for what happened")
print(guess)
thre_guess = guess.pop()
print("\nI am really sorry " + thre_guess + " for what happened")
print(guess)
four_guess = guess.pop()
print("\nI am really sorry " + four_guess + " for what happened")
print(guess)
five_guess = guess.pop()
print("\nI am really sorry " + five_guess + " for what happened")
print(guess)
print("\nI chalenge " + guess[0] + "," + guess[1] + " in my villa")
print("\nI chalenge " + guess[0] + " in my villa")
print("\nI chalenge " + guess[1] + " in my villa")
print(guess)
del guess[1]
print(guess)
del guess[0]
print(guess)

guess = ['Viktor', 'Lev', 'Anton', 'Andrei']
len(guess)
