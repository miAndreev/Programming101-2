class CashDesk(object):
    """self.money = {100:0, 50:0, 20:0, 10:, 5:0, 2:0, 1:0}"""
    i_list = [100, 50, 20, 10, 5, 2, 1]
    def __init__(self):
        
        self.money = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}


       # for m in self.money.items():

    def take_money(self, money):
        for v_m_pair in money.items():
            if v_m_pair[1] != 0:
                self.money[v_m_pair[0]] = self.money[v_m_pair[0]] + v_m_pair[1]
        #print(self.money)


    def total(self):
        summ = 0
        for money_pair in self.money.items():
            print(money_pair)
            summ = summ + money_pair[0]*money_pair[1]

        return summ

    def can_withdraw_money(self, money_to_withdraw):
        rest = money_to_withdraw
        i_list = [100, 50, 20, 10, 5, 2, 1]
        for i in i_list:
            amount = self.money[i]
            if amount > 0 and rest >= i:    
                while amount > 0:
                    rest = rest - i
                    amount = amount - i
                    
        if rest > 0 :
            return False
        else:
            return True

        
        
if __name__ == '__main__':
    my_cash_desk = CashDesk()
    my_cash_desk.take_money({1:2, 50:1, 20:1})
    print(my_cash_desk.total()) # 72
    print(my_cash_desk.can_withdraw_money(30)) #False
    print(my_cash_desk.can_withdraw_money(70)) #True