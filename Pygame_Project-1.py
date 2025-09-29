import random

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return float('inf')
    return x / y

ops = {'+': add, '-': sub, '*': mul, '/': div}

def draw_cards():
    numbers = []
    for i in range(4):
        numbers.append(random.randint(1, 10))
    symbols = []
    for i in range(3):
        symbols.append(random.choice(['+', '-', '*', '/']))
    return numbers, symbols

def calculate_result(numbers, symbols):
    tokens = []
    for i in range(4):
        tokens.append(numbers[i])
        if i < 3:
            tokens.append(symbols[i])
    
    i = 1
    while i < len(tokens):
        if tokens[i] == '*' or tokens[i] == '/':
            if tokens[i] == '*':
                result = tokens[i-1] * tokens[i+1]
            else:
                if tokens[i+1] == 0:
                    result = float('inf')
                else:
                    result = tokens[i-1] / tokens[i+1]
            tokens[i-1:i+2] = [result]
        else:
            i += 2
    
    i = 1
    while i < len(tokens):
        if tokens[i] == '+' or tokens[i] == '-':
            if tokens[i] == '+':
                result = tokens[i-1] + tokens[i+1]
            else:
                result = tokens[i-1] - tokens[i+1]
            tokens[i-1:i+2] = [result]
        else:
            i += 2
    
    return round(tokens[0], 2)

def get_input(prompt):
    while True:
        val = input(prompt).strip().lower()
        if val == 'skip':
            return None
        try:
            return round(float(val), 2) 
        except:
            print("Please enter a number or 'skip'.")

def get_bet():
    while True:
        bet = input("Bet 'small' or 'big': ").strip().lower()
        if bet == 'small' or bet == 'big':
            return bet
        print("Invalid, try again.")


def sep():
    print("\n" + "-"*30 + "\n")

def play_round():
    numbers_big, symbols_big = draw_cards()
    numbers_small, symbols_small = draw_cards()

    sep()
    print("Goal: Big -> 20, Small -> 1")
    print("Big set:", numbers_big, "Operators:", symbols_big)
    print("Small set:", numbers_small, "Operators:", symbols_small)
    sep()

    big_input = get_input("Your result for big set (or 'skip'): ")
    small_input = get_input("Your result for small set (or 'skip'): ")
    bet = get_bet()
    sep()

    big_true = calculate_result(numbers_big, symbols_big)
    small_true = calculate_result(numbers_small, symbols_small)

    print("System results:")
    print("Big:", big_true)
    print("Small:", small_true)
    sep()

    if abs(big_true - 20) < abs(small_true - 1):
        correct = 'big'
    else:
        correct = 'small'
    print("Correct bet:", correct)
    sep()

    threshold = 3
 
    too_far = False
    if big_input is not None and abs(big_true - big_input) > threshold:
        too_far = True
    if small_input is not None and abs(small_true - small_input) > threshold:
        too_far = True


    if too_far:
        print("No")
        return False
    else:
        if bet == correct:
            print("You win!")
            return True
        else:
            print("You lose!")
            return False

def main():
    score = 0
    rounds = 0
    while True:
        rounds += 1
        print("\n=== Round", rounds, "===")
        if play_round():
            score += 1
        print("Score:", score, "/", rounds)
        again = input("Play again? yes/no: ").strip().lower()
        if again != 'yes':
            print("Final score:", score, "/", rounds, "Goodbye!")
            break

main()
