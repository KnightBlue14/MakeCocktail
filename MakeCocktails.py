import csv
import pandas as pd
import sys
import tracemalloc

tracemalloc.start()

class Ingredient:
    def __init__(self,cost,price,volume):
        self.cost = cost
        self.price = price
        self.volume = volume
        self.shots = self.volume/25
        self.cost_per = self.cost/self.shots
        self.sum = self.shots*self.price
        self.profit = self.sum-self.cost
        self.profit_per = self.profit/self.shots

class Accessory:
    def __init__(self,cost):
        self.cost = cost
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
        self.unit_per = self.unit/self.shots
    def IsNonAlc(self):
        return True if self.abv == 0 else False


class Mix(Ingredient):
    def __init__(self,cost,price,volume,serving,syrup = None):
        super().__init__(cost,price,volume)
        self.serving = serving
        self.syrup = syrup
        if syrup != None:
            self.serving = serving/6
        self.cost_per = cost/serving
        self.profit = self.price - self.cost_per

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

def find_item(item,type):
    with open(f'{type}.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)
        found = 0
        rowlist = []
        for row in reader:
            if row[0] == f'{item}':
                print(f"{item} found")
                rowlist = row
                return rowlist
                found += 1
        if found == 0:
            print('Item not found, please update')
        file.close

#Broken into individual sections rather than a single repeated function as the setup for each object is slightly different

csvspirit = pd.read_csv('Spirit.csv')
for index, row in csvspirit.iterrows():
    exec(f'{row["name"]} = Spirit({row["cost"]},{row["price"]},{row["volume"]},{row["abv"]})')

csvmix = pd.read_csv('Mix.csv')
for index, row in csvmix.iterrows():
    exec(f'{row["name"]} = Mix({row["cost"]},{row["price"]},{row["volume"]},{row["serving"]})')
    if row['syrup'] == False:
        pass
    else:
        exec(f'{row["name"]}.syrup = True')

def calculate_volume_from_ice(Glass,Ice):
    vol = Glass.volume
    if Ice.fill == 'full' and Ice.type == 'normal':
        vol = vol * 0.5
    if Ice.fill == 'full' and Ice.type == 'shake' and Glass == Martiniglass:
        vol = vol * 0.8
    if Ice.fill == 'full' and Ice.type == 'crushed':
        vol = vol * 0.5
    return vol

def MakeCocktail(spirit_dict,mix_dict,Glass,Price,Ice):
    vol = calculate_volume_from_ice(Glass,Ice)
    cost = 0
    fillers = sum(1 for v in mix_dict.values() if v == 0)
    nonfillers = sum(v for v in mix_dict.values() if v != 0)
    vol_neg = []
    for i in spirit_dict:
        try:
            i
        except NameError:
            print('Item not found, please update csv')
            break
        finally:
            pass
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



OldMout = Bottles(12,500,16.99,4.00)
Corona = Bottles(24,330,20.79,4.00)

Hurricane = Glass(590)
Martiniglass = Glass(120)
PineappleGlass = Glass(520)

NormalIce = Ice('normal','full')
MartiniIce = Ice('normal','shake')
CrushedIce = Ice('crushed','full')

SexonBeach = MakeCocktail({Vodka:1,Peach_Schnapps:1}, {OJ:0},Hurricane,6.50,NormalIce)
#PornstarMartini = MakeCocktail({Smirnoff:(35/25),Passoa:0.5}, {PJ:4},Martiniglass,9,MartiniIce)
#GratefulDead = MakeCocktail({DeadMansFingersSpicedRum:1,PinGrapeliquer:1},{OJ:0,Lemonade:0},PineappleGlass,9,CrushedIce)
print(SexonBeach.cost)

print(tracemalloc.get_traced_memory())
tracemalloc.stop()