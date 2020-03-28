while True:
    try:
        line = input('please enter operands')
        # operand = line.split(',')
        operand = line
        print(int(operand[0]) + int(operand[1]))
    except:
        break