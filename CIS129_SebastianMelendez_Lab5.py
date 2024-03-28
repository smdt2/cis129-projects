#Sebastian Melendez Del Toro
#The program calculates how many bottles are returned in a week and the total payout for 7 days.

keep_going = 'y'
# Set variables and first while loop
while keep_going == 'y':
    total_bottles = 0
    counter = 1
    today_bottles = 0
    total_payout = 0

    # The variables are calculated

    while counter <= 7:
        today_bottles = int(input(f'Enter number of bottles returned for day #{counter}: '))
        counter = counter + 1
        total_bottles = total_bottles + today_bottles
        total_payout = total_bottles * .10

    #Prints out total_bottles and total_payout
    print(f'\nThe total number of bottles collected is {total_bottles}')
    print(f'The total paid out is ${total_payout:.2f}\n')

    #Asks if they wanna keep going or not
    keep_going = input('Do you want to enter another week\'s worth of data?\n(Enter y or n): ')
    print()

keep_going = 'y'
