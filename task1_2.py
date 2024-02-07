with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for recipe_line in file:
        recipe_name = recipe_line.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recipe = file.readline().strip().split(' | ')
            product, quantity, word = recipe
            ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
        file.readline()
        cook_book[recipe_name] = ingredients
        
output = "cook_book = {\n"
for dish, ingredients in cook_book.items():
    output += f"  '{dish}': [\n"
    for ingredient in ingredients:
        output += f"    '{ingredient}',\n"
    output += "  ],\n"
output += "}"
print(output)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                product = ingredient['product']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if product in shop_list:
                    shop_list[product]['quantity'] += quantity
                else:
                    shop_list[product] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Такого блюда '{dish}' нет в книге")
    return shop_list

result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(result)
