# Example: Probability that a game is postponed given that it rains
def main():
    P_rain = 0.40
    P_posponed = 0.25
    P_rain_postponed = 0.1
    P_postponed_given_rain = P_rain_postponed / P_rain
    print("Probability that a game is postponed given that it rains: ", P_postponed_given_rain)

if __name__ == "__main__":
    main()
    