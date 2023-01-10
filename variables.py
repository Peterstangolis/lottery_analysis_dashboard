
data_url = 'https://github.com/Peterstangolis/lottery_tracking_dashboard/blob/main/data/keno_lottery_analysis.csv?raw=true'

numbers_url = 'https://github.com/Peterstangolis/lottery_tracking_dashboard/blob/main/data/lottery_number_occurrences.csv?raw=true'


keno_combinations = list(range(1,71))

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




