

user_input = input('What is your weather state (cold, warm  or hot) :\n ? ').lower()

reminder = f'Youre currently experience weather. '

if user_input =='cold':
    reminder += 'Weather warm cloth to avoid sickness!!'
elif user_input == 'warm':
    reminder += 'You can wear your refreshing cloth, remember to Drink Water'
elif user_input == 'hot':
    reminder += 'Its not a frendly weather. Wear shades to protect your eyes against \'UV\' and to drink a lot of water '
else:
    print('Wrong input,  or bad respond, try again! ')
print(reminder)