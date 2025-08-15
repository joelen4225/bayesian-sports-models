# Example: Probability of MVP award going to a player from any team
def main():
    P_team_A_wins = 0.30
    P_team_B_wins = 0.20
    P_team_C_wins = 0.5
    P_MVP_given_team_A = 0.1
    P_MVP_given_team_B = 0.15
    P_MVP_given_team_C = 0.05
    P_MVP = (P_team_A_wins * P_MVP_given_team_A) + (P_team_B_wins * P_MVP_given_team_B) + (P_team_C_wins * P_MVP_given_team_C)
    print("Probability of MVP award going to a player from any team: ", P_MVP)

if __name__ == "__main__":
    main()
    