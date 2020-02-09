file = open('text.txt', 'r', encoding='UTF-8')

line = ['Какой-то текст4', 'И еще4']

# text = file.write('Новая строка1\n')


for line in file:
    print(line)

file.close()