def read_sprav():
    sprav = []
    path = 'tel_sprav.txt'
    tel_sprav = open(path, 'r', encoding='utf-8')
    for line in tel_sprav:
        n = line.split()
        # print (n)
        dict_ = {
            "last_name": n[0],
            "first_name": n[1],
            "second_name": n[2],            
            "tel": n[3],
        }
        sprav.append(dict_)

    """Альтернативный вариант"""
    # headers = ['last_name', 'first_name', 'second_name', 'tel']
    # for line in tel_sprav:
    #     line = line.strip().split()
    #     sprav.append(dict(zip(headers, line)))

    tel_sprav.close()
    return sprav


def print_sprav(tel_sprav):
    for item in tel_sprav:
         print(*(f"{v}" for v in item.values()))


    return None


def add_contact(tel_spra_ls):
    tel_sprav = open('tel_sprav.txt', 'a', encoding='utf-8')
    s = input("Введите ФИО, тел, резделенные пробелами: ")
    ls_s = s.split() # Делаю список, чтобы к каждому слову присенить / capitalize() /
    print(ls_s)
    for i in range(len(ls_s)):
        ls_s[i] = ls_s[i].capitalize()
        # tel_sprav.write(f'{ls_s[i]} ')
    tel_sprav.write('\n')

    dict_ = {
        "last_name": ls_s[0],        
        "first_name": ls_s[1],
        "second_name":ls_s[2],
        "tel": ls_s[3],
        }
    tel_spra_ls.append(dict_)
    # print (tel_spra_ls)       
    # ToDo: использовать str.capitalize()

    tel_sprav.close()
    return None


def find_last_name(last_name: str, my_sprav):
    for item in my_sprav:
        if item["last_name"] == last_name.capitalize() or item["first_name"] == last_name.capitalize() or item["second_name"] == last_name.capitalize():
            print(*(f"{v}" for v in item.values()))
    return None


def change_human (tel_spra_ls):
    print("Введите номер человека, которого хотите заменить")
    for index, item in enumerate(tel_spra_ls):
         print(*(f"{index+1} {v}" for v in item.values()))
    number = int(input())-1
    dict_ = {                                            # Попробуй разобраться почему не работает
        "last_name": input('Введите фамилию\t').capitalize(),        
        "first_name": input('Введите имя\t').capitalize(),
        "second_name":input('Введите отчество\t').capitalize(),
        "tel": input('Введите телефон\t').capitalize(),
        }

    tel_spra_ls[number] = dict_ # Заменяем значение в массиве
    print(dict_)
    print(tel_spra_ls)
    tel_sprav = open('tel_sprav.txt', 'w', encoding='utf-8')
    for item in tel_spra_ls:
        print (item)
        for val in item.values():
            # print (key, val)
            tel_sprav.writelines(f"{val}\t")
        tel_sprav.write(f" \n")
 
    tel_sprav.close()
    return None

def copy_human (tel_spra_ls):
    print("Введите номер человека, которого хотите скопировать")
    for index, item in enumerate(tel_spra_ls):
         print(*(f"{index+1} {v}" for v in item.values()))
    number = int(input())-1
    tel_sprav = open('new_tel_sprav.txt', 'a', encoding='utf-8')
    for val in tel_spra_ls[number].values():
        tel_sprav.write(f"{val}\t")
    tel_sprav.write(f" \n")
    tel_sprav.close()
    return None





def main():
    # переменная = open ('название файла', 'режим работы', encoding='кодировка')
    while True:
        print("Что хотите сделать?")
        print("1: Вывести данные")
        print("2: Записать новый контакт")
        print("3: Найти контакт по фамилии")
        print("4: Заменить контакт")
        print("5: Копировать контакт в новый справочник")
        print("0: Выйти")

        x = input()
        tel_sprav = read_sprav()
        if x == "1":
            print_sprav(tel_sprav)
        elif x == "2":
            add_contact(tel_sprav)
        elif x == "3":
            find_last_name(input("Введите фамилию: "), my_sprav=tel_sprav)
        elif x == "4":
            change_human(tel_sprav)
        elif x == "5":
            copy_human(tel_sprav)
        elif x == "0":
            break

                    
        else:
            print("неверная команда")


if __name__ == "__main__":
    main()