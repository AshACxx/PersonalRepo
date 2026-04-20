import requests
import pandas as pd
print("hi")

# ---------------------------------
# 1. Fetch data from API
# ---------------------------------
def fetch_data(url):
    response = requests.get(url, timeout=30)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None


# ---------------------------------==
# 2. Extract games + date
# ---------------------------------
def get_games(data):
    game_date = data["scoreboard"]["gameDate"]
    games = data["scoreboard"]["games"]
    return game_date, games


# ---------------------------------
# 3. Print basic info
# ---------------------------------
def print_games(games):
    for game in games:
        home = game["homeTeam"]["teamName"]
        away = game["awayTeam"]["teamName"]
        status = game["gameStatusText"]
        print(f"{away} vs {home} → {status}")


# ---------------------------------
# 4. Build DataFrame
# ---------------------------------
def build_dataframe(game_date, games):
    rows = []

    for game in games:
        home = game["homeTeam"]["teamName"]
        away = game["awayTeam"]["teamName"]
        home_score = game["homeTeam"]["score"]
        away_score = game["awayTeam"]["score"]
        status = game["gameStatusText"]

        row = {
            "date": game_date,
            "game_id": game["gameId"],
            "home_team": home,
            "away_team": away,
            "home_score": home_score,
            "away_score": away_score,
            "total_score": home_score + away_score,
            "status": status,
            "went_ot": "OT" in status
        }

        rows.append(row)

    df = pd.DataFrame(rows)
    return df

def hscoring_game(games):
    highest = 0
    best_game = None
    
    for game in games:
        home = game["homeTeam"]["teamName"]
        away = game["awayTeam"]["teamName"]
        home_score = game["homeTeam"]["score"]
        away_score = game["awayTeam"]["score"]
        
        total = home_score + away_score
        
        if total > highest:
            highest = total
            best_game = (home,away)
            
    return highest, best_game

def lscoring_game(games):
    lowest = 0
    worst_game = None
    
    for game in games:
        home = game["homeTeam"]["teamName"]
        away = game["awayTeam"]["teamName"]
        home_score = game["homeTeam"]["score"]
        away_score = game["awayTeam"]["score"]
        
        total = home_score + away_score
        
        if total < lowest:
            lowest = total
            worst_game = (home,away)
            
    return lowest, worst_game
        

def overtime(games):
    found = False
    
    for game in games:
        overtimes = game["gameStatusText"]
        if "OT" in overtimes:
            home = game["homeTeam"]["teamName"]
            away = game["awayTeam"]["teamName"]
            print(f"{home} vs {away} went to overtime")
            found = True
            
    if not found:
            print("No games went to OT")
            
        


def main():
    url = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"
    
    
    
    
    data = fetch_data(url)
    
    if data is None:
        return
    
    import json
    with open("nba_data.json", "w") as f:
        json.dump(data, f, indent=2)
        print(json.dumps(data, indent=2))
    
    game_date, games = get_games(data)
    print("Games today:\n")
    print_games(games)
    
    
    highest, best_game = hscoring_game(games)
    print(f"Highest scoring game: {highest} by {best_game[0]} vs {best_game[1]}")
    
    overtime(games)

    print("\nCreating DataFrame...\n")
    df = build_dataframe(game_date, games)

    print(df)


    print("\nNumber of games:", len(df))

# ---------------------------------
# Run program
# ---------------------------------
if __name__ == "__main__":
    main()