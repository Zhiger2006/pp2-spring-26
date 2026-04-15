import csv
from connect import get_connection


def add():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
    conn.commit()

    print("Contact added or updated.")

    cur.close()
    conn.close()


def show():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete():
    conn = get_connection()
    cur = conn.cursor()

    target = input("Enter name or phone to delete: ")
    cur.execute("CALL delete_contact(%s);", (target,))
    conn.commit()

    print("Contact deleted.")

    cur.close()
    conn.close()


def upload_from_csv():
    conn = get_connection()
    cur = conn.cursor()

    file_name = input("Enter CSV file name: ")

    try:
        with open(file_name, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 2:
                    continue
                cur.execute("CALL upsert_contact(%s, %s);", (row[0], row[1]))

        conn.commit()
        print("CSV data imported.")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    cur.close()
    conn.close()


def update_contact():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Enter contact name to update: ")
    new_phone = input("Enter new phone: ")

    cur.execute("CALL upsert_contact(%s, %s);", (name, new_phone))
    conn.commit()

    print("Contact updated.")

    cur.close()
    conn.close()


def search_contact():
    conn = get_connection()
    cur = conn.cursor()

    query = input("Enter name or phone part to search: ")
    cur.execute("SELECT * FROM search_contacts(%s);", (query,))
    results = cur.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print("Nothing found.")

    cur.close()
    conn.close()


def show_paginated():
    conn = get_connection()
    cur = conn.cursor()

    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
    results = cur.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print("No records.")

    cur.close()
    conn.close()


def insert_many():
    conn = get_connection()
    cur = conn.cursor()

    names = ["Zhuman", "Alisher", "Damir"]
    phones = ["87071112233", "87475556677", "87019990011"]

    cur.execute("CALL insert_many_contacts(%s, %s);", (names, phones))
    conn.commit()

    print("Many contacts inserted.")

    cur.close()
    conn.close()


while True:
    print("\n1 Add contact")
    print("2 Show all contacts")
    print("3 Delete contact")
    print("4 Upload from CSV")
    print("5 Update contact")
    print("6 Search contact")
    print("7 Show paginated")
    print("8 Insert many contacts")
    print("9 Exit")

    c = input("Choose: ")

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
        show_paginated()
    elif c == "8":
        insert_many()
    elif c == "9":
        break