from minesweeper import *
from menu import *
import json
import os

def load_saved_games():
    saved_game_data = []
    if os.path.exists('saved_games.json'):
        with open('saved_games.json', 'r') as file:
            saved_game_data = json.load(file)
    return saved_game_data

def display_saved_games(saved_game_data):
    print("Saved Games:")
    for i, game in enumerate(saved_game_data, start=1):
        print(f"{i}. {game['name']}")
    selected_game_i = abs(int(input("Select a game to load (enter the corresponding number): "))) - 1
    selected_game = saved_game_data[selected_game_i]
    load_saved_games(selected_game)

def savedGames():
    saved_game_data = load_saved_games()
    display_saved_games(saved_game_data)

def calculate_game_statistics(saved_game_data):
    total_games_played = len(saved_game_data)
    games_won = 0
    games_lost = 0
    total_cells_opened = 0

    for game in saved_game_data:
        if game['game_won']:
            games_won += 1
        else:
            games_lost += 1
        total_cells_opened += game['cells_opened']

    average_cells_opened = total_cells_opened / total_games_played if total_games_played > 0 else 0

    game_stats = {
        'total_games_played': total_games_played,
        'games_won': games_won,
        'games_lost': games_lost,
        'average_cells_opened': average_cells_opened
    }

    return game_stats

def display_game_statistics(game_stats):
    print("Game Statistics:")
    print(f"Total Games Played: {game_stats['total_games_played']}")
    print(f"Games Won: {game_stats['games_won']}")
    print(f"Games Lost: {game_stats['games_lost']}")
    print(f"Average Cells Opened: {int(game_stats['average_cells_opened'])}")

def gameStatistics():
    game_stats = calculate_game_statistics()
    display_game_statistics(game_stats)


def check_earned_achievements():
#     earned_achievements = []
#
#     if player_opened_cells_in_row >= 10:
#         earned_achievements.append("Opened 10 Cells in a Row")
#
#     if player_won_game:
#         earned_achievements.append("Won a Game")
#
#     if total_cells_opened >= 100:
#         earned_achievements.append("Explored 100 Cells")
#
#     if total_bombs_defused >= 50:
#         earned_achievements.append("Defused 50 Bombs")
#
#     if total_games_played >= 25:
#         earned_achievements.append("Played 25 Games")
#
#     if total_cells_opened >= 500:
#         earned_achievements.append("Explored 500 Cells")
#
#     if total_bombs_defused >= 100:
#         earned_achievements.append("Defused 100 Bombs")
#
#     if total_games_played >= 50:
#         earned_achievements.append("Played 50 Games")
#
#     if total_cells_opened >= 1000:
#         earned_achievements.append("Explored 1000 Cells")
#
#     if total_bombs_defused >= 200:
#         earned_achievements.append("Defused 200 Bombs")
#
#     if total_games_played >= 100:
#         earned_achievements.append("Played 100 Games")
#
#     if player_won_game and total_cells_opened >= 200:
#         earned_achievements.append("Victory Explorer")
#
#     if total_games_played >= 200 and total_bombs_defused >= 150:
#         earned_achievements.append("Master Sweeper")
#
#     if player_opened_cells_in_row >= 20:
#         earned_achievements.append("Opened 20 Cells in a Row")
#
#     if player_won_game and total_bombs_defused >= 75:
#         earned_achievements.append("Safe and Sound")
#
#     if total_games_played >= 150 and player_won_game:
#         earned_achievements.append("Game Conqueror")
#
#     if player_won_game and total_games_played >= 75:
#         earned_achievements.append("Persistent Victor")
#
#     if total_cells_opened >= 2000:
#         earned_achievements.append("Explored 2000 Cells")
#
#     if total_games_played >= 500:
#         earned_achievements.append("Played 500 Games")
#
#     return earned_achievements

    pass

def display_achievements(earned_achievements):
    print("Earned Achievements:")
    if earned_achievements:
        for index, achievement in enumerate(earned_achievements, start=1):
            print(f"{index}. {achievement}")
    else:
        print("No achievements earned yet.")

    input("Press Enter to continue...")

def achievements():
    earned_achievements = check_earned_achievements()
    display_achievements(earned_achievements)


def exitGame():
    print("Exiting the game...")
    exit()


def mainMenu():
    global LVL
    while True:
        print("Main menu ->")
        printMenuLvl()

        option = input("Choose  -> ")
        if option.lower() == directions[0] and current_pos >= min_pos:
            current_pos -= 1
        elif option.lower() == directions[1] and current_pos <= max_pos:
            current_pos += 1
        elif option == '':
            if current_pos == 0:
                startGame(LVL)
            elif current_pos == 1:
                savedGames()
            elif current_pos == 2:
                gameStatistics()
            elif current_pos == 3:
                achievements()
            elif current_pos == 4:
                exitGame()

        if current_pos > max_pos:
            current_pos = max_pos
        elif current_pos < min_pos:
            current_pos = min_pos

if __name__ == '__main__':
    LVL = menuChooseLvl()
    startGame(LVL)
