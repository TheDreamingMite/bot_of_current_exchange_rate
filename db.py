import sqlite3

def start_bd(nam):
    #nam = "Vova"
    commis = '0.05'

    conn = sqlite3.connect('data_base2.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), commission varchar(10))')
    conn.commit()

    cur.execute("INSERT INTO users (name, commission) VALUES ('%s', '%s')" % (nam, commis))
    conn.commit()

    cur.close()
    conn.close()
    print('пользователь зарегистрирован!')
    return 'Пользователь зарегистрирован!'

def all_usres():
    conn = sqlite3.connect('data_base2.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Имя: {el[1]}, комиссия: {el[2]}\n'

    cur.close()
    conn.close()

    print('Пользователи отправлены!')

    return info
def change_data(name, commission):
    conn = sqlite3.connect('data_base2.sql')
    cur = conn.cursor()

    cur.execute("DELETE FROM users WHERE name = '%s'"%(name))
    cur.execute("INSERT INTO users (name, commission) VALUES ('%s', '%s')" % (name, commission))
    conn.commit()

    cur.close()
    conn.close()

    print('Данные пользователя изменены')

