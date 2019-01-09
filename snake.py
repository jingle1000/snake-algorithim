import itertools
snake_numbers = [[8,3,4,5],[1,4,2,3],[6,2,3,9],[4,4,2,6]]
answers = [7,6,1,5]
operators = ["x", '/', '+', '-']
combinations = itertools.product(*snake_numbers)

for combo in combinations:
    for answer in answers:
        a = combo[0]
        b = combo[1]
        c = combo[2]
        d = combo[3]
        if a*b*c*d is answer:
            print(f'{a}{b}{c}{d}')
        if a*b*c/d is answer:
            print(f'{a}{b}{c}{d}')
        if (a*b*c)+d is answer:
            print(f'{a}{b}{c}{d}')
        if (a*b*c)-d is answer:
            print(f'{a}{b}{c}{d}')
        if a*b/c*d is answer:
            print(f'{a}{b}{c}{d}')
        if a*b/c/d is answer:
            print(f'{a}{b}{c}{d}')
        if (a*b/c)+d is answer:
            print(f'{a}{b}{c}{d}')
        else:
            pass #modify code from here


    