# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной 
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

import os

def create_phonebook(filename="phonebook.txt"):
    """Создает телефонный справочник."""

    if not os.path.exists(filename):
        with open(filename, "w", encoding='utf-8') as f:
            f.write("Фамилия, Имя, Отчество, Телефон\n")

def add_entry(filename="phonebook.txt"):
    """Добавляет новую запись в телефонный справочник."""

    with open(filename, "a", encoding='utf-8') as f:
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        middle_name = input("Введите отчество: ")
        phone_number = input("Введите номер телефона: ")
        f.write(f"{last_name}, {first_name}, {middle_name}, {phone_number}\n")
        print("Запись добавлена.")

def view_entries(filename="phonebook.txt"):
    """Отображает все записи телефонного справочника."""

    with open(filename, "r", encoding='utf-8') as f:
        for line in f:
            print(line.strip())

def search_entry(filename="phonebook.txt"):
    """Ищет запись по заданному критерию."""

    search_term = input("Введите имя или фамилию для поиска: ")
    with open(filename, "r",encoding='utf-8') as f:
        for line in f:
            if search_term.lower() in line.lower():
                print(line.strip())

def export_entries(filename="phonebook.txt", export_filename="phonebook_export.txt"):
    """Экспортирует записи телефонного справочника в файл."""

    with open(filename, "r", encoding='utf-8') as f, open(export_filename, "w", encoding='utf-8') as export_file:
        for line in f:
            export_file.write(line)
    print(f"Записи экспортированы в файл {export_filename}")

def import_entries(filename="phonebook.txt", import_filename="phonebook_import.txt"):
    """Импортирует записи телефонного справочника из файла."""

    with open(filename, "a",encoding='utf-8') as f, open(import_filename, "r", encoding='utf-8') as import_file:
        for line in import_file:
            f.write(line)
    print(f"Записи импортированы из файла {import_filename}")

def modify_entry(filename="phonebook.txt"):
    """Изменяет запись в телефонном справочнике."""

    search_term = input("Введите имя или фамилию для поиска: ")
    with open(filename, "r", encoding='utf-8') as f, open("temp.txt", "w", encoding='utf-8') as temp_file:
        found = False
        for line in f:
            if search_term.lower() in line.lower():
                print("Найдено:")
                print(line.strip())
                new_last_name = input("Введите новую фамилию (или нажмите Enter для сохранения): ")
                new_first_name = input("Введите новое имя (или нажмите Enter для сохранения): ")
                new_middle_name = input("Введите новое отчество (или нажмите Enter для сохранения): ")
                new_phone_number = input("Введите новый номер телефона (или нажмите Enter для сохранения): ")
                line = f"{new_last_name},{new_first_name},{new_middle_name},{new_phone_number}\n"
                found = True
            temp_file.write(line)

    if not found:
        print("Запись не найдена.")
    else:
        os.remove(filename)
        os.rename("temp.txt", filename)
        print("Запись изменена.")

def delete_entry(filename="phonebook.txt"):
    """Удаляет запись из телефонного справочника."""

    search_term = input("Введите имя или фамилию для поиска: ")
    with open(filename, "r", encoding='utf-8') as f, open("temp.txt", "w", encoding='utf-8') as temp_file:
        found = False
        for line in f:
            if search_term.lower() not in line.lower():
                temp_file.write(line)
            else:
                print("Запись удалена:")
                print(line.strip())
                found = True

    if not found:
        print("Запись не найдена.")
    else:
        os.remove(filename)
        os.rename("temp.txt", filename)
        print("Запись удалена.")

def main():
    """Основная функция программы."""

    create_phonebook()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить запись")
        print("2. Просмотреть записи")
        print("3. Поиск записи")
        print("4. Экспортировать записи")
        print("5. Импортировать записи")
        print("6. Изменить запись")
        print("7. Удалить запись")
        print("8. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entry()
        elif choice == "4":
            export_entries()
        elif choice == "5":
            import_entries()
        elif choice == "6":
            modify_entry()
        elif choice == "7":
            delete_entry()
        elif choice == "8":
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()