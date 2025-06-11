import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
import re
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Scrape roster table from main team page
teams_url = "https://www.basketball-reference.com/teams/PHI/2025.html"
response = requests.get(teams_url)
print("Status code (roster):", response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    roster_table = soup.find("table", id="roster")
    if roster_table:
        roster_df = pd.read_html(io.StringIO(str(roster_table)))[0]
        print("\nPhiladelphia 76ers 2024-25 Roster:")
        print(roster_df[["Player", "Pos", "Ht", "Wt", "Birth Date", "Exp", "College"]])
    else:
        print("Roster table not found.")
else:
    print("Failed to fetch the roster page.")

# 2. Scrape games table from the games page
games_url = "https://www.basketball-reference.com/teams/PHI/2025_games.html"
games_response = requests.get(games_url)
print("Status code (games):", games_response.status_code)

if games_response.status_code == 200:
    games_soup = BeautifulSoup(games_response.text, "lxml")
    games_table = games_soup.find("table", id="games")
    if games_table:
        games_df = pd.read_html(io.StringIO(str(games_table)))[0]
        # Fix multi-level columns if present
        if isinstance(games_df.columns, pd.MultiIndex):
            games_df.columns = games_df.columns.get_level_values(-1)

        # Drop rows where 'G' is not a number (these are header rows repeated in the table)
        games_df = games_df[games_df['G'].apply(lambda x: str(x).isdigit())]
        total_games = len(games_df)
        result_col = 'Unnamed: 7'  # This is the column with 'W' or 'L'
        wins = (games_df[result_col] == 'W').sum()
        losses = (games_df[result_col] == 'L').sum()
        home_games = games_df[games_df['Unnamed: 5'] != '@']
        away_games = games_df[games_df['Unnamed: 5'] == '@']

        # Confirm counts
        print(f"Number of home games: {len(home_games)}")
        print(f"Number of away games: {len(away_games)}")

        home_wins = (home_games[result_col] == 'W').sum()
        away_wins = (away_games[result_col] == 'W').sum()

        print(f"\nPhiladelphia 76ers 2024-25 Season Results:")
        print(f"Total games: {total_games}")
        print(f"Wins: {wins} ({wins/total_games*100:.1f}%)")
        print(f"Losses: {losses} ({losses/total_games*100:.1f}%)")
        print(f"Home record: {home_wins}-{len(home_games)-home_wins} ({home_wins/len(home_games)*100:.1f}% wins)")
        print(f"Away record: {away_wins}-{len(away_games)-away_wins} ({away_wins/len(away_games)*100:.1f}% wins)")

        # --- Team Win/Loss Pie Chart ---
        plt.figure(figsize=(5,5))
        plt.pie([wins, losses], labels=['Wins', 'Losses'], autopct='%1.1f%%', colors=["#002DF7", "#FA0800"])
        plt.title('76ers 2024-25 Wins vs Losses')
        plt.show()

        # --- Home vs Away Bar Chart ---
        plt.figure(figsize=(8,5))
        sns.barplot(
            x=['Home Wins', 'Home Losses', 'Away Wins', 'Away Losses'],
            y=[home_wins, len(home_games)-home_wins, away_wins, len(away_games)-away_wins],
            palette='Purples'
        )
        plt.title('76ers 2024-25 Home/Away Record')
        plt.ylabel('Games')
        plt.tight_layout()
        plt.show()

    else:
        print("Games table not found on the games page.")
else:
    print("Failed to fetch the games page.")

# 3. Scrape depth chart table from the depth chart page
depth_url = "https://www.basketball-reference.com/teams/PHI/2025_depth.html"
depth_response = requests.get(depth_url)
print("Status code (depth chart):", depth_response.status_code)

players, mp, pts, reb, ast, ws = [], [], [], [], [], []

if depth_response.status_code == 200:
    depth_soup = BeautifulSoup(depth_response.text, "lxml")
    tables = depth_soup.find_all("table")
    if tables:
        depth_df = pd.read_html(io.StringIO(str(tables[0])))[0]
        print("\nPhiladelphia 76ers 2024-25 Depth Chart (Player Stats):")
        last_player = None
        for cell in depth_df.iloc[:, 0]:
            # Paste your player stats here (copy from the website and edit as needed)
            test_string = """
            Tyrese Maxey 1960 MP, 26.3 Pts/3.3 Reb/6.1 Ast, 3.8 WS Kyle Lowry 659 MP, 3.9 Pts/1.9 Reb/2.7 Ast, 1.0 WS Jeff Dowtin Jr. 621 MP, 7.0 Pts/1.5 Reb/1.9 Ast, 1.3 WS Reggie Jackson 384 MP, 4.4 Pts/1.4 Reb/1.5 Ast, 0.1 WS Quentin Grimes 943 MP, 21.9 Pts/5.2 Reb/4.5 Ast, 1.6 WS Eric Gordon 768 MP, 6.8 Pts/1.2 Reb/1.7 Ast, 0.9 WS Jared Butler 682 MP, 11.5 Pts/2.5 Reb/4.9 Ast, 0.8 WS Jared McCain 592 MP, 15.3 Pts/2.4 Reb/2.6 Ast, 0.7 WS Lonnie Walker IV 477 MP, 12.4 Pts/3.2 Reb/2.5 Ast, 0.3 WS Jalen Hood-Schifino 301 MP, 7.8 Pts/2.0 Reb/2.8 Ast, -0.1 WS Lester Quinones 17 MP, 2.3 Pts/1.0 Reb/0.3 Ast, -0.1 WS Kelly Oubre Jr. 2078 MP, 15.1 Pts/6.1 Reb/1.8 Ast, 2.6 WS Ricky Council IV 1250 MP, 7.3 Pts/2.9 Reb/1.3 Ast, 0.6 WS Justin Edwards 1155 MP, 10.1 Pts/3.4 Reb/1.6 Ast, 0.9 WS Caleb Martin 943 MP, 9.1 Pts/4.4 Reb/2.2 Ast, 0.6 WS Marcus Bagley 253 MP, 6.7 Pts/7.0 Reb/1.0 Ast, 0.2 WS Oshae Brissett 142 MP, 8.7 Pts/3.7 Reb/0.7 Ast, 0.1 WS Paul George 1334 MP, 16.2 Pts/5.3 Reb/4.3 Ast, 1.0 WS KJ Martin 480 MP, 6.4 Pts/3.0 Reb/0.8 Ast, 1.1 WS Alex Reese 214 MP, 5.3 Pts/3.3 Reb/0.3 Ast, 0.5 WS Chuma Okeke 171 MP, 6.9 Pts/6.1 Reb/1.9 Ast, 0.6 WS Phillip Wheeler 44 MP, 1.6 Pts/1.6 Reb/0.4 Ast, -0.3 WS David Roddy 29 MP, 6.0 Pts/3.0 Reb/1.0 Ast, 0.0 WS Isaiah Mobley 17 MP, 6.0 Pts/4.0 Reb/5.0 Ast, 0.0 WS Guerschon Yabusele 1895 MP, 11.0 Pts/5.6 Reb/2.1 Ast, 3.9 WS Adem Bona 905 MP, 5.8 Pts/4.2 Reb/0.5 Ast, 2.3 WS Andre Drummond 751 MP, 7.3 Pts/7.8 Reb/0.9 Ast, 1.2 WS Joel Embiid 574 MP, 23.8 Pts/8.2 Reb/4.5 Ast, 1.4 WS Colin Castleton 98 MP, 6.0 Pts/7.4 Reb/2.0 Ast, 0.3 WS Pete Nance 68 MP, 2.1 Pts/1.4 Reb/0.4 Ast, 0.0 WS
            """
            pattern = r"([A-Za-z .'\-]+?)\s+(\d+) MP, ([\d\.\-]+) Pts/([\d\.\-]+) Reb/([\d\.\-]+) Ast, ([\d\.\-]+) WS"
            matches = re.findall(pattern, test_string)
            for match in matches:
                player, mp_val, pts_val, reb_val, ast_val, ws_val = match
                players.append(player.strip())
                mp.append(float(mp_val))
                pts.append(float(pts_val))
                reb.append(float(reb_val))
                ast.append(float(ast_val))
                ws.append(float(ws_val))
                print(f"{player:20} | {mp_val:>4} MP | {pts_val:>5} PPG | {reb_val:>5} RPG | {ast_val:>5} APG | {ws_val:>5} WS")
            print("Players:", players)
            print("Points:", pts)
            print("Rebounds:", reb)
            print("Assists:", ast)
            print("Win Shares:", ws)
            print("Lengths:", len(players), len(pts), len(reb), len(ast), len(ws))
        
        # --- Use DataFrame for plotting ---
        df = pd.DataFrame({
            'Player': players,
            'MP': mp,
            'PPG': pts,
            'RPG': reb,
            'APG': ast,
            'WS': ws
        })
        print(df)

        chart_width = max(12, len(df) * 1.2)

        # --- Player Points Per Game Bar Chart ---
        plt.figure(figsize=(chart_width, 6))
        sns.barplot(data=df, x='Player', y='PPG', palette='Reds')
        plt.title('76ers 2024-25 Points Per Game')
        plt.ylabel('PPG')
        plt.ylim(0, 35)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

        # --- Player Rebounds Per Game Bar Chart ---
        plt.figure(figsize=(chart_width, 6))
        sns.barplot(data=df, x='Player', y='RPG', palette='Greens')
        plt.title('76ers 2024-25 Rebounds Per Game')
        plt.ylabel('RPG')
        plt.ylim(0, 15)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

        # --- Player Assists Per Game Bar Chart ---
        plt.figure(figsize=(chart_width, 6))
        sns.barplot(data=df, x='Player', y='APG', palette='Blues')
        plt.title('76ers 2024-25 Assists Per Game')
        plt.ylabel('APG')
        plt.ylim(0, 15)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

        # --- Player Win Shares Bar Chart ---
        plt.figure(figsize=(chart_width, 6))
        sns.barplot(data=df, x='Player', y='WS', palette='Purples')
        plt.title('76ers 2024-25 Win Shares')
        plt.ylabel('WS')
        plt.ylim(0, max(ws) + 2 if ws else 10)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    else:
        print("Depth chart table not found on the page.")
else:
    print("Failed to fetch the depth chart page.")
