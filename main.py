# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#Module 3_1
#"Пространство имён"

calls = 0

def count_calls ():    # Создаём функцию count_calls и изменять в ней значение переменной calls.
    global calls
    calls+=1



def string_info (string):       # Создаём функцию string_info с параметром string
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains (string, list_to_search):# Создаём функцию is_contains с двумя параметрами string и list_to_search
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]
                     # Вывод результата
print(string_info('Simferopol'))
print(string_info('Yalta'))
print(string_info('Черное море'))
print(is_contains('Informatika', ['Inform', 'ROmantic', 'INFORmaTika']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)