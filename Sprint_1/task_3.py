world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions [2022] = 'Аргентина'
for year in world_champions.keys():
    print(year, '-', world_champions[year])

country = 'Италия'
if 2022 in world_champions:
    print(country + ' cтановилась чемпионом мира по футболу в 21 веке!')
else:
       print(country + ' не выигрывала чемпионат мира по футболу в 21 веке.')