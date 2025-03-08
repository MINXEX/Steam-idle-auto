import requests

# put your steam api key in here
api_key = 'your key here'

# your Steam ID here. you can find your steam id
steam_id = 'your steam id here'

url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={api_key}&steamid={steam_id}&format=json"

response = requests.get(url)

if response.status_code == 200:
    try:
        
        data = response.json()

        
        with open("steam_idle_commands.bat", "w") as bat_file:
            
            bat_file.write("@echo off\n\n")

            # Extract game details
            if "response" in data and "games" in data["response"]:
                for game in data["response"]["games"]:
                    game_id = str(game["appid"])
                    
                    bat_file.write(f"start steam-idle.exe {game_id}\n")

        print("Batch file 'steam_idle_commands.bat' created successfully!")
    except ValueError:
        print("Failed to decode JSON response.")
else:
    print(f"Error: Received status code {response.status_code}")
    print("Please check your API key and Steam ID.")
