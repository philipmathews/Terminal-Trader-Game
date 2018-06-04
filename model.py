import sqlite3
from wrapper import Markit

connection= sqlite3.connect('stock.db')
cursor= connection.cursor()

class model:
    def __init__(self):
        self.n=Markit()

    def add_user(self,nam, user,passw):
        cursor.execute("INSERT INTO Users(Username, Password, Name, amount_available) VALUES(?,?,?,?)", (user,passw,nam,100000))
        connection.commit()
    
    def check_user(self,usr,pa):
        cursor.execute("SELECT Username FROM Users WHERE Username=(?) AND Password=(?)", (usr,pa))
        f=cursor.fetchone()
        return f
    
    def add_stock(self,st_d,name,qn):
        cursor.execute("INSERT INTO Stocks(StockName, StockSymbol, Price, Quantity, Username) VALUES(?,?,?,?,?)", (st_d['Name'],st_d['Symbol'],st_d['LastPrice'],qn,name))
        connection.commit()

    def check_stock(self,u_name,c_n):
        cursor.execute("SELECT StockName FROM Stocks WHERE Username=(?) AND StockSymbol=(?)", (u_name,c_n))
        i=cursor.fetchone()
        return i

    def see_stock(self,n_):
        cursor.execute("SELECT StockName,StockSymbol,Price,Quantity FROM Stocks WHERE Username=(?)", (n_,))
        g=cursor.fetchall()
        return g
    
    def see_earning(self,nm):
        cursor.execute("SELECT amount_available FROM Users WHERE Username=(?)", (nm,))
        h=cursor.fetchone()
        return h

    def see_quant(self,u,s):
        cursor.execute("SELECT quantity FROM Stocks Where Username=(?) AND StockSymbol=(?)", (u,s))
        j=cursor.fetchone()
        return j
    
    def balance_update(self,un,bal):
        cursor.execute("UPDATE Users SET amount_available=(?) WHERE Username=(?)", (un,bal))
        connection.commit()

    def quant_update(self,qt,ui,s_y):
        cursor.execute("UPDATE Stocks SET quantity=(?) WHERE Username=(?) AND StockSymbol=(?)", (qt,ui,s_y))
        connection.commit()
    
    def remove_stock(self,uy,sy):
        cursor.execute("DELETE FROM Stocks WHERE Username=(?) AND StockSymbol=(?)", (uy,sy))
        connection.commit()
    
    def leaderboard(self):
        cursor.execute("SELECT Username FROM Users WHERE Username != 'admin'")
        e=cursor.fetchall()
        return e
    
    def username_check(self,li):
        cursor.execute("SELECT Username FROM Users Where Username=(?)", (li,))
        d=cursor.fetchone()
        return d

    def getfull_stock(self):
        cursor.execute("SELECT StockSymbol,Quantity,Username FROM Stocks")
        c=cursor.fetchall()
        return c
    
    def only_quant(self,ko):
        cursor.execute("SELECT Quantity From Stocks WHERE Username=(?)", (ko,))
        b=cursor.fetchall()
        return b
    
    def only_symbol(self,kp):
        cursor.execute("SELECT StockSymbol FROM Stocks WHERE Username=(?)", (kp,))
        a=cursor.fetchall()
        return a
    
    def only_amount(self,x):
        cursor.execute("SELECT amount_available FROM Users WHERE Username=(?)", (x,))
        w=cursor.fetchone()
        return w

    def only_user(self,fg):
        cursor.execute("SELECT Username FROM Users WHERE Username=(?) AND amount_available != '100000'", (fg,))
        y=cursor.fetchone()
        return y
    
    def get_usr(self,q,s):
        cursor.execute("SELECT Username FROM Stocks WHERE Quantity=(?) AND StockSymbol=(?)", (q,s))
        z=cursor.fetchone()
        return z
