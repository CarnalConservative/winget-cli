i = 0
lowest = 1000
lowest_year = 1000
lowest_country = ""

pickAyear = int(input("What year do you want to know about?"))

with open("life-expectancy.csv") as lifeFile:
    for line in lifeFile:
        i = i + 1
        cleanLine = line.strip()
        item = cleanLine.split(",")
        if i > 1:
            country = item[0]
            code = item[1]
            year = int(item[2])
            life = float(item[3])
            if lowest > life:
                lowest = life
                lowest_year = year
                lowest_country = country
                print(f"{lowest} - {lowest_year} - {lowest_country}")
        if pickAyear == year:
            print(f"{year} - {country} - {life}")
