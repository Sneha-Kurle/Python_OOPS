#Exception- An event that interepts the flow
#ZeroDivisionError, ValueError, TypeError
# using try except finnaly 

try:
    a=int(input('enter a number   :'))
    print(1/a)
except ZeroDivisionError:
    print('Value can not be zero..')
except ValueError:
    print('Enete a valid number')
finally:
    print('Here you go..')

