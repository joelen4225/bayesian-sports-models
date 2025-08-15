def main():
    # Prior probability driver will finish in the top 10
    P_B = 0.25

    # Prob of great qualifying lap time given T10 finish
    P_A_given_B = 0.8

    # Probability of great qualifying lap time
    P_A = 0.3

    # Applying Bayes' Rule
    P_B_given_A = (P_A_given_B * P_B) / P_A
    print("Probability of T10 finish given great qualifying lap time: ", P_B_given_A)  

if __name__ == "__main__":
    main()
    