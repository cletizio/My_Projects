# Roster

import random

class Roster:
    def __init__(self):
         self.players = []

    def add_player(self):
        name = input('Enter the players name:')
        self.players.append(name)
        print('Player added to roster!')

    def print_roster(self):
        print(self.players)

def create_defensive_lineup(roster):
    positions = ["pitcher", "catcher", "first base", "second base", "shortstop", "third base", "left field", "center field", "right field"]
    lineup = []
    players_assigned = []

    for player in range(len(roster.players)):
        available_players = [player for player in roster.players if player not in players_assigned]
        player = random.choice(available_players)
        position = random.choice(positions)
        player_position_dict = {player: position}
        lineup.append(player_position_dict)
        positions.remove(position)
        players_assigned.append(player)

    return lineup

def main ():
    quit = 0
    inning = 1
    roster = Roster()
    
    while quit != 1:
        roster.add_player()
        quit = int(input('Are you done adding players? (1=Yes 0=No)'))

    while inning < 8:
        lineup = create_defensive_lineup(roster)
        print('Inning #', inning)
        for i, player_position_dict in enumerate(lineup, start=1):
            player, position = list(player_position_dict.items())[0]
            print(f"{i}. {position.capitalize()}: {player}")
        inning += 1
    

if __name__ == "__main__":
    main()