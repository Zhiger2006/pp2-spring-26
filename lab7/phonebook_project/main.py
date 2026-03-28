import psycopg2
import csv  


conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="12345678",  
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def add():
    name = input("Имя: ")
    phone = input("Телефон: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Контакт успешно добавлен.")

def show():
    cur.execute("SELECT * FROM phonebook")
    for row in cur.fetchall():
        print(row)

def delete():
    
    target = input("Введите имя или телефон для удаления: ")
    cur.execute("DELETE FROM phonebook WHERE name=%s OR phone=%s", (target, target))
    conn.commit()
    print("Контакт удален.")


def upload_from_csv():
    file_name = input("Введите название файла (например, data.csv): ")
    try:
        with open(file_name, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 2: continue
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
        conn.commit()
        print("Данные из CSV импортированы.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        conn.rollback() 


def update_contact():
    name = input("Имя контакта, который нужно изменить: ")
    new_phone = input("Новый номер телефона: ")
    cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (new_phone, name))
    conn.commit()
    print("Данные обновлены.")


def search_contact():
    query = input("Введите имя или часть номера для поиска: ")
    cur.execute("SELECT * FROM phonebook WHERE name LIKE %s OR phone LIKE %s", (f'%{query}%', f'{query}%'))
    results = cur.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("Ничего не найдено.")


while True:
    print("\n1 Добавить\n2 Показать\n3 Удалить\n4 Загрузить из CSV\n5 Обновить телефон\n6 Поиск\n7 Выход")
    c = input("Выбор: ")

    if c == "1":
        add()
    elif c == "2":
        show()
    elif c == "3":
        delete()
    elif c == "4":
        upload_from_csv()
    elif c == "5":
        update_contact()
    elif c == "6":
        search_contact()
    elif c == "7":
        break

cur.close()
conn.close()