time = '1h 45m,360s,25m,30m 120s,2h 60s'

new_times = time.replace(',', ' ').split()

total = 0

for item in new_times:

    if 'h' in item:
        total += int(item.replace('h', ' ')) * 60
        
    elif 'm' in item:
        total += int(item.replace('m', ' '))

    elif 's' in item:
        total += int(item.replace('s', ' ')) / 60

print(total, 'minutes')