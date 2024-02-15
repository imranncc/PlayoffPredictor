import math
from Team import Team

#Part A - 1

def calculate_resistance(is_series, resistances): #Function 1

    if len(resistances) <= 1:
        return "NA"

    if is_series:
        result = sum(resistances)
        connection = "series"
    else:
        reciprocal_sum = sum([1/r for r in resistances])
        result = round(1/reciprocal_sum, 8)
        connection = "parallel"

    print(f"Resistors used: {resistances}")
    print(f"Resistance in {connection}: {result}")

    return result

#Part A - 2

def compound_interest(principal, periods, interest_rate): #Function 2

    total = round(principal * (1 + interest_rate) ** periods, 2)

    print("\nCalculated Interest")
    print("Principal:", principal)
    print("Periods:", periods)
    print("Rate:", interest_rate)
    print("After Interest:", total)
    
    return total

#Part B

def permutations(wins, losses):
    p = wins + losses
    perms = math.factorial(p) / (math.factorial(wins) * math.factorial(losses))
    return perms

def series(team1, team2):

    game_num = 0
    t1_wins = 0
    t2_wins = 0
    t1_goals = 0
    t2_goals = 0

    while True:

        game_num += 1
        home_team = team1 if game_num in [1, 2, 5, 7] else team2
        away_team = team2 if game_num in [1, 2, 5, 7] else team1
        home_goals = int((home_team.get_goals_for() + away_team.get_goals_against()) / (2 * away_team.get_save_percentage() * 82))
        away_goals = int((away_team.get_goals_for() + home_team.get_goals_against()) / (2 * home_team.get_save_percentage() * 82))

        if home_team == team1:
            t1_goals += home_goals
            t2_goals += away_goals
        else:
            t1_goals += away_goals
            t2_goals += home_goals

        print("TEST")
        
        if home_goals > away_goals:
            if home_team == team1:
                t1_wins += 1
            else:
                t2_wins += 1
        elif away_goals > home_goals:
            if home_team == team1:
                t2_wins += 1
            else:
                t1_wins += 1

        if t1_wins ==4 or t2_wins == 4:
            break
        
    winner = team1 if t1_wins >= 4 else team2
    loser = team2 if t1_wins >= 4 else team1
    num_perms = permutations(4, 3)

    print(winner.get_name(),loser.get_name(),t1_wins,t2_wins,num_perms,t1_goals,t2_goals)

    return [winner.get_name(), loser.get_name(), t1_wins, t2_wins, num_perms, t1_goals, t2_goals]


def main():
    
    toronto = Team("Toronto Maple Leafs", 4, 312,252, .897)
    tampa = Team("Tampa Bay Lightning", 8, 285,228, .915)
    
    # Call the series function with the two teams and assign the return value to the winner variable
    winner = series(toronto, tampa)
    
    # Print results
    print("The winning team is the", winner[0])
    print("The", winner[0], "won the series", winner[2], "games to", winner[3], "games!")
    print("The total number of ways that", winner[0], "could have won the series is", winner[4], "ways!")
    print(winner[0], "scored", winner[5], "total goals,", winner[1], "scored", winner[6], "total goals!")

main()
