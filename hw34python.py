
#Задача1
#
# books = ['Оружейный остров (Амитав Гош)','Уничтожить (Мишель Уэльбек)','Буря мечей (Джордж Мартин)','Ася (Иван Тургенев)','Долина ужаса (Дойл Артур Конан)']
# years = ['Год издания 2022','Год издания 2023','Год издания 2008','Год издания 1858','Год издания 1915']
#
# def add_book():
#     name_book = input("Введите название книги: ")
#     year = input("Введите год выпуска: ")
#     books.append(name_book)
#     years.append(year)
#
# def sorter_name_book():
#
#     sorted_books = sorted(books)
#     print("Список книг, отсортированный по названию:")
#     for book in sorted_books:
#         index = books.index(book)
#         year = years[index]
#         print(f"{book} - {year}")
#
# def sorter_year():
#     sorted_years = sorted(years)
#     print("Список книг, отсортированный по годам выпуска:")
#     for year in sorted_years:
#         index = years.index(year)
#         book = books[index]
#         print(f"{book} - {year}")
#
# def spisok_books():
#     print("Список книг с названиями и годами выпуска:")
#     for i in range(len(books)):
#         print(f"{books[i]} - {years[i]}")
#
# while True:
#     print("Меню:")
#     print("1. Добавить книгу")
#     print("2. Отсортировать по названию книг")
#     print("3. Отсортировать по годам выпуска")
#     print("4. Вывести список книг с названиями и годами выпуска")
#     print("5. Выход")
#
#     choice = input("Выберите пункт меню: ")
#
#     if choice == "1":
#         add_book()
#     elif choice == "2":
#         sorter_name_book()
#     elif choice == "3":
#         sorter_year()
#     elif choice == "4":
#         spisok_books()
#     elif choice == "5":
#         break
#     else:
#         print("ОШИБКА. Пожалуйста, выберите пункт из меню.")

#Задача2

basketball_players = {}
basketball_players["Майкл Джордан"] = {"Рост": "198 см", "Клуб": "Чикаго Буллс"}
basketball_players["Леброн Джеймс"] = {"Рост": "206 см", "Клуб": "Лос-Анджелес Лейкерс"}
basketball_players["Кобе Брайант"] = {"Рост": "198 см", "Клуб": "Лос-Анджелес Лейкерс"}

def add_player():
    name = input("Введите ФИО баскетболиста: ")
    height = input("Введите рост баскетболиста: ")
    club = input("Введите клуб, за который играл баскетболист: ")
    basketball_players[name] = {"Рост": height, "Клуб": club}
    print("Информация о баскетболисте успешно добавлена.")

def delete_player():
    name = input("Введите ФИО баскетболиста для удаления: ")
    if name in basketball_players:
        del basketball_players[name]
        print("Информация о баскетболисте успешно удалена.")
    else:
        print("Баскетболист не найден.")

def search_player():
    name = input("Введите ФИО баскетболиста для поиска: ")
    if name in basketball_players:
        player_info = basketball_players[name]
        print("Информация о баскетболисте:")
        print(f"ФИО: {name}")
        print(f"Рост: {player_info['Рост']}")
        print(f"Клуб: {player_info['Клуб']}")
    else:
        print("Баскетболист не найден.")

def update_player():
    name = input("Введите ФИО баскетболиста для обновления данных: ")
    if name in basketball_players:
        height = input("Введите новый рост баскетболиста: ")
        club = input("Введите новый клуб, за который играл баскетболист: ")
        basketball_players[name]["Рост"] = height
        basketball_players[name]["Клуб"] = club
        print("Данные баскетболиста успешно обновлены.")
    else:
        print("Баскетболист не найден.")

def view_players():
    if basketball_players:
        print("Список баскетболистов:")
        for name, player_info in basketball_players.items():
            print(">>>>>>>>>>>>>>>")
            print(f"ФИО: {name}")
            print(f"Рост: {player_info['Рост']}")
            print(f"Клуб: {player_info['Клуб']}")
            print("<<<<<<<<<<<<<<<")
    else:
        print("Список баскетболистов пуст.")

while True:
    print("Меню:")
    print("1. Добавить баскетболиста")
    print("2. Удалить баскетболиста")
    print("3. Найти баскетболиста")
    print("4. Обновить данные баскетболиста")
    print("5. Просмотреть всех баскетболистов")
    print("6. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        add_player()
    elif choice == "2":
        delete_player()
    elif choice == "3":
        search_player()
    elif choice == "4":
        update_player()
    elif choice == "5":
        view_players()
    elif choice == "6":
        break
    else:
        print("Некорректный ввод. Пожалуйста, выберите пункт из меню.")
