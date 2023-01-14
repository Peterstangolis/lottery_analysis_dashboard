
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




