import sqlite3

def start_bd(nam):
    comis = 0.05

    conn = sqlite3.connect('data_base.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), comission varchar(10)')
    conn.commit()

    cur.execute("INSERT INTO users (name, comission) VALUES ('%s', '%s')" % (nam, comis))
    conn.commit()

    cur.close()
    conn.close()
    print('пользователь зарегистрирован!')
