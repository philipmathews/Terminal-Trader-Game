import sqlite3
connection = sqlite3.connect('stock.db')
cursor = connection.cursor()
cursor.execute('DROP TABLE Users')
cursor.execute('DROP TABLE Stocks')
query = 'CREATE TABLE Users(Username Varchar, Password Varchar,  Name Varchar, amount_available integer);'
cursor.execute(query)
query = 'CREATE TABLE Stocks(StockName varchar, StockSymbol varchar, Price integer, Quantity integer, Username Varchar, FOREIGN KEY(Username) REFERENCES Users(Username));'
cursor.execute(query)
connection.commit()
connection.close