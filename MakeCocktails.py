class Ingredient:
    def __init__(self,cost,price,volume):
        self.cost = cost
        self.price = price
        self.volume = volume
        self.shots = int(self.volume/25)
        self.cost_per = self.cost/self.shots
        self.profit = (self.shots*self.price)-self.cost
        self.profit_per = self.profit/self.shots

class Accessory():
    def __init__(self):
        pass

class Glass:
    def __init__(self,volume):
        self.volume = volume
        self.measures = self.volume/25

class Spirit(Ingredient):
    def __init__(self,cost,price,volume,abv):
        super().__init__(cost,price,volume)
        self.abv = abv
        self.proof = self.abv*2
        self.unit = (self.abv/100)*self.volume/10
    def IsNonAlc(self):
        return True if self.abv == 0 else False


class Mix(Ingredient):
    def __init__(self,cost,price,volume):
        super().__init__(cost,price,volume)

class Bottles:
    def __init__(self,number,vol,cost,price):
        self.number = number
        self.vol = vol
        self.cost = cost
        self.price = price
        self.cost_per = self.cost/self.number
        self.profit_per = self.price - self.cost_per
        self.profit = self.price*self.number - self.cost

class Ice:
    def __init__(self,type,fill):
        self.type = type
        self.fill = fill

class Cocktail():
    def __init__(self,price,cost,volume):
        self.price = price
        self.cost = cost
        self.volume = volume
        self.profit = self.price - self.cost


def MakeCocktail(spirit_dict,mix_dict,Glass,Price,Ice):
    vol = Glass.volume
    if Ice.fill == 'full' and Ice.type == 'normal':
        vol = vol * 0.5
    if Ice.fill == 'full' and Ice.type == 'shake' and Glass == Martiniglass:
        vol = vol * 0.5
    if Ice.fill == 'full' and Ice.type == 'crushed':
        vol = vol * 0.5
    cost = 0
    fillers = sum(1 for v in mix_dict.values() if v == 0)
    nonfillers = sum(v for v in mix_dict.values() if v != 0)
    vol_neg = []
    for i in spirit_dict:
        vol_neg.append(spirit_dict[i])
    spirits = sum(vol_neg)
    for key,value in spirit_dict.items():
        cost += key.cost_per*value
    for key,value in mix_dict.items():
        if value == 0:
            mix_measure = (vol - spirits - nonfillers - (1 - 1/fillers))/25
            cost += key.cost_per*mix_measure
        elif value != 0:
            cost += value*key.cost_per
    return Cocktail(Price,cost,vol)

Vodka = Spirit(10,2.40,700,40)
NonAlcVodka = Spirit(10,2.00,700,0)
Peach_Schnapps = Spirit(8,2.40,700,37.5)
Smirnoff = Spirit(11.49,3.20,700,40)
Passoa = Spirit(9.49,2.60,700,17)
GreyGoose = Spirit(28.49,4.00,700,40)
BacardiWhite = Spirit(13.99,3.60,700,40)
DeadMansFingersSpicedRum = Spirit(14.49,4.00,700, 37.5)
PinGrapeliquer = Spirit(11.99,3.20,500,20)
Limoncello = Spirit(11.99,3.00,700,27)
Baileys = Spirit(10.99,3.60,700,17)
Kahlua = Spirit(11.99,4.00,700,20)
Absolut = Spirit(12.99,4.00,700,40)
Hendricks = Spirit(24.49,4.00,700,41.4)
BacardiWhiteLarge = Spirit(30.99,3.60,1500,40)
BombaySapphire = Spirit(15.69,3.80,700,40)
PatronTequila = Spirit(35.99,4.00,700,40)
JoseCuervo = Spirit(17.49,3.40,700,35)
KrakenRum = Spirit(19.49,3.60,700,40)
SambucaBlack = Spirit(14.99,3.50,700,38)
SambucaWhite = Spirit(12.49,3.50,700,38)
TequilaRose = Spirit(11.79,3.20,700,15)
Midori = Spirit(13.79,2.80,700,27)
TiaMaria = Spirit(11.49,3.20,700,20)

OldMout = Bottles(12,500,16.99,4.00)
Corona = Bottles(24,330,20.79,4.00)

OJ = Mix(1.70,1.75,1000)
PJ = Mix(1.70,1.75,1000)
Lemonade = Mix(47.49,1.75,7000)

Hurricane = Glass(590)
Martiniglass = Glass(120)
PineappleGlass = Glass(520)

BeachIce = Ice('normal','full')
MartiniIce = Ice('normal','shake')
CrushedIce = Ice('crushed','full')

SexonBeach = MakeCocktail({Vodka:1,Peach_Schnapps:1}, {OJ:0},Hurricane,6.50,BeachIce)
PornstarMartini = MakeCocktail({Smirnoff:(35/25),Passoa:0.5}, {PJ:4},Martiniglass,9,MartiniIce)
GratefulDead = MakeCocktail({DeadMansFingersSpicedRum:1,PinGrapeliquer:1},{OJ:0,Lemonade:0},PineappleGlass,9,CrushedIce)
print(GratefulDead.profit)
print(Vodka.unit)

