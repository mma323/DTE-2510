import random as rdm

def roll_pair_of_six_sided_dice():
    dice_1 = rdm.randint(1, 6)
    dice_2 = rdm.randint(1, 6)
    total = dice_1 + dice_2
    return total

def main():
    AMOUNT_OF_ROLLS = 1000
    POSSIBLE_OUTCOMES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    PROBABILITIES = (
        [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
    )

    totals = []
    for i in range(AMOUNT_OF_ROLLS):
        total = roll_pair_of_six_sided_dice()
        totals.append(total)
    
    print("Total Simulated Expected")
    print("       Percent Percent")
    for i in range( len(POSSIBLE_OUTCOMES) ):
        outcome_count = totals.count(POSSIBLE_OUTCOMES[i])
        expected_percentage = PROBABILITIES[i] * 100
        outcome_percentage = (outcome_count / AMOUNT_OF_ROLLS) * 100
        print(
            f"{POSSIBLE_OUTCOMES[i]:3} " +
            f"{outcome_percentage:10.2f} " +
            f"{expected_percentage:5.2f}"
            )

if __name__ == "__main__":
    main()
