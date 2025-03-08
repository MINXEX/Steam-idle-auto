# **Steam Idle Batch File Generator** 🎮💻

## **Overview** 🌟
A Python script that generates a batch file to idle all games in your Steam library using `steam-idle.exe`. Just input your Steam API key and Steam ID, and the script will create a `.bat` file with commands to open all your games sequentially.

## **Features** 🔥
- Automatically fetches all games from your Steam library. 📂
- Creates a `.bat` file to idle games using `steam-idle.exe`. 📝
- Easy setup with customizable Steam API key and ID. ⚙️

## **Installation** 🛠️

1. **Install Python**: Make sure Python 3.x is installed on your system. 🐍
2. **Install Dependencies**: Install the `requests` library by running:
    ```bash
    pip install requests
    ```

3. **Configure API Key and Steam ID**:
    - Replace `'your_api_key_here'` in the script with your [Steam Web API key](https://steamcommunity.com/dev/apikey). 🔑
    - Replace `'your_steam_id_here'` with your 64-bit Steam ID (you can use a Steam ID converter to find it). 🆔

4. **Install Steam Idle Master Extended**: To idle your games, you'll need [Steam Idle Master Extended](https://github.com/JonasNilson/idle_master_extended/releases). Follow the instructions on the GitHub page to download and set it up. 🔧

5. **Run the Script**:
    ```bash
    python steam_idle.py
    ```

6. **Execute the Generated Batch File**: The script will generate a `.bat` file named `steam_idle_commands.bat`. Simply run this batch file to idle all your Steam games. 🎮

## **Example Output** 💡
The generated `.bat` file will contain lines like:
```batch
start steam-idle.exe 620
start steam-idle.exe 815370
start steam-idle.exe 431960
