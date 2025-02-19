# write a python program which will keep adding a string of numbers inputted by
# the user .the adding stops as soon as user press a q key on the keyboard



sum = 0

while(True):
    for item in range(1,1000):
        user_input = input(f'enter the price of the item {item}:\n')
        try:
            if(user_input != 'q'):
                sum = sum + int(user_input)
                print(f'order total so far {sum}')

            else:
                print(f'your total bill amount is{sum}')
                print(f"thank you for shoping")
        except:
            print("invalid input")

            break
 











