import os
import mysql.connector
from datetime import datetime


# Создание и работа с файлами
def create_and_manage_files():
    # Создаём файлы
    with open("domestic_animals.txt", "w") as file:
        file.write("Собака\nКошка\nХомяк\n")
    with open("pack_animals.txt", "w") as file:
        file.write("Лошадь\nВерблюд\nОсел\n")

    # Объединяем файлы
    with open("friends_of_human.txt", "w") as outfile:
        for fname in ["domestic_animals.txt", "pack_animals.txt"]:
            with open(fname) as infile:
                outfile.write(infile.read())

    # Переименование файла
    os.rename("friends_of_human.txt", "human_friends.txt")

    # Создаём директорию и перемещаем файл
    os.makedirs("animal_data", exist_ok=True)
    os.replace("human_friends.txt", os.path.join("animal_data",
                                                 "human_friends.txt"))


# Работа с базой данных
def setup_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        port=3307,
        password="serdserf"
    )
    cursor = connection.cursor()

    # Создаём базу данных
    cursor.execute("CREATE DATABASE IF NOT EXISTS human_friends")
    cursor.execute("USE human_friends")

    # Создаём таблицы
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS domestic_animals (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        commands TEXT,
        birth_date DATE
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pack_animals (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        commands TEXT,
        birth_date DATE
    )
    """)

    connection.commit()
    connection.close()


# Основной класс Animal и наследование
class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        self.commands = []

    def teach_command(self, command):
        if command not in self.commands:
            self.commands.append(command)

    def list_commands(self):
        return self.commands if self.commands else ["Нет обученных команд"]

    def __str__(self):
        return f"{self.name} (Родился: {self.birth_date.date()}, Команды:\
        {', '.join(self.commands)})"


class DomesticAnimal(Animal):
    pass


class PackAnimal(Animal):
    pass


# Реализация интерфейса программы
def main_menu():
    animals = []

    while True:
        print("\nМеню:")
        print("1. Завести новое животное")
        print("2. Показать список животных")
        print("3. Обучить животное команде")
        print("4. Показать команды животного")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите имя животного: ")
            birth_date = input("Введите дату рождения (YYYY-MM-DD): ")
            category = input("Категория (1 - Домашнее, 2 - Вьючное): ")

            if category == "1":
                animals.append(DomesticAnimal(name, birth_date))
            elif category == "2":
                animals.append(PackAnimal(name, birth_date))
            else:
                print("Неверная категория!")

        elif choice == "2":
            for animal in animals:
                print(animal)

        elif choice == "3":
            name = input("Введите имя животного: ")
            command = input("Введите команду: ")

            for animal in animals:
                if animal.name == name:
                    animal.teach_command(command)
                    print("Команда добавлена!")
                    break
            else:
                print("Животное не найдено!")

        elif choice == "4":
            name = input("Введите имя животного: ")

            for animal in animals:
                if animal.name == name:
                    print(f"Команды животного {name}:\
                          {', '.join(animal.list_commands())}")
                    break
            else:
                print("Животное не найдено!")

        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    create_and_manage_files()
    setup_database()
    main_menu()
