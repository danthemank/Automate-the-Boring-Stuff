#Exception handling example

try:
    print(10/0)

except ZeroDivisionError:
    print('Dividing by 0 causes an error!')