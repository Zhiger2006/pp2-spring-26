import psycopg2

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

def show():
    cur.execute("SELECT * FROM phonebook")
    for row in cur.fetchall():
        print(row)

def delete():
    name = input("Кого удалить: ")
    cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))
    conn.commit()

while True:
    print("\n1 Добавить\n2 Показать\n3 Удалить\n4 Выход")
    c = input("Выбор: ")

    if c == "1":
        add()
    elif c == "2":
        show()
    elif c == "3":
        delete()
    elif c == "4":
        break

cur.close()
conn.close()