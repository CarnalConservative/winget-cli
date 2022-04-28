import pandas as pd # Our data manipulation library 
import seaborn as sns # Used for graphing/plotting 
import matplotlib.pyplot as plt # If we need any low level methods 
import os # Used to change the directory to the right place 
players = pd.read_csv("basketball_players.csv") 
master = pd.read_csv("basketball_master.csv") # We can do a left join to "merge" these two datasets together 
nba = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID") 
mean = players["points"].mean() 
median = players["points"].median() 
print("Points per season: Mean:{:.2f}, Median:{}".format(mean, median)) 
print(players[["playerID", "year", "tmID", "points"]].sort_values("points", ascending=False).head(10)) 
sns.boxplot(data=nba[["points", "assists", "rebounds"]]) 
plt.show()


nba["medianPerGame"] = nba["points"] / nba["GP"] 
print(nba[["year", "useFirst", "lastName", "points", "GP", "medianPerGame"]].sort_values("medianPerGame", ascending=False).head(10)) 
nba_grouped_year = nba[["medianPerGame","year"]].groupby("year").median() 
print(nba_grouped_year) 
nba_grouped_year = nba_grouped_year.reset_index() 
sns.regplot(data=nba_grouped_year, x="year", y="medianPerGame") 
plt.show()


print(nba[["playerID", "points","fgAttempted", "ftAttempted", "threeAttempted",]].sort_values("points", ascending=False).head(10)) 
print(nba[["playerID","points","GP","fgMade", "ftMade", "threeMade","assists"]].sort_values("points", ascending=False).head(20)) 
print(nba[["playerID", "points","year","threeMade",]].sort_values("year", ascending=False).head(20)) 
print(nba[["playerID", "year","points","GP", "fgMade", "ftMade", "threeMade","assists",]].sort_values("points", ascending=False).head(20)) 
print(nba[["playerID", "year","points", "hsCity", "hsState", "hsCountry","threeMade"]].sort_values("points", ascending=False).head(20)) 
nba.tail().plot(kind="bar", rot=10, title= "Three Points Throw", x= "playerID", Y = "No. of Throws" ) 
plt.show()  