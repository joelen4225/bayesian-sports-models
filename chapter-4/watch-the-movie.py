def main():
    # Prior probability we will enjoy the movie
    P_B = 0.3

    # Prob movie is rted high given it's worth watching
    P_A_given_B = 0.9

    # Probability that a movie is rated highly
    P_A = 0.5

    # Applying Bayes' Rule
    P_B_given_A = (P_A_given_B * P_B) / P_A
    print("Probability that a movie is worth watching given it's rated highly: ", P_B_given_A)

if __name__ == "__main__":
    main()
    
