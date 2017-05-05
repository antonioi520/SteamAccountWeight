import steamfront
import re


class Weights(object):

    # user = client.getUser(id64='76561198014207004')
    # user1 = user.raw_apps
    #test



    def __init__(self, steamid):
        self.client = steamfront.Client('F2F002825B1A7D88A18A97579E93F936')
        self.steamid = steamid
        self.user = self.client.getUser(id64='76561198014207004')
        self.user1 = self.user.raw_apps
        self.total = 0
        self.gameCount = 0
        self.m = 0
        self.x = 0
        self.game = 0
        self.price = 0
        self.n = 0

    #def convertID64(self, steamid):
        # do later


    def getGameCount(self):
        self.m = re.findall('appid\'\: (.+?),', str(self.user1))
        self.m = list(map(int, self.m))
        self.gameCount = len(self.m)
        return self.gameCount
        print(self.gameCount + 'games')

    def getTotalPrice(self):
        self.total = 0
        for self.x in range(self.getGameCount()):
            try:
                self.game = self.client.getApp(appid=self.m[self.x])
                self.price = self.game.price_overview
                self.n = re.findall('\'final\'\: (.+?),', str(self.price))
                self.n = list(map(int, self.n))
                self.total = self.total + sum(self.n)
                self.x = self.x + 1
            except:
                pass
            continue
        return self.total
        print(self.total + 'pennies')
    # stephen was here
    # penny weight
    def getPennyWeight(self):
        pennyPerPound = 181.4368
        pennyCalculation = self.total / pennyPerPound
        #pennyCalc2 = str(round(pennyCalculation, 2))
        #return pennyCalc2
        return pennyCalculation
        print('Your account weighs ' + str(round(pennyCalculation, 2)) + ' pounds in pennies.')

    # physical weight
    def getPhysicalWeight(self):
        gameWeight = 0.3125
        weightCalculation = self.gameCount * gameWeight
        return weightCalculation
        print('Your account weighs ' + str(round(weightCalculation, 2)) + ' actual pounds.')

    def getTotalValue(self):
        self.totalValue = self.total / 100
        return self.totalValue
        print('The total value of your account is $' + str(self.totalValue))

    def getAveragePrice(self):
        pricePerGame = self.totalValue / self.gameCount
        str(round(pricePerGame, 2))
        return pricePerGame
        print('Average price per game is $' + str(pricePerGame)[:5])