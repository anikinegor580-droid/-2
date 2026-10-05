import random

def birthday_probability(people):
    if people > 365:
        return 1
    if people <= 1:
        return 0.0
    res = 1.0
    for i in range(people):
        res *= (365 - i) / 365
    return 1 - res

print(birthday_probability(1))
print(birthday_probability(23))
print(birthday_probability(50))
print(birthday_probability(366))


def simulate_birthday(people, trials):
    hits = 0
    for _ in range(trials):
        days = [random.randint(1, 365) for _ in range(people)]
        if len(set(days)) < people:
            hits += 1
    return hits / trials

print(simulate_birthday(23, 1000))
