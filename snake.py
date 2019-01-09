import itertools
snake_numbers = [[8.0,3.0,4.0,5.0],[1.0,4.0,2.0,3.0],[6.0,2.0,3.0,9.0],[4.0,4.0,2.0,6.0]]
answers = [7.0,6.0,1.0,5.0]
operators = ["x", '/', '+', '-']
combinations = itertools.product(*snake_numbers)
operator_combos = list(itertools.product(operators, repeat=3))

def do_operation(string, num1, num2):
    if string is 'x':
        return num1*num2
    if string is "/":
        return num1/num2
    if string is '+':
        return num1+num2
    else:
        return num1-num2

def get_value(operations, num_list):
    a = num_list[0]
    b = num_list[1]
    c = num_list[2]
    d = num_list[3]
    value = 0
    if operations[0] is 'x' or operations[0] is '/':
        value += do_operation(operations[0], a, b)
        if operations[1] is 'x' or operations[1] is '/':
            value += do_operation(operations[1], value, c)
            value += do_operation(operations[2], value, d)
        else:
            if operations[2] is 'x' or operations[2] is '/':
                value2 = do_operation(operations[2], c, d)
                value += do_operation(operations[1], value, value2)
            else:
                value += do_operation(operations[1], value, c)
                value += do_operation(operations[2], value, d)

    else:
        if operations[1] is 'x' or operations[1] is '/':
            value += do_operation(operations[1], b, c)
            if operations[2] is 'x' or operations[2] is '/':
                value += do_operation(operations[2], value, d)
            else:
                value += do_operation(operations[0], a, value)
                value += do_operation(operations[2], value, d)
        else:
            if operations[2] is 'x' or operations[2] is '/':
                value += do_operation(operations[2], c, d)
                value += do_operation(operations[1], b, value)
                value += do_operation(operations[0], a, value)
    print(f'calculating: {a}{operations[0]}{b}{operations[1]}{c}{operations[2]}{d} = {value}')
    return value



for combo in combinations:
    for answer in answers:
        for operation_list in operator_combos:
            if answer is get_value(operation_list, combo):
                print(f'{combo[0]}{operation_list[0]}{combo[1]}{operation_list[1]}{combo[2]}{operation_list[2]}{combo[3]} = {answer}')
            


    