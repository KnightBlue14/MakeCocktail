# Make Cocktails
A python script to calculate a number of variables involved in making cocktails, including price, abv and volume of the final drink
## Description
This project is an exercise in the use of standardised Python classes in order to bulk-generate objects that can then be used to carry out operations. In this instance, using listed prices, volumes and other variables of ingredients and tools to calulate the components of a given cocktail.

IMPORTANT DISCLAIMER -- 
The total calulated price does not necessarily represent the total cost to produce, as a number of factors are not accounted for here, such as the cost of electricty, cost of tools, cost of labour, etc. This is primarily based on prices I was able to find online, and at my local bar. Your experience may vary.

Also, spirits are assumed to be used in standardised measures of 25ml, or 'shots'. This will be relevant when determining the amount of ingredients used in the final product.



## How to use

The files listed are, for all intents and purposes, complete, and do not need any editing to change their functionality, though you may need to add some information to the csv files, to increase your options. I will elaborate further in the relevant section.

### CSV files
These are the long-term storage files for ingredients, glasses, ice types, etc. The information stored in these is used by the main Python file to generate the cocktail. As mentioned, if an ingredient is not listed here, you will need to add it for your cocktail.

Spirits are self-explanatory, simply add name and cost, how much you would charge per serving of 25ml, total volume, and the alcohol by volume (ABV). For spirits, this is typically around 40%.

Bottles and Glasses are also straightforward, simply fill the columns.

Ice requires more explanation - the 'fill' column refers to how much of the glass is filled by the ice. For simplicity's sake, I have taken crushed and normal ice to fill the glass. As for MartiniIce, this is shaken, so none of the ice goes into the glass.

As for Mix, there are a few things of note. 'Serving' refers to how much of each ingredient is used in a normal serving. In my local, a normal glass of juice is 250ml. As for soft drinks, these are in boxed bags of syrup mixed with soda water, at a ratio of approximatley 1:5 syrup to water. This is reflected in the main python file, but the overall serving is still 250ml. Finally, cocktail syrups, such as Grenadine, only need a dash at a time, hence the small serving size, and are not served as individual items, so the price is set to zero. How the 'syrup' label is implemented in the main file will be explained in the relevant section.


### MakeCocktails.py

The primary file that brings everything together. The only changes you need to make are at the end, but I will go over it to explain a few key points.

#### (Line 4 - 79)
These lines cover the creation of classes, to be used when the cocktails are generated. Most of the classes are derived from the 'Ingredient' class, though some require their own.
A feature of classes in Python is that most properties can be inherited from a superclass, allowing you to add features based on input variables. For instance, the 'Mix' class features many properties from 'Ingredient', such as cost_per, shots and profit. However, it also has it's own properties, primarily based on the type of syrup. If it is not a syrup, it is simply treated as a normal ingredient. Id it is a syrup, this will adjust the amount used per serving, which in turn affects the potential profit and cost per shot. 
The final class is the 'Cocktail' class, which is used based on your input.

#### (Line 98 - 125)
These blocks of code parse the csv files to generate objects using the classes defined earlier. This is relatively inefficient, as it will create objects you will not use, but I was unable to automate the process only using what was provided, due to how I was creating them. They are only in use while the script runs, so they will be removed from memory once it is done, but this does result in noticeable RAM usage and increased time, which will increase further as more items are added to the csvs.

#### (Line 128 - 136)

This determines how much volume is taken up by ice in the glass, which will later determine how much of other ingredients need to be used. For instance, using normal, blocked ice is assumed to take up half the volume of a glass when filled, so the volume of the glass is simply halved. The values listed are based on my own experience, and are not based on any definitive testing or research, so if you disagree, feel fee to change them.

#### (Line 138 - 158)

The function to generate the cocktail, used in this format -
```
MakeCocktail(spirit_dict,mix_dict,Glass,Price,Ice)
```
To help explain, I will use the example of a 'Sex on the Beach', lsited below -
```
SexonBeach = MakeCocktail({Vodka:1,PeachSchnapps:1}, {OrangeJuice:0,Grenadine:1},Hurricane,6.50,NormalIce)
```
After calculating available volume, it will initialise variables for tracking. Then, the number of fillers and non-fillers - 
fillers are mixer ingredients that are not measured specifically, and are simply poured over the other ingredients until the glass is full (Ths is not an official term, I am just using it for explanation's sake). However, multiple fillers can be used, so the total number of them needs to be tracked. Conversley, non-fillers are ingredients that are used in measured amounts.
Once the number of ingredients is calculated, further volume operations are carried out - before the amount of filler can be calulated, we must first determine how much volume will need to be filled, for which we will use 'vol_neg'. This is calculated by simply adding the total number of shots of spirit. Then, the same is done for non-fillers. Finally, we calculate how much volume is left to fill, by subtracting vol_neg and the number of non-fillers from the total volume of the glass. The remaining volume is then divided by 25, to determine how many shots of filler are needed.

Now that we have everything, we can calculate the cost, and other variables of our cocktail -
```
Cost to make - £1.29 
Price sold - £6.5 
Profit - £5.21 
ABV - 6.6 
Ice used - cubed
```

Again, this does not necessarily represent the total cost of production, and is only based on the ingredients used.