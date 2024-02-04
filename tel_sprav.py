def read_sprav():
    sprav = []
    path = 'tel_sprav.txt'
    tel_sprav = open(path, 'r', encoding='utf-8')

    # content = tel_sprav.read()   # Вариант-2
    # print(content)
    # print(type(content))
    for line in tel_sprav:
        n = line.split()
        # print (n)
        dict_ = {
            "last_name": n[0],
            "first_name": n[1],
            "second_name": n[2],            
            "tel": n[3],
        }
        # print(dict)
        sprav.append(dict_)
        # print(sprav)

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
        # print(*(f"{k}: {v}" for k, v in item.items()))
        # print(*(f"обычный текст до {v} и после" for v in item.values()))
        # print(item['last_name'], item['first_name'], item['second_name'], item['tel'])

    return None


def add_contact(tel_spra_ls):
    tel_sprav = open('tel_sprav.txt', 'a', encoding='utf-8')
    s = input("Введите ФИО, тел, резделенные пробелами: ")
    ls_s = s.split() # Делаю список, чтобы к каждому слову присенить / capitalize() /
    print(ls_s)
    for i in range(len(ls_s)):
        ls_s[i] = ls_s[i].capitalize()
        tel_sprav.write(f'{ls_s[i]} ')
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
    return tel_sprav


def find_last_name(last_name: str, my_sprav):
    for item in my_sprav:
        if item["last_name"] == last_name.capitalize():
            print(item)


def main():
    # переменная = open ('название файла', 'режим работы', encoding='кодировка')
    while True:
        print("Что хотите сделать?")
        print("1: Вывести данные")
        print("2: Записать новый контакт")
        print("3: Найти контакт по фамилии")
        print("0: Выйти")

        x = input()
        tel_sprav = read_sprav()
        if x == "1":
            print_sprav(tel_sprav)
        elif x == "2":
            add_contact(tel_sprav)
        elif x == "3":
            find_last_name(input("Введите фамилию: "), my_sprav=tel_sprav)
        elif x == "0":
            break
        else:
            print("неверная команда")


if __name__ == "__main__":
    main()