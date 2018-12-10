requested_toppings = ['green pepper', 'extra cheese', 'mushrooms']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("Finished making youre pizza!")

requested_toppings = ['green pepper', 'extra cheese', 'mushrooms']
for requested_topping in requested_toppings:
    if requested_topping == 'green pepper':
        print("Sorry we are out green pepper right now")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making yore pizza!")


requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making youre pizza!")
else:
    print("Are you shore you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry we dont have " + requested_topping)
print("\nFinished making youre pizza!")


hello_admin = ['user', 'admin', 'noob', ' hacker', 'kracker']
for hello_admins in hello_admin:
    if hello_admins == 'admin':
        print("Hello " + hello_admins + ", would you like to see a status report?")
    else:
        print("Hello " + hello_admins + " thank you for logging in again!")
