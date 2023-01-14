

def odds_calc(n):

    from itertools import combinations
    from variables import keno_combinations

    combinations_70 = list(combinations(list(range(1, 71)), n))
    combinations_20 = list(combinations(list(range(1,21)), n))


    prob = round((len(combinations_20) / len(combinations_70)) * 100, 5)
    odds = f"1 in {round(len(combinations_70)/ len(combinations_20), 1)}"

    return prob, odds

