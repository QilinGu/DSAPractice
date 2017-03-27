# My advise is to spend 20 mins on the
# problem with no coding, since it is easy to not get the requirements.
# I made this mistake and I paid the price. (Lesson learned)

class Solution(object):
    def __init__(self):
        self.insider_trades = set()
        self.trades = {}
        self.current_price = None

    def findFraudolentTraders(self, datafeed):
        for feed in datafeed:
            vals = feed.split("|")
            day = int(vals[0])
            if len(vals) == 2:
                self.checkTrades(vals, day)
            else:
                self.saveTradeRecord(vals, day)

        insider_trades = sorted(list(self.insider_trades))
        return [ str(x[0]) + "|" + str(x[1]) for x in insider_trades ]

    def checkTrades(self, vals, day):
        self.current_price = int(vals[1])
        for x in range(day - 3, day):
            if x in self.trades:
                for (trader_name, isBuy, price, amount) in self.trades[x]:
                    if (x, trader_name) in self.insider_trades:
                        continue
                    if isBuy:
                        fraudolent = (self.current_price - price) * amount >= 5000000
                    else:
                        fraudolent = (price - self.current_price) * amount >= 5000000
                    if fraudolent:
                        self.insider_trades.add((x, trader_name))

    def saveTradeRecord(self, vals, day):
        trader_name = vals[1]
        isBuy = len(vals[2]) == 3
        amount = int(vals[3])
        record = (trader_name, isBuy, self.current_price, amount)
        self.trades[day] = self.trades.get(day, []) + [record]



#Testing
 
feed1 = """0|1000
0|Shilpa|BUY|30000
0|Will|BUY|50000
0|Tom|BUY|40000
0|Kristi|BUY|15000
1|Kristi|BUY|11000
1|Tom|BUY|1000
1|Will|BUY|19000
1|Shilpa|BUY|25000
2|1500
2|Will|SELL|7000
2|Shilpa|SELL|8000
2|Kristi|SELL|6000
2|Tom|SELL|9000
3|500
38|1000
78|Shilpa|BUY|30000
79|Kristi|BUY|60000
80|1100
81|1200"""
 
datafeed1 = feed1.split("\n")
 
print Solution().findFraudolentTraders(datafeed1)
 
feed2 = """0|20
0|Kristi|SELL|3000
0|Will|BUY|5000
0|Tom|BUY|50000
0|Shilpa|BUY|1500
1|Tom|BUY|1500000
3|25
5|Shilpa|SELL|1500
8|Kristi|SELL|600000
9|Shilpa|BUY|500
10|15
11|5
14|Will|BUY|100000
15|Will|BUY|100000
16|Will|BUY|100000
17|25"""
 
datafeed2 = feed2.split("\n")
 
print Solution().findFraudolentTraders(datafeed2)