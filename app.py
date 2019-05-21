from constants import TEAMS, PLAYERS
import copy

player_copy = copy.deepcopy(PLAYERS)
team_copy = copy.deepcopy(TEAMS)


def clean_data(player_copy):
    clean_data_list = []
    for player in player_copy:
        player_dict = {}
        for key, value in player.items():
            if key == 'name':
                dict = {key: value}
                player_dict.update(dict)
            elif key == 'guardians':
                value = value.split(" and ")
                value = ", ".join(value)
                dict = {key: value}
                player_dict.update(dict)
            elif key == 'experience':
                if value == 'YES':
                    value = True
                    dict = {key: value}
                    player_dict.update(dict)
                elif value == 'NO':
                    value = False
                    dict = {key: value}
                    player_dict.update(dict)
            elif key == 'height':
                value = value.split(" ")
                value = value.pop(0)
                value = int(value)
                dict = {key: value}
                player_dict.update(dict)
        clean_data_list.append(player_dict)
    return clean_data_list


def exp(clean_data):
    experienced_players = []
    for player in clean_data:
        for key, value in player.items():
            if key == 'experience' and value == True:
                experienced_players.append(player)
            else:
                continue
    return(experienced_players)


def non_exp(clean_data):
    non_exp_players = []
    for player in clean_data:
        for key, value in player.items():
            if key == 'experience' and value == False:
                non_exp_players.append(player)
            else:
                continue
    return non_exp_players


def build_team(exp, non_exp):
    exp_players = exp
    non_exp_players = non_exp
    panthers = exp_players[:3] + non_exp_players[:3]
    bandits = exp_players[3:6] + non_exp_players[3:6]
    warriors = exp_players[6:] + non_exp_players[6:]
    teams = panthers, bandits, warriors
    return(teams)


def team_stats(stats):
    teams = stats
    players = []
    guardians = []
    height = []
    for dict in teams:
        for x in dict:
            for key, value in x.items():
                if key == 'name':
                    players.append(value)
                if key == 'guardians':
                    guardians.append(value)
                elif key == 'experience':
                    continue
                elif key == 'height':
                    height.append(value)
    player_str = ", ".join(players)
    guardian_str = ", ".join(guardians)
    average_height = (sum(height)) / 6
    return player_str, guardian_str, average_height


if __name__ == '__main__':

    print("BASKETBALL TEAM STATS TOOL\n")

    panther_stats = team_stats(build_team(exp(clean_data(player_copy)), non_exp(clean_data(player_copy)))[:1])
    bandit_stats = team_stats(build_team(exp(clean_data(player_copy)), non_exp(clean_data(player_copy)))[1:2])
    warrior_stats = team_stats(build_team(exp(clean_data(player_copy)), non_exp(clean_data(player_copy)))[2:])

    while True:
            print("----- Main Menu-----\n"
                  "Here are your choices:\n"
                  "1) Display Team Stats\n"
                  "2) Quit\n"
                  )
            menu_choice = input("Enter an option >  ")
            if menu_choice == '1':
                print("\n1) {}\n"
                      "2) {}\n"
                      "3) {}\n\n" .format(team_copy[0], team_copy[1], team_copy[2]))

                stats_choice = input("Pick a team > ")
                if stats_choice == '1':
                    print("\nTeam name: {}\n".format(team_copy[0]))
                    print("Total Players: 6\n\nExperienced Players: 3\n\nInexperienced Players: 3\n")
                    print("Roster: {}\n".format(panther_stats[:1]))
                    print("Guardians: {}\n".format(panther_stats[1:2]))
                    print("Average Height: {}\n".format(panther_stats[2:]))
                    continue
                elif stats_choice == '2':
                    print("\nTeam name: {}\n".format(team_copy[1]))
                    print("Total Players: 6\n\nExperienced Players: 3\n\nInexperienced Players: 3\n")
                    print("Roster: {}\n".format(bandit_stats[:1]))
                    print("Guardians: {}\n".format(bandit_stats[1:2]))
                    print("Average Height: {}\n".format(bandit_stats[2:]))
                    continue
                elif stats_choice == '3':
                    print("\nTeam name: {}\n".format(team_copy[2]))
                    print("Total Players: 6\n\nExperienced Players: 3\n\nInexperienced Players: 3\n")
                    print("Roster: {}\n".format(warrior_stats[:1]))
                    print("Guardians: {}\n".format(warrior_stats[1:2]))
                    print("Average Height: {}\n".format(warrior_stats[2:]))
                    continue
            elif menu_choice == '2':
                break
