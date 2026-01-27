time = '1h 45m,360s,25m,30m 120s,2h 60s'

time_values = time.split(',')

total_minutes = 0

for time_2 in time_values:

    parts = time_2.split()
    
    for i in parts:
        if 'h' in i:
            hours = int(i.replace('h', ''))
            total_minutes += hours * 60
        elif 'm' in i:
            minutes = int(i.replace('m', ''))
            total_minutes += minutes
        elif 's' in i:
            seconds = int(i.replace('s', ''))
            total_minutes += seconds // 60

print('Общее количество минут:', total_minutes)