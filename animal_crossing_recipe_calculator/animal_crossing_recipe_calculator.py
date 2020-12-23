# Program:      Animal Crossing Recipe Calculator
# Author:       Jessica Cassidy
# Date:         12/06/2020
# The Recipe Calculator gives two recipe options from Animal Crossing New Horizons. The user picks from two recipes available. 
# After the user selected an option, the user is then prompted to provide their current inventory of each item applicable to the 
# recipe, then the program calculates the total items they can create from that recipe.

# | Option 1 - Illuminated Snowflakes Recipe     | Qty.  |
# | -------------------------------------------- | ------|
# | Blue Ornaments                               |  9    |
# | Iron Nuggets                                 |  3    |

# | Option 2 - Illuminated Reindeer              | Qty.  |
# | -------------------------------------------- | ------|
# | Gold Ornaments                               |  6    |
# | Iron Nuggets                                 |  5    |

# Input:        Pick a recipe from options 1 & 2; Enter inventory qty. of items req. for recipe.
# Output:       Total times you can execute/create an item based on that recipe.

import math


# // PICK RECIPE AND ENTER CURRENT INVENTORY COUNT
def pick_recipe():
    while True:
        print('\n//PICK A RECIPE//')
        pickRecipe = str(
            input('Which recipe would you like to create?\nEnter "1" for option 1 or "2" for option 2: \n'))
        print('\n//CURRENT INVENTORY//')
        if pickRecipe == '1':
            inv_ironNuggets1 = int(input('How many iron nuggets do you have?: '))
            inv_blueOrn = int(input('How many blue ornaments do you have?: '))
            return pickRecipe, inv_ironNuggets1, inv_blueOrn
        elif pickRecipe == 2:
            inv_ironNuggets2 = int(input('How many iron nuggets do you have?: '))
            inv_goldOrn = int(input('How many gold ornaments do you have?: '))
            return pickRecipe, inv_ironNuggets2, inv_goldOrn
        else:
            # Print error if user enters any numeric number besides 1 and 2
            if pickRecipe != '1' and '2':
                print("Error. Please Try again")

            # Print error if user enters lowercase/uppercase/symbol character.
            elif pickRecipe.isaplha() == True:
                print("Error. Please Try again")


# // CALCULATE HOW MANY OF A RECIPE YOU CAN CREATE
def calc_totals(pickRecipe, inv_ironNuggets1, inv_orn1):
    # Option 1 - Illuminated Snowflake Recipe
    if pickRecipe == '1':
        count_nugget1 = math.ceil(inv_ironNuggets1 / 9)
        count_orn = math.ceil(inv_orn1 / 3)

        nums = [count_nugget1, count_orn]
        length = len(nums)
        min = nums[0]
        max = nums[0]
        for index in range(length):
            if nums[index] < min:
                min = nums[index]
            if nums[index] > max:
                max = nums[index]
        snowflakes = math.floor(max / min)
        return snowflakes

    # Option 2 - Illuminated Reindeer Recipe
    elif pickRecipe == '2':
        count_nugget1 = math.ceil(inv_ironNugget / 6)
        count_orn = math.ceil(inv_orn2 / 5)

        nums = [count_nugget1, count_orn]
        length = len(nums)
        min = nums[0]
        max = nums[0]
        for index in range(length):
            if nums[index] < min:
                min = nums[index]
            if nums[index] > max:
                max = nums[index]
        reindeer = math.floor(max / min)
        return reindeer


# // DISPLAY TOTAL RECIPES CREATED OF OPTION 1 & 2
def display_total_recipe(pickRecipe, result):
    print('\n//TOTAL ITEMS YOU CAN CREATE FROM RECIPE CHOSEN//')
    if pickRecipe == '1':
        print('Total Illuminated Snowflakes: ', result)
    else:
        print('Total Illuminated Reindeer: ', result)


# // MAIN MODULE - DISPLAY RECIPE/MATERIALS AND CALL FUNCTIONS
def main():
    print(
        ' =========== ANIMAL CROSSING RECIPE CALCULATOR===========\n\n',
        '| Option 1 - Illuminated Snowflakes Recipe     | Qty.  |\n',
        '| -------------------------------------------- | ------|\n',
        '| Blue Ornaments                               |  9    |\n',
        '| Iron Nuggets                                 |  3    |\n\n',

        '| Option 2 - Illuminated Reindeer              | Qty.  |\n',
        '| -------------------------------------------- | ------|\n',
        '| Gold Ornaments                               |  6    |\n',
        '| Iron Nuggets                                 |  5    |')
    pickRecipe, inv_ironNugget, inv_Orn = pick_recipe()
    result = calc_totals(pickRecipe, inv_ironNugget, inv_Orn)
    display_total_recipe(pickRecipe, result)

main()