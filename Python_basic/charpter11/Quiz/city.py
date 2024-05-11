def city_form(city,country,population=0):
    if population!=0:
        a = city + ',' + country + '-population ' +str(population)
    else:
        a = city + ',' + country
    return a.title()
