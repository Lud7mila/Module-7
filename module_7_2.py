info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding = 'utf-8')
    result = {}

    for ind in range(len(strings)):
        result[(ind+1,file.tell())] = strings[ind]
        #print(f'result[({ind+1}, {file.tell()})] = "{strings[ind]}"')
        file.write(strings[ind] + '\n')

    file.close()
    return result


result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)



