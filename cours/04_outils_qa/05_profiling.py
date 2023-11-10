import cProfile
def fonction_lente():
    total = 0
    for i in range(100000000):
        total += i
    return total

def fonction_rapide():
    return sum(range(100000000))

def main():
    fonction_rapide()
    fonction_lente()

cProfile.run('main()')