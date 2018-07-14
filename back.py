import sqlite3

def ping():
    #Database Connection
    conn_obj = sqlite3.connect("books.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("CREATE TABLE IF NOT EXISTS "
                    "book (id integer PRIMARY KEY, "
                            "title text, "
                            "author text, "
                            "year integer, "
                            "isbn integer)")
    conn_obj.commit()
    conn_obj.close()

def add(b_title, b_author, p_year, isbn):
    #Database Insertion
    conn_obj = sqlite3.connect("books.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("INSERT INTO book "
                    "VALUES (NULL, ?, ?, ?, ?)", (b_title, b_author, p_year, isbn))
    conn_obj.commit()
    conn_obj.close()

def seek():
    #Database Entries
    conn_obj = sqlite3.connect("books.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("SELECT * FROM book")
    rows = cur_obj.fetchall()
    conn_obj.close()
    return rows

def modify(id, b_title, b_author, p_year, isbn):
    #Database Updation
    conn_obj = sqlite3.connect("books.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("UPDATE book "
                    "SET title = ?, "
                    "author = ?, "
                    "year = ?, "
                    "isbn = ? "
                    "WHERE id = ?", 
                    (b_title, b_author, p_year, isbn, id))
    conn_obj.commit()
    conn_obj.close()

def delete(id):
    #Deletion in Database
    conn_obj = sqlite3.connect("books.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("DELETE FROM book "
                    "WHERE id = ?", (id,))
    conn_obj.commit()
    conn_obj.close()

def search(b_title = "", b_author = "", p_year = "", isbn = ""):
    #Searching in Database
    conn_obj = sqlite3.connect("books.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("SELECT * "
                    "FROM book "
                    "WHERE title = ? OR author = ? OR year = ? OR isbn = ?", 
                    (b_title, b_author, p_year, isbn))
    rows = cur_obj.fetchall()
    conn_obj.close()
    return rows
    
ping()
