import math
speed = 0
in_temperature = 0
realfeel = 0
fahren_temp = 0
foc = ""

def celsius2Fahren(f_temperature):
    fahren_temp = float((in_temperature*9/5)+32)
    return fahren_temp

def wind_chill(speed, in_temperature):
    realfeel = float(35.74 + 0.6215 * in_temperature - 35.75 * speed ** 0.16 + 0.4275 * in_temperature * speed ** 0.16)
    return realfeel

    