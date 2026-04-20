import requests
import json

# Send GET request to NBA API
response = requests.get(
    url="https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json",
    timeout=30
)

# Convert response to Python dictionary (JSON → dict)
data = response.json()

# Check if request was successful (status 200 = OK)
if response.status_code == 200:
    data = response.json()
    
    # Access list of games
    games = data["scoreboard"]["games"]
    
    # Loop through each game and print basic info
    for game in games:
        home = game["homeTeam"]["teamName"]
        away = game["awayTeam"]["teamName"]
        status = game["gameStatusText"]
        
        print(f"Home Team: {home}, Away Team: {away}, Status: {status}")

else:
    print("Error:", response.status_code)

# -------------------------------
# Mini Challenges Section
# -------------------------------

if response.status_code == 200:
    data = response.json()
    games = data["scoreboard"]["games"]
    
    # Find games that went to overtime
    for game in games:
        if "OT" in game["gameStatusText"]:
            home = game["homeTeam"]["teamName"]
            away = game["awayTeam"]["teamName"]
            print(f"This match between {home} and {away} went overtime")
        else:
            # This else is unnecessary logically, but kept for structure
            print("Error:", response.status_code)
    

    # -------------------------------
    # Find highest scoring game
    # -------------------------------
    highest = 0
    highest_game = None
    
    # Get overall game date (same for all games)
    game_date = data["scoreboard"]["gameDate"]
    
    for game in games:
        homeName = game["homeTeam"]["teamName"]
        awayName = game["awayTeam"]["teamName"]
        
        # Scores from API (should be ints, but sometimes strings in APIs)
        homeScore = game["homeTeam"]["score"]
        awayScore = game["awayTeam"]["score"]
        
        # Total score for the game
        total = homeScore + awayScore
        
        # Update highest score if current game is higher
        if total > highest:
            highest = total
            highest_game = (homeName, awayName)
    
    # Print result
    print(f"The highest scoring game today was: {highest} achieved by {highest_game[0]} and {highest_game[1]} on {game_date}")
    
    
    # -------------------------------
    # Count number of games
    # -------------------------------
    print(len(games))  # counts how many game dictionaries in the list
    

    # -------------------------------
    # Calculate total points per home team using periods
    # -------------------------------
    for game in games:
        total_period_home = 0
        homeName = game["homeTeam"]["teamName"]
        
        # Loop through each period (quarter/OT)
        for p in game["homeTeam"]["periods"]:
            total_period_home += p["score"]
            
        print(f"The total points by home teams is: {total_period_home} by {homeName}")