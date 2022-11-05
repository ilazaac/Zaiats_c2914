import colorama

print(help(colorama))
print(colorama.Fore.CYAN + 'циановий текст')
print(colorama.Back.CYAN + colorama.Fore.BLACK + 'а тепер поміняємо)')
print(colorama.Style.BRIGHT + 'із жирним стилем')
print(colorama.Style.RESET_ALL + 'знову нормально')

print('Найважливіша функція Колорами - зміна параметрів тексту у консолі. А саме Back, Fore та Style')