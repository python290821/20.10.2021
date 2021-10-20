

# 1
# installed ...

# 2
def print_1_100():
    for i in range(1, 100 + 1):
        print(i)

# 3
def print_1_x(x = 10):
    for i in range(1, x + 1):
        print(i, end=' ')

print_1_100();
print_1_x(); # will print 1-10
#print()
#print_1_x(3) # will print 1-3

## guess game
import random

def random_game():
    best_score = 0
    for i in range(3):
        lucky = random.randint(1, 2)
        guess_count = 0
        while True:
            guess_count += 1
            cur_guess = int(input(f'{guess_count} please guess the number: '))
            if cur_guess == lucky:
                print('Bingo! ')
                print(f'it took you {guess_count} guesses')
                break
            if cur_guess > lucky:  # you may also go with elif...
                print('guess lower...')
                continue
            # you may also do: elif cur_guess < lucky:
            else:
                print('guess higher...')
        # after game
        if best_score == 0 or cur_guess < best_score:
            best_score = cur_guess
        print(f'your best score is: {best_score}')

random_game()



