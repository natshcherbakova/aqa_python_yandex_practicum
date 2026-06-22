# Временные значения
time = '1h 45m,360s,25m,30m 120s,2h 60s'

# Замена данных и разбиение строки на список
new_times = time.replace('1h', '60').replace('45m', '45').replace('360s', '6').replace('25m', '25').replace('30m', '30').replace('120s', '2').replace('2h', '120').replace('60s', '1').replace(',', ' ').split()

# Подсчет времени
total = 0
if '60' in new_times:
    total += 60
if '45' in new_times:
    total += 45
if '6' in new_times:
    total += 6
if '25' in new_times:
    total += 25
if '30' in new_times:
    total += 30
if '2' in new_times:
    total += 2
if '120' in new_times:
    total += 120
if '1' in new_times:
    total += 1

# Результат с общем кол-во минут
print(total, 'minutes')