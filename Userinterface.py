import Note


def createNote(number):
    title = checkInputLength(
        input('Введите название заметки: '), number)
    body = checkInputLength(
        input('Введите описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nЭто программа 'Заметки'. Имеются следующие функции:\n\n1 - вывод заметок\n2 - добавление\n3 - удаление\n4 - редактирование\n5 - выборка заметок по дате\n6 - показать заметку по id\n7 - выход\n\nВведите номер функции: ")


def checkInputLength(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите текст: ')
    else:
        return text


def close():
    print("Конец!")
