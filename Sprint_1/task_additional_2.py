def digit_root(num):
    total = 0
    for digit in str(num):
        total += int(digit)

    if total < 10:
        return total
    return digit_root(total)

print(digit_root(4851))
print(digit_root(97569))
print(digit_root(889987))