# Cocktail Generator
This is a python script that generates cocktails from a list of given ingredients, along with properties that can be used to track a number of variables, including the cost of ingredients, how much alcohol is in the cocktail, and profit based on a given price.

## Description
This project is based on my work at a bar, in which I mix and serve cocktails, using a variety of ingredients, including spirits, mixers, syrups, and many more. From time to time, I am able to get a look at catalogues, offering deals and discounts, which led me to wonder how far that caost is spread, hence the creation of this tool. Potentially, it could be used to help track costs for a cocktail in a business, or even for personal use. The listed prices are based on a number of sources, and will need to be updated to reflect your own options.

IMPORTANT NOTE -

The costs and prices listed do not necessarily represent the entire cost of the product to the business. There are many more 'hidden' costs to consider, such as the cost of electricity, heating, other appliances, or the labour and skill in preparing the drink, none of which are represented in this project. The only prices considered are the upfront cost of purchase (based on local prices, catalogue prices, and online storefronts), and the price at which it may be sold (based on the bar where I work, as well as others in my local area). 



## How to use
As mentioned earlier, the prices listed will need to be updated depending on the options you have available, be it from local retailers or online stores. Additionally, this script works from a few assumptions, which you will also need to change if needed. I will address each of them as they arise.

### CSV files
This is where the base information for each class is stored, with associated variables. For instance Spirit.csv has listed a number of spirits, including their cost to purchase, their price per shot, total volume of the bottle, and abv (Alcohol by volume). This information is used to create instances of the associated class. 

All prices are in pounds, all volumes are in millilitres, and abv is in percentage (i.e. '40' in the file refers to an abv of 40%)

Two quick notes - first, the price column in Glass.csv has each value set to zero. This is because when automating the instance creation process, I found a consistent issue with this class but not others. Upon adding the price column, the issue appears to have been resolved. The price of glasses is not accounted for, so it doesn't affect anything.

Second, by 'shot', I am referring to a standard shot size of 25ml. In accordance with UK law, shots sold on premises must be in either 25ml measures, or 35ml measures. If you serve in 35ml measures, you will need to update the main file and the test file accordingly.

### test_MakeCocktails.py
This is a testing suite for the main function, serving as a demonstration of what outcomes are expected from different inputs. Apart from adjusting these outcomes if you need to change prices or measure sizes, this can be left alone, and is more of a debugging tool.

### MakeCocktails.py
This is the primary file of this project. For full transparency, and to aid if any changes need to be made, I will go over it section by section, as well as point out some other assumptions made

#### 1-73 - Classes
The classes serve to assign properties to objects, which are then used to perform calulations. The Ingredient class is used as the superclass, from which the Spirit and Mix
classes inherit many properties. They then have additional functions for their own uses - for instance, Spirit has properties specific to alcoholic drinks, and Mix has a function to adjust serving sizes based upon it's type.

For those unfamiliar, soft drinks such as lemonade or coke can be sold as syrups, which are then mixed with soda water. Some sources I found suggested that this would be done at a ratio of 5 parts soda to 1 part syrup, so the serving size is adjusted appropriatley. In addition, simple syrups such as Grenadine can be added to cocktails for flavour. A standard pump for a 700ml bottle will dispense 10ml, so a 'shot' for simple syrups is assumed to be 10ml.

#### 75-89 - find_item
This is a function intended to search the csvs and find if an ingredient is present. If it is not present, then the cocktail cannot be generated. Currently, it is not used, as another function has rendered it redundant, but I have opted to leave it in as using it would be more efficient than what I currently have, I am just not currently able to implement it successfuly.

#### 91 - 119 - Setting up instances
These blocks of code iterate over each csv file, and generate instances based on each item. Ideally, this would only be done to ingredients listed in the cocktail recipe, but I have not yet been able to implement it. Instead, this setup generates every object, even if it is not used, resulting in much more ram usage. When I am able to work a solution, I wull update this accordingly. Additionaly, rather than a single function for all classes, I have split them into different blocks, as each one is set up differently, and the class used needs to be specified. This is also where servings for Mix objects are adjusted, as it needs to be done after the instances are generated.

#### 122 - 130 - Calculating volume from ice
Here is where we start to apply our instances. In a cocktail glass, the total volume available is reduced depending on how much ice is used. This function serves to apply that reduction, depending on what ice is used on what glass. For instance, a hurricane glass is 590ml. Cocktails that use this glass usually call for being filled with ice, which I have assumed to take up half the volume. Therefore, the volume left will be 295ml, which is then applied in the next function.

As for the Martini glass, this is based on my experience with the Pornstar Martini. While no ice is in the glass, the final product should have a foam layer on top, from shaking the ingredients. I have assumed this layer, plus some ice melting during mixing, to take up 20% of the total volume. 

These amounts are not based on any direct measurement, so feel free to change it of you disagree. Also, it does not account for every potential combination - I intend to update this over time.

#### 132 - 157 - Mixing the cocktail
Now all of the ingredients are brought together.

To initialise the function, call it in this format -

```
{Name} = MakeCocktail({[Name of Spirit]:[Number of shots]}, {[Name of mixer]:[Number of shots]},{Type of glass},{Price},{Type of ice})
```
In the case of a Sex on the Beach, it would read -
```
SexonBeach = MakeCocktail({Vodka:1,PeachSchnapps:1}, {OrangeJuice:0,Grenadine:1},Hurricane,6.50,NormalIce)
```
Alternatively, a Pornstar Martini would read -
```
PornstarMartini = MakeCocktail({Smirnoff:35/25,Passoa:12.5/25}, {PineappleJuice:4},Martiniglass,9,MartiniIce)
```
as the Smirnoff and Passoa are not added in standard measures, and the amount of Pineapple Juice is specified.

After calculating the volume left from adding ice, the variables cost, vol_neg and units are initialised. Then, the variables filler and nonfiller are created. Filler refers to any mixer that is used without a specific measurement, such as Orange Juice in Sex on the Beach, where [Number of shots] is given as 0. Conversley, nonfiller refers to when a number is given, such as with the Grenadine, where 1 measure of 10ml is specified.

That done, spirits are then applied. Vol_neg is the total volume taken by the spirits, and units refers to how many units of alcohol are in the drink, which can then be used to calculate abv. After this, the cost per ingredient is tallied and added to the total.

Next, the mixers. If the amount of mixer used is specified, then cost per shot is simply added, as is the case with Grenadine. However if it is not, then we need to determine how much volume needs to be filled, using these formulae -
```
147 - vol = vol/25 - vol_neg - nonfillers

150 - mix_measure = vol/fillers
151 - cost += key.cost_per_shot*mix_measure
```
In the case of Sex on the Beach, vol (295ml) is divided by 25 to meet the standard shot measure. Then, vol_neg and nonfillers, both measured in shots, are subtracted. The remaining volume is then divided by the number of fillers, into mix_measure. That done, the cost per shot of orange juice is multiplied by mix_measure to determine the total cost of the mixer

Finally, all of the outputs of these functions are used to generate the cocktail -
```
return Cocktail(Price,cost,vol,units,Ice)
```

Once it has been generated, you can then print a brief descriptive paragraph, as shown below
```
print(SexonBeach)

Cost to make - £1.29 
Price sold - £6.5
Profit - £5.21
ABV - 6.6
Ice used - cubed
```

Do note that your experience may vary, depending on the ice you use, the glass you use, whether you include garnish, whether you increase a serving, or any number of other variables. Again, if anything on your end differs from what you find here, feel free to change it to reflect your use case.