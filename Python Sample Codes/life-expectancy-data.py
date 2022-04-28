with open("life-expectancy.csv") as life_expec:
    for line in life_expec:
        load_out = life_expec.split(",")
        print(load_out)