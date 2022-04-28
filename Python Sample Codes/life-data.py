def load_csv(life-expectancy.csv):
data =  []
    col = []
    checkcol = False
    with open(life-expectancy.csv) as f:
        for val in f.readlines():
            val = val.replace("\n","")
            val = val.split(',')
            if checkcol is False:
                col = val
                checkcol = True
            else:
                data.append(val)
    df = pd.DataFrame(data=data, columns=col)
return df