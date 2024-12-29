# Я не имел возможности реализовать код на операционной системе Linux, поэтому реализовал программу на Windows с использованием MySQL Command Line Client.
# Описание проекта

Этот проект представляет собой систему учёта для питомника, в котором живут домашние и вьючные животные. Программа реализована на Python и включает работу с файлами, базой данных MySQL и объектно-ориентированное программирование.

## Структура проекта

- `animal_registry.py`: Основной файл проекта, содержащий реализацию логики программы.
- `domestic_animals.txt`: Файл с данными о домашних животных (создаётся программой).
- `pack_animals.txt`: Файл с данными о вьючных животных (создаётся программой).
- `animal_data/human_friends.txt`: Объединённый файл с информацией о всех животных (создаётся и перемещается программой).
- `README.md`: Описание структуры проекта и команды для работы с MySQL.

## Основные функции программы

1. **Создание и управление файлами:**
   - Создаёт текстовые файлы для домашних и вьючных животных.
   - Объединяет их содержимое в один файл и перемещает в директорию `animal_data`.

2. **Работа с базой данных MySQL:**
   - Создаёт базу данных `human_friends`.
   - Создаёт таблицы для хранения данных о домашних и вьючных животных.

3. **Операции с животными:**
   - Добавление нового животного в реестр.
   - Обучение животных новым командам.
   - Просмотр списка животных.
   - Просмотр списка команд, которые знает животное.

4. **Меню:**
   - Интерактивное меню для работы с системой учёта.

## Настройка MySQL

Для работы программы необходимо настроить MySQL и выполнить следующие команды в MySQL Command Line Client:

### Подключение к MySQL
```bash
mysql -u root -p
```

### Создание базы данных
```sql
CREATE DATABASE IF NOT EXISTS human_friends;
USE human_friends;
```

### Создание таблиц
```sql
CREATE TABLE IF NOT EXISTS domestic_animals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    commands TEXT,
    birth_date DATE
);

CREATE TABLE IF NOT EXISTS pack_animals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    commands TEXT,
    birth_date DATE
);
```

## Запуск программы

1. Убедитесь, что MySQL сервер запущен и доступен на порту `3307` (именно этот порт я использовал при работе над проектом).
2. Установите зависимости:
   ```bash
   pip install mysql-connector-python
   ```
3. Запустите программу:
   ```bash
   python animal_registry.py
   ```

## Примечания

- Убедитесь, что настройки подключения в `animal_registry.py` соответствуют вашим учетным данным MySQL (параметры `host`, `user`, `password`,`port`).
- Для корректной работы программы рекомендуется Python версии 3.7 или выше.

