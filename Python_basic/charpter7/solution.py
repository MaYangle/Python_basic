canteen = {
    'abloc':{
        'lunch' : [{
            'name' : 'chicke pea',
            'taste' : 'terrible',
            'price' : 'expensive'
        }]
    }
}

message = input("where's the food do you want to eat? ")
f = True

while f:
    print(message)
    if message.lower() in canteen:
        for food in canteen[message]['lunch']:
            food_name = food['name']
            food_taste = food ['taste']
            food_price = food['price']
            print(" we provid this kind food " + str(food_name)+ " today")
            detail = input('DO you want to know more details , yes or no?')
            if detail.lower() == 'yes':
                print('The food taste ' + str(food_taste) + ', and the price is ' + str(food_price))
            continue
    else:
        print("we don't have that canteen now ")
        f = False
