import title
import operations
import os

def choosing():
    while True:
        print("1. Посмотреть контакты".center(133))
        print("2. Создать контакт".center(129))
        print("3. Поиск".center(120))
        print("4. Удалить контакт".center(129))
        print("5. Выход".center(120))
        print("_______________________".center(131))
        option = int(input("\t\t\t\t\t\t\tВыбери опцию: "))

        if option == 1:
            operations.view()
            title.title()

        if option == 2:
            while True:
                operations.create()
                ans = input("\t\t\t\t\tХочешь создать еще один контакт?[Д/Н]: ")
                if ans == 'Д' or ans == 'д':
                    continue
                else:
                    break
            os.system('cls')
            title.title()

        if option == 3:
            while True:
                operations.search()
                print("")
                ans = input("\t\t\t\t\tПоиск еще одного контакта?[Д/Н]: ")
                if ans == 'Д' or ans == 'д':
                    continue
                else:
                    break
            os.system('cls')
            title.title()

        if option == 4:
            while True:
                operations.delete()
                ans = input("\t\t\t\t\tУдалить еще один контакт?[Д/Н]: ")
                if ans == 'Д' or ans == 'д':
                    continue
                else:
                    break
            os.system('cls')
            title.title()

        if option == 5:
            os.system('cls')
            line_1 = "------------------------------------------"
            Tq = "   Хорошего дня!"
            line_2 = "------------------------------------------"
            print(line_1.center(130))
            print(Tq.center(130))
            print(line_2.center(130))
            break

        if option > 5 or option < 1:
            os.system('cls')
            print("Неверный выбор. Попробуй что-то из предложенных вариантов".center(129))
            print("\n")
            input("Нажми enter для продолжения...".center(130))
            os.system('cls')
            title.title()