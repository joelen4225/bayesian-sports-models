def main():
    # Prior probability that the team will win
    P_B = 0.5

    # Prob of winning given backup goalie starts
    P_A_given_B = 0.38

    # Probability that the backup goalie starts
    P_A = 0.4

    # Applying Bayes' Rule
    P_B_given_A = (P_A_given_B * P_B) / P_A
    print("Probability that the team will win given the backup goalie starts: ", P_B_given_A)

if __name__ == "__main__":
    main()