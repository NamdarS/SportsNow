import requests
import re

page = requests.get("https://www.espn.com/")
pageText = page.text

basketball = len((re.findall("nba|basketball", pageText, re.IGNORECASE)))
football = len((re.findall("nfl|football", pageText, re.IGNORECASE)))
combatSports = len((re.findall("ufc|boxing", pageText, re.IGNORECASE)))
hockey = len((re.findall("nhl|hockey", pageText, re.IGNORECASE)))
baseball = len((re.findall("mlb|baseball", pageText, re.IGNORECASE)))

sports = [(basketball, "basketball"), (football, "football"),
          (combatSports, "combat sports"), (hockey, "hockey"),  (baseball, "baseball")]

total = sum(sport for sport, name in sports)
coveredSports = [sport for sport in sports if sport != 0]
percentages = [f"{str(int((sport / total) * 100))}% is {str(name)} related" for sport, name in coveredSports]

print("Right now,out of all the news on the page, approximately\n")
for percentage in percentages:
    print(percentage)
