import steamfront
import re

client = steamfront.Client('F2F002825B1A7D88A18A97579E93F936')
user = client.getUser(id64='76561198014207004')
user1 = user.raw_apps

m = re.findall('appid\'\: (.+?),', str(user1))
m = list(map(int, m))

gameCount = len(m)
print(gameCount)

total = 0

x=0
for x in range (gameCount):
    try:
        game = client.getApp(appid=m[x])
        price = game.price_overview
        n = re.findall('\'final\'\: (.+?),', str(price))
        n = list(map(int, n))
        total = total + sum(n)
        x = x + 1
    except:
        pass
    continue

print(total)

#penny weight
userAccount = total
pennyPerPound = 181.4368
pennyCalculation = total / pennyPerPound

print('Your account weighs ' + str(round(pennyCalculation,2)) + ' pounds in pennies.')

#physical weight
gameWeight = 0.3125
weightCalculation = gameCount * gameWeight

print('Your account weighs ' + str(round(weightCalculation,2)) + ' actual pounds.')