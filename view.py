from wrapper import Markit
from controller import *
import getpass

class view:
    
    def __init__(self):
        self.c=controller()
    
    def user_interface(self):
        while True:
            try:
                c=int(input("\n........welcome to Terminal Trader game.........\n (choose the option) \n 1.Search the companies and get exact ticker symbol\n 2.Retrieve market data for a stock\n 3.Create an account with username and password\n 4.Login\n 5.exit\n Enter: "))
                if (c==1):
                    qw=self.c.get_tickersymbol(input("\nEnter the name of the company: "))
                    print("\nStock Symbol:",qw)
                if(c==2):
                    ew=self.c.get_marketdata(input("\nEnter the Stock symbol: "))
                    print("\n.....Market Data.....\n")
                    print("Name:",ew['Name'])
                    print("Symbol:",ew['Symbol'])
                    print("LastPrice:",ew['LastPrice'])
                if(c==3):
                    u=input("\nEnter Name:")
                    i=input("Enter username: ")
                    ed=self.c.user_valid(i)
                    if(ed == None):
                        r=getpass.getpass("Enter password:")
                        self.c.new_account(u,i,r)
                        print("\n.....Account Created.......")
                    else:
                        print("\n!!!!This username is already taken.Try again!!!")
                        continue
                if(c==4):
                    io=input("\nEnter username: ")
                    ou=getpass.getpass("Enter password: ")
                    w=self.c.check_account(io,ou)
                    try:
                        if(w[0]!="admin"):
                            print("\nYou have succesfully Logged in")
                            while True:
                                usr_i=input("\n(choose the option:)\n 1.Buy stock\n 2.Sell Stock\n 3.View the portfolio\n 4.Search the companies and get exact ticker symbol\n 5.Retrieve market data for a stock\n 6.Log Out\n Enter: ")
                                if(usr_i=='1'):
                                    t=input("\nEnter the company name you want to buy: ")
                                    q=int(input("enter the quantity: "))
                                    b=self.c.get_tickersymbol(t)
                                    a=self.c.get_marketdata(b)
                                    self.c.buy(a,q,io,b)
                                if(usr_i=='2'):
                                    en=input("\nEnter the company name you want to sell: ")
                                    rt=int(input("Enter the quantity: "))
                                    e=self.c.get_tickersymbol(en)
                                    p=self.c.get_marketdata(e)
                                    self.c.sell(p,rt,io,e)
                                if(usr_i=='3'):
                                    self.c.portfolio(io)
                                if(usr_i=='4'):
                                    ty=self.c.get_tickersymbol(input("\nEnter the name of the company: "))
                                    print("\nStock Symbol:",ty)
                                if(usr_i=='5'):
                                    yt=self.c.get_marketdata(input("\nEnter the Stock symbol: "))
                                    print("\n.....Market Data.....\n")
                                    print("Name:",yt['Name'])
                                    print("Symbol:",yt['Symbol'])
                                    print("LastPrice:",yt['LastPrice'])
                                if(usr_i=='6'):
                                    print("\nYou have logged out")
                                    break
                                if(usr_i!='1' and usr_i!='2' and usr_i!='3' and usr_i!='4' and usr_i!='5' and usr_i!='6'):
                                    print("\n!!!!!!!That's an invalid option you chose.Try again!!!!!!!")
                                    continue
                        elif(w[0]=="admin"):
                            print("\nadmin has logged in")
                            while True:
                                py=input("\n.....choose the option........\n 1.View LeaderBoard\n 2.Logout\n Enter: ")
                                if(py=='1'):
                                    self.c.admin_leader()
                                if(py=='2'):
                                    print("\nadmin has logged out")
                                    break
                                if(py!='1' and py!='2'):
                                    print("\n!!!!!!!That's an invalid option you chose.Try again!!!!!!!")
                                    continue
                    except TypeError:
                        print("\n!!!!!!Invalid Username or password. Try again!!!!!")
                if(c==5):
                    break
                if(c!=1 and c!=2 and c!=3 and c!=4 and c!=5):
                    print("\n!!!!!!!That's an invalid option you chose.Try again!!!!!!!")
                    continue
            except ValueError:
                print("\n!!!!!!!That's an invalid option you chose.Try again!!!!!!!")
                continue

v=view()
v.user_interface()