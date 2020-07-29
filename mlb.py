from bs4 import BeautifulSoup
import requests
import webbrowser
from pandas import pandas as pd




# Enter the name of a team and its opponent and figure out how many times the team has won against oppenent in the past five years
def num_games_won_versus_regular_season(team, opponent):
    num_games = 0
    year = 0
    for year in range(2017, 2020):
        url = 'https://www.baseball-reference.com/teams/'+str(team)+'/'+ str(year) + '-schedule-scores.shtml'
        web_page = requests.get(url)
        soup = BeautifulSoup(web_page.content, 'lxml')
        for div in soup.findAll('div', class_ = 'overthrow table_container'):
            table = div.findAll('table')[0]
            season_data = pd.read_html(str(table))[0]
            Opp = season_data["Opp"]
            W_L = season_data['W/L']
            for i in range(len(Opp)):
                    if(Opp[i] == opponent and (W_L[i] == 'W' or W_L[i] == 'W-wo')):
                        num_games +=1             
    return num_games

# Determine the amount of games a team has played an opponent
def num_games_played_versus_regular_season(team, opponent):
    num_games = 0
    year = 0
    for year in range(2017, 2020):
        url = 'https://www.baseball-reference.com/teams/'+str(team)+'/'+ str(year) + '-schedule-scores.shtml'
        web_page = requests.get(url)
        soup = BeautifulSoup(web_page.content, 'lxml')
        for div in soup.findAll('div', class_ = 'overthrow table_container'):
            table = div.findAll('table')[0]
            season_data = pd.read_html(str(table))[0]
            Opp = season_data["Opp"] 
            for i in range(len(Opp)):
                    if(Opp[i] == opponent):
                        num_games +=1    
    return num_games 

# Determine the average amount of runs a team scores in wins against an opponent
def avg_num_runs_scored_in_wins_against(team,opponent):
    num_runs_scored = []
    year = 0
    total = 0
    for year in range(2017, 2020):
        url = 'https://www.baseball-reference.com/teams/'+str(team)+'/'+ str(year) + '-schedule-scores.shtml'
        web_page = requests.get(url)
        soup = BeautifulSoup(web_page.content, 'lxml')
        for div in soup.findAll('div', class_ = 'overthrow table_container'):
            table = div.findAll('table')[0]
            season_data = pd.read_html(str(table))[0]
            Opp = season_data["Opp"]
            W_L = season_data['W/L']
            runs = season_data['R']
            for i in range(len(Opp)):
                    if(Opp[i] == opponent and (W_L[i] == 'W' or W_L[i] == 'W-wo')):
                        num_runs_scored.append(runs[i])
    
    for i in range(len(num_runs_scored)):
        total += int(num_runs_scored[i])
    avg = total / len(num_runs_scored)
    return round(avg,3)

#Determine the average amount of runs a team allows in wins against an opponent
def avg_num_runs_allowed_in_wins_against(team,opponent):
    num_runs_allowed = []
    year = 0
    total = 0
    for year in range(2017, 2020):
        url = 'https://www.baseball-reference.com/teams/'+str(team)+'/'+ str(year) + '-schedule-scores.shtml'
        web_page = requests.get(url)
        soup = BeautifulSoup(web_page.content, 'lxml')
        for div in soup.findAll('div', class_ = 'overthrow table_container'):
            table = div.findAll('table')[0]
            season_data = pd.read_html(str(table))[0]
            Opp = season_data["Opp"]
            W_L = season_data['W/L']
            runs = season_data['RA']
            for i in range(len(Opp)):
                    if(Opp[i] == opponent and (W_L[i] == 'W' or W_L[i] == 'W-wo')):
                        num_runs_allowed.append(runs[i])
    
    for i in range(len(num_runs_allowed)):
        total += int(num_runs_allowed[i])
    avg = total / len(num_runs_allowed)
    avg = total / len(num_runs_allowed)
    return round(avg,3)

#Determine the average amount of runs a team scores in all wins
def avg_num_runs_score_in_wins(team):
    num_runs_scored = []
    year = 0
    total = 0
    for year in range(2017, 2020):
        url = 'https://www.baseball-reference.com/teams/'+str(team)+'/'+ str(year) + '-schedule-scores.shtml'
        web_page = requests.get(url)
        soup = BeautifulSoup(web_page.content, 'lxml')
        for div in soup.findAll('div', class_ = 'overthrow table_container'):
            table = div.findAll('table')[0]
            season_data = pd.read_html(str(table))[0]
            W_L = season_data['W/L']
            runs = season_data['R']
            for i in range(len('W/L')):
                    if(W_L[i] == 'W' or W_L[i] == 'W-wo'):
                        num_runs_scored.append(runs[i])
    
    for i in range(len(num_runs_scored)):
        total += int(num_runs_scored[i])
    avg = total / len(num_runs_scored)
    return round(avg,3)

# Determine the avg num of runs allowed in all wins
def avg_num_runs_allowed_in_wins(team):
    num_runs_allowed = []
    year = 0
    total = 0
    for year in range(2017, 2020):
        url = 'https://www.baseball-reference.com/teams/'+str(team)+'/'+ str(year) + '-schedule-scores.shtml'
        web_page = requests.get(url)
        soup = BeautifulSoup(web_page.content, 'lxml')
        for div in soup.findAll('div', class_ = 'overthrow table_container'):
            table = div.findAll('table')[0]
            season_data = pd.read_html(str(table))[0]
            W_L = season_data['W/L']
            runs = season_data['RA']
            for i in range(len('W/L')):
                    if(W_L[i] == 'W' or W_L[i] == 'W-wo'):
                        num_runs_allowed.append(runs[i])
    
    for i in range(len(num_runs_allowed)):
        total += int(num_runs_allowed[i])
    avg = total / len(num_runs_allowed)
    return round(avg,3)

# Determine total amount of night game wins
def night_game_wins(team):
    num_Games = 0
    year = 0
    for year in range(2017, 2020):
        url = 'https://www.baseball-reference.com/teams/'+str(team)+'/'+ str(year) + '-schedule-scores.shtml'
        web_page = requests.get(url)
        soup = BeautifulSoup(web_page.content, 'lxml')
        for div in soup.findAll('div', class_ = 'overthrow table_container'):
            table = div.findAll('table')[0]
            season_data = pd.read_html(str(table))[0]
            W_L = season_data['W/L']
            tofd = season_data['D/N']
            for i in range(len(W_L)):
                    if((W_L[i] == 'W' or W_L[i] == 'W-wo') and tofd[i] == 'N'):
                        num_Games += 1
    return num_Games

# Determine total amount of day game wins
def day_Game_wins(team):
    num_Games = 0
    year = 0
    for year in range(2017, 2020):
        url = 'https://www.baseball-reference.com/teams/'+str(team)+'/'+ str(year) + '-schedule-scores.shtml'
        web_page = requests.get(url)
        soup = BeautifulSoup(web_page.content, 'lxml')
        for div in soup.findAll('div', class_ = 'overthrow table_container'):
            table = div.findAll('table')[0]
            season_data = pd.read_html(str(table))[0]
            W_L = season_data['W/L']
            tofd = season_data['D/N']
            for i in range(len(W_L)):
                    if((W_L[i] == 'W' or W_L[i] == 'W-wo') and tofd[i] == 'D'):
                        num_Games += 1
    return num_Games

# Determine total number of day games played
def num_games_played_day(team):
    num_Games = 0
    year = 0
    for year in range(2017, 2020):
        url = 'https://www.baseball-reference.com/teams/'+str(team)+'/'+ str(year) + '-schedule-scores.shtml'
        web_page = requests.get(url)
        soup = BeautifulSoup(web_page.content, 'lxml')
        for div in soup.findAll('div', class_ = 'overthrow table_container'):
            table = div.findAll('table')[0]
            season_data = pd.read_html(str(table))[0]
            tofd = season_data['D/N']
            for i in range(len(tofd)):
                    if(tofd[i] == 'D'):
                        num_Games += 1
    return num_Games

# determine total number of night games played
def num_games_played_night(team):
    num_Games = 0
    year = 0
    for year in range(2017, 2020):
        url = 'https://www.baseball-reference.com/teams/'+str(team)+'/'+ str(year) + '-schedule-scores.shtml'
        web_page = requests.get(url)
        soup = BeautifulSoup(web_page.content, 'lxml')
        for div in soup.findAll('div', class_ = 'overthrow table_container'):
            table = div.findAll('table')[0]
            season_data = pd.read_html(str(table))[0]
            tofd = season_data['D/N']
            for i in range(len(tofd)):
                    if(tofd[i] == 'N'):
                        num_Games += 1
    return num_Games

#return win percentage for night games
def percent_night_games_won(team):
    return round(night_game_wins(team)/num_games_played_night(team),3)

#return win percentage for day games
def percent_day_games_won(team):
    return round(day_Game_wins(team)/num_games_played_day(team),3)

# return number of runs scored in night games
def num_runs_scored_night(team):
    num_runs_allowed = []
    year = 0
    total = 0
    for year in range(2017, 2020):
        url = 'https://www.baseball-reference.com/teams/'+str(team)+'/'+ str(year) + '-schedule-scores.shtml'
        web_page = requests.get(url)
        soup = BeautifulSoup(web_page.content, 'lxml')
        for div in soup.findAll('div', class_ = 'overthrow table_container'):
            table = div.findAll('table')[0]
            season_data = pd.read_html(str(table))[0]
            runs = season_data['R']
            tofd = season_data['D/N']
            for i in range(len(tofd)):
                    if(tofd[i] == 'N'):
                        num_runs_allowed.append(runs[i])
    
    for i in range(len(num_runs_allowed)):
        total += int(num_runs_allowed[i])
    avg = total / len(num_runs_allowed)
    return round(avg,3)

# return number of runs scored in day games
def num_runs_scored_day(team):
    num_runs_scored = []
    year = 0
    total = 0
    for year in range(2017, 2020):
        url = 'https://www.baseball-reference.com/teams/'+str(team)+'/'+ str(year) + '-schedule-scores.shtml'
        web_page = requests.get(url)
        soup = BeautifulSoup(web_page.content, 'lxml')
        for div in soup.findAll('div', class_ = 'overthrow table_container'):
            table = div.findAll('table')[0]
            season_data = pd.read_html(str(table))[0]
            runs = season_data['R']
            tofd = season_data['D/N']
            for i in range(len(tofd)):
                    if(tofd[i] == 'D'):
                        num_runs_scored.append(runs[i])
    
    for i in range(len(num_runs_scored)):
        total += int(num_runs_scored[i])
    avg = total / len(num_runs_scored)
    return round(avg,3)

# return the win percentage for team 
def winPercentage(team):
    numerator = night_game_wins(team) + day_Game_wins(team)
    denominator = num_games_played_night(team) + num_games_played_day(team)
    win_percent = (numerator/denominator)
    return round(win_percent,3)


# return the win probability in a head to head match up
def pureWinProb_against(team, opponent):
    numerator = winPercentage(team) * (1 - winPercentage(opponent))
    denominator = numerator + winPercentage(opponent) * (1 - winPercentage(team))
    return round(numerator/denominator,3)

# return the win probability in a head to head at night
def winProb_against_night(team, opponent):
    numerator = percent_night_games_won(team) * (1 - percent_night_games_won(opponent))
    denominator = numerator + percent_night_games_won(opponent) * (1 - percent_night_games_won(team))
    return round(numerator/denominator, 3)

# return win probability in a head to head during day
def winProb_against_day(team, opponent):
    numerator = percent_day_games_won(team) * (1 - percent_day_games_won(opponent))
    denominator = numerator + percent_day_games_won(opponent) * (1 - percent_day_games_won(team))
    return round(numerator/denominator, 3)


def bookie():
    team_in = input("enter a team: ")
    opponent_in = input("enter an opponent: ")
    over_under = input("enter the over under: ")
    over_under = float(over_under)
    time_of_day = input("night or day game? ")


    print("data from past 3 seasons:\n")
    print(str(team_in) + " won " + str(num_games_won_versus_regular_season(team_in,opponent_in)) + " out of " + str(num_games_played_versus_regular_season(team_in,opponent_in)) + " against " + str(opponent_in))
    print(str(team_in) + " has a " + str(pureWinProb_against(team_in,opponent_in)) + " chance of winning in head to head match-ups against " + str(opponent_in))

    if(time_of_day == "night"):

        print("\nIf the game is played at night:") 
        print(str(team_in) + " has a " + str(winProb_against_night(team_in,opponent_in))+ " chance of winning head to head against "+ str(opponent_in))
        runs_scored = num_runs_scored_night(team_in) + num_runs_scored_night(opponent_in)
        if(runs_scored >= over_under) :
            print("Predicted runs scored : " + str(runs_scored) + "\nWe recommend betting the over")
        else:
            print("Predicted runs scored : " + str(runs_scored) + "\nWe recommend betting the under")
        
    elif(time_of_day == "day"):

        print("\nIf the game is played during the day:")
        print(str(team_in) + " has a " + str(winProb_against_day(team_in,opponent_in)) + " chance of winning head to head against " + str(opponent_in))
        runs_scored = num_runs_scored_day(team_in) + num_runs_scored_day(opponent_in)
        if(runs_scored >= over_under) :
            print("Predicted runs scored : " + str(runs_scored) + "\nWe recommend betting the over")
        else:
            print("Predicted runs scored : " + str(runs_scored) + "\nWe recommend betting the under")
    

def main():
    print("When entering teams, enter the three letter acronym")
    bookie()
    again = input("Want more? (y/n) ")
    if(again == 'y'):
        bookie()
    elif(again == 'n'):
        print("Hope you win!")
    else:
        print("invalid input, running program again")
        bookie()


if __name__ == "__main__":
    main()
