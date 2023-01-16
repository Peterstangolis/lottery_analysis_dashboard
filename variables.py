
data_url = 'https://github.com/Peterstangolis/lottery_tracking_dashboard/blob/main/data/keno_lottery_analysis.csv?raw=true'

numbers_url = 'https://github.com/Peterstangolis/lottery_tracking_dashboard/blob/main/data/lottery_number_occurrences.csv?raw=true'


keno_combinations = list(range(1,71))

keno_odds = {
    '2' : [7.87, 12.7],
    '3' : [2.08, 48.0],
    '4' : [0.53, 189.3],
    '5' : [0.13, 780.6],
    '6' : [0.03, 3382.8],
    '7' : [0.0065, 15464.1],
    '8' : ['0.00133', 74941.3],
    '9' : ['0.00026', 387196.5],
    '10' : ['0.000047', 2147180.7]
}

def list_conversion(l):
    if isinstance(l, int):
            return l
    else:
        new_list = []
        l2 = l.split(',')
        for item in l2:
            i = item.replace('[','').replace(']','').strip()
            if not i:
                i = i
            else:
                try:
                    i = int(i)
                except:
                    i = float(i)
            new_list.append(i)
        return new_list


numbers_breakdown = {
    "ODD_1_19": [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],
    "EVEN_2_18": [2, 4, 6, 8, 10, 12, 14, 16, 18],
    "ODD_21_35": [21, 23, 25, 27, 29, 31, 33, 35],
    "EVEN_20_34": [20, 22, 24, 26, 28, 30, 32, 34],
    "ODD_37_51": [37, 39, 41, 43, 45, 47, 49, 51],
    "EVEN_36_52": [36, 38, 40, 42, 44, 46, 48, 50, 52],
    "ODD_53_69": [53, 55, 57, 59, 61, 63, 65, 67, 69],
    "EVEN_54_70": [54, 56, 58, 60, 62, 64, 66, 68, 70]
}





