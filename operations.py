import csv
import os
import title


def create():
    contact_fields = ["Имя", "Номер телефона"]
    contact_data = []
    os.system('cls')
    title.title()
    print("    Создать контакт:")
    print("    ---------------")
    print("")
    for i in contact_fields:
        contact_details = input("    Ввод " + i + ":")
        print("")
        contact_data.append(contact_details)

    with open("contacts.csv", 'a') as file:
        write = csv.writer(file)
        write.writerows([contact_data])
    contact_data = []
    print("")
    print("Контакт успешно создан".center(129))
    print("\n")



def view():
    contact_fields = ["Имя", "Номер телефона"]
    os.system('cls')
    title.title()
    print("Контакты:".center(10))
    print("---------".center(10))
    print("")
    count = 0
    with open("contacts.csv", 'r') as file:
        read = csv.reader(file)
        for i in read:
            if len(i) > 0:
                count = count + 1
        print("Всего контактов: ", count)
        print("")

    with open("contacts.csv", 'r') as file:
        read = csv.reader(file)
        if os.path.getsize("contacts.csv") == 0:
            print("Телефонный справочник пуст. Пожалуйста, заполните его".center(129))
        else:
            for i in contact_fields:
                print('{0:<10}'.format(i).center(10), end="\t\t")
            print('{:<10}\t\t{:<10}'.format('', ''))
            print("")

            for data in read:

                for item in data:
                    print('{:<10}'.format(item).center(10), end="\t\t")
                print("")
    print("\n")
    input("\t Нажми enter для продолжения..".center(120))
    os.system('cls')


def search():
    contact_fields = ["Имя", "Номер телефона"]
    os.system('cls')
    title.title()
    print("Поиск контактов:".center(10))
    print("----------------".center(10))
    print("")
    contact_match = 'false'
    search_value = input("Введи имя: ")
    print("")
    for i in contact_fields:
        print('{0:<10}'.format(i).center(10), end="\t\t")
    print('{:<10}\t\t{:<10}'.format('', '').center(10))
    print("")
    with open("contacts.csv", 'r') as file:
        read = csv.reader(file)
        for data in read:
            if len(data) > 0:
                if search_value == data[0]:
                    contact_match = 'true'
                    print('{:<10}\t\t{:<10}'.format(data[0], data[1]).center(10))
    if contact_match == 'false':
        print("")
        print("Нет контакта с таким именем".center(129))
    print("")

def delete():
    os.system('cls')
    title.title()
    print("")
    print("Удалить контакт:")
    print("----------------")
    print("")

    person_match = 'false'
    update_contact = input("Введи имя: ")
    update_list = []
    with open("contacts.csv", 'r') as file:
        read = csv.reader(file)
        for data in read:
            if len(data) > 0:
                if update_contact != data[0]:
                    update_list.append(data)
                else:
                    person_match = 'true'

        if person_match == 'true':
            with open("contacts.csv", 'w') as f:
                write = csv.writer(f)
                write.writerows(update_list)
                print("")
                print("Контакт успешно удален!".center(129))
                print("")
    if person_match == 'false':
        print("")
        print("Извините! Данные не обнаружены")
        print("")

