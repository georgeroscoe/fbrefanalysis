# fbrefanalysis
Using the help of Christopher Martin's fbref scraper (https://github.com/chmartin/FBref_EPL), I have done some analysis on goals and assists in the 'big 5' (EPL,Ligue 1, La Liga, Serie A, Bundesliga) over the last two decades.


fbref.py is essentially Christopher Martin's scraper with a couple of things changed. It scrapes the following player stats, given a league and a season:

"player","minutes","goals","assists","pens_made","goals_per90","goals_assists_per90","goals_pens_per90","goals_assists_pens_per90"

and outputs them in to separate .csv files for each season.

I combined all of the data from the big 5 leagues from the 2000/2001 season up to and including the 2019/20 season. I also had the Premier League seasons from 1992/93 up to and including 1999/00.

This combined dataset can be found in the file ALLData2.csv, the separate data files for each league can be found also.

The script NPGA25.py grabs all of the player seasons where the player has got at least 25 Non-Penalty Goals + Assists, and outputs the player, the tally, and the seasons in to a .csv file.

The script AssistSeasons.py grabs the number of times a player has reached at least 10 league assists in a season, and outputs the ordered top 15 in to a .csv file.

The script NPGA90Stats.py grabs the the player, the Non-Penalty Goals + Assists per 90, the season, and the minutes, and outputs every player that has NPGA/90 of over 0.9 and has played over 1,500 minutes that season, in to a .csv file. 
