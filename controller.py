from wrapper import Markit
from model import *
import time
import operator
from prettytable import PrettyTable

class controller:
    
    def __init__(self):
        self.m=Markit()
        self.l=model()
    
    def get_tickersymbol(self,string):
        c= self.m.company_search(string)
        q= c[0]['Symbol']
        return q
    
    def get_marketdata(self,string):
        m=self.m.get_quote(string)
        return m
    
    def new_account(self,string1,string2,string3):
        name= string1
        user_name = string2
        password = string3
        self.l.add_user(name,user_name,password)
        
    def check_account(self,str1,str2):
        chk=self.l.check_user(str1,str2)
        return chk

    def buy(self,a,q,usr,sy):
        total_price= a['LastPrice'] * q
        now=self.l.see_earning(usr)
        if total_price < now[0]:
            ch=self.l.see_quant(usr,sy)
            if(ch==None):
                self.l.add_stock(a,usr,q)
                balance=now[0] - total_price
                self.l.balance_update(balance,usr)
            else:
                nq=q+ch[0]
                balance=now[0] - total_price
                self.l.balance_update(balance,usr)
                self.l.quant_update(nq,usr,sy)
            
            print("\n...The Transaction was Successfull...")
            print("Balance:",balance)
        else:
            print("\nYou dont have enough fund to buy")
    
    def sell(self,dt,quant,usr_n,sn):
        wr=self.l.check_stock(usr_n,sn)
        if(wr!=None):
            g_price=dt['LastPrice'] * quant
            rnow=self.l.see_earning(usr_n)
            n_price=g_price + rnow[0]
            self.l.balance_update(n_price,usr_n)
            rq=self.l.see_quant(usr_n,sn)
            lq=rq[0] - quant
            if(lq==0):
                self.l.remove_stock(usr_n,sn)
                print("\n.....The Transaction was Sucessfull.....")
                print("Balance:",n_price)
            elif(lq<0):
                print("\nYou dont have this much quantity to sell")
            else:
                self.l.quant_update(lq,usr_n,sn)
                print("\n.....The Transaction was Sucessfull.....")
                print("Balance:",n_price)

        else:
            print("\nThis company is not in your list")

    def portfolio(self,n):
        b=self.l.see_stock(n)
        print("\nStocks:" ,b)
        k=self.l.see_earning(n)
        print("Earnings:",k[0])

    def admin_leader(self):
        sl=[]
        pm=[]
        rp=[]
        ew=[]
        tr=[]
        net_w=[]
        rt=[]
        fd=[]
        di={}
        ut=self.l.leaderboard()
        for i in ut:
            sl.append(i[0])
        for k in sl:
            try:
                uy=self.l.only_user(k)
                tr.append(uy[0])
            except TypeError:
                pass
        for i in tr:
            eh=self.l.only_quant(i)
            for d in eh:
                pm.append(d[0])
        for t in tr:
            ej=self.l.only_symbol(t)
            for o in ej:
                rp.append(o[0])
        for r in range(len(pm)):
            quan=pm[r]
            symbol=rp[r]
            bv=self.l.get_usr(quan,symbol)
            fd.append(bv[0])
            gt=self.l.see_earning(bv[0])
            time.sleep(3)
            pl=self.m.get_quote(symbol)
            time.sleep(3)
            stock_value=pl['LastPrice'] * quan
            net_worth=gt[0] + stock_value
            net_w.append(net_worth)
        
        qa=zip(fd,net_w)
        rt=list(qa)
        for each in rt:
            if each[0] in di:
                di[each[0]]= di[each[0]] + each[1]
            else:
                di[each[0]] = each[1]
        sorted_x = sorted(di.items(), key=operator.itemgetter(1),reverse=True)
        print("\n.........LeaderBoard............\n")
        t=PrettyTable(("Username","Earnings"))
        for o in sorted_x:
            t.add_row(o)
        print(t)

    def user_valid(self,op):
        qr=self.l.username_check(op)
        return qr