from datetime import *
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU')

# print(now.strftime('%B'))
# print(now.strftime('%X'))

days = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']


now = datetime.now()

print(now.strftime('%c'))
d1 = now + timedelta(days=1, hours=2, minutes=10)
print(d1.strftime('%c'))
