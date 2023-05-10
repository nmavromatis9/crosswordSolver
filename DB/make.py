import sqlite3

def main():
    print("hello world")
    try:
        conn = sqlite3.connect('login.db')
        cur=conn.cursor()
    except:
        print("cannot create")

    try:
        s=""" CREATE TABLE IF NOT EXISTS users(email varchar, password varchar);"""
        cur.execute(s)
        conn.commit()
    except:
        print("error")
    
    S2=""" INSERT INTO users VALUES('test1', 'pwd');"""
    
    cur.execute(S2)
    conn.commit()
    return

if __name__ == '__main__':
    main()
