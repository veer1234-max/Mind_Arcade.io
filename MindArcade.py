import random
import string
import time 


def coderunner():
    print("🎮 Welcome to the Mind Arcade! 🎮\n\nChoose an activity from the menu below:\n"
      "1. 🔢 Guess the Number Game\n"
      "2. 🔐 Random Password Generator\n"
      "3. ✊🖐✌ Rock, Paper, Scissors (vs. the Computer)\n"
      "4. ⏳ Timed Math Quiz\n"
      "5. 🔤 Hangman Game\n\n"
      "Simply press the number corresponding to the game you want to play and have fun! 😄")
    Choice = int(input("Enter your choice in numbers: "))
    if Choice==1:
        target=random.randint(1, 100)
        while True:
            userchoice = input("Guess the target or Quit(Q): ")
            if (userchoice=="Quit"):
                break
            userchoice=int(userchoice)
            if(userchoice == target):
                print("Success: Correct Guess!!")
                break
            elif(userchoice<target):
                print("The number was too small. Take a bigger guess....")
            else:
                print("The number was too big. Take a smaller  guesss....")    
        print("-----------GAME OVER-----------")
      

    elif Choice==2:
        pass_len=12
        characterValues=string.punctuation+string.digits+string.ascii_letters
        password=""
        for i in range(pass_len):
            password+=(random.choice(characterValues))
        print("Your random password is:",password)

    elif Choice==3: 
        def play():
            user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
            computer = random.choice(['r', 'p', 's'])
            if user == computer:
                return 'It\'s a tie'
        # r > s, s > p, p > r
            if is_win(user, computer):
                return 'You won!'
            return 'You lost!'
        def is_win(player, opponent):
        # return true if player wins
        # # r > s, s > p, p > r
            if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
                or (player == 'p' and opponent == 'r'):
                return True
        print(play())
       

    elif Choice==4: 
        OPERATORS = ["+", "-", "*"]
        MIN_OPERAND = 3
        MAX_OPERAND = 12
        TOTAL_PROBLEMS = 10
        def generate_problem():
            left = random.randint(MIN_OPERAND, MAX_OPERAND)
            right = random.randint(MIN_OPERAND, MAX_OPERAND)
            operator = random.choice(OPERATORS)
            expr = str(left) + " " + operator + " " + str(right)
            answer = eval(expr)
            return expr, answer
        wrong = 0
        input("Press enter to start!")
        print("----------------------")
        start_time = time.time()
        for i in range(TOTAL_PROBLEMS):
            expr, answer = generate_problem()
            while True:
                guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
                if guess == str(answer):
                    break
                wrong += 1
        end_time = time.time()
        total_time = round(end_time - start_time, 2)
        print("----------------------")
        print("Nice work! You finished in", total_time, "seconds!")

    elif Choice==5:
    # List of words to guess
        words = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift']
        chosen_word = random.choice(words)
        word_display = ['_' for _ in chosen_word]  # Create a list of underscores
        attempts = 8  # Number of allowed attempts
        print("Welcome to Hangman!")
        while attempts > 0 and '_' in word_display:
            print("\n" + ' '.join(word_display))
            guess = input("Guess a letter: ").lower()
            if guess in chosen_word:
                for index, letter in enumerate(chosen_word):
                    if letter == guess:
                        word_display[index] = guess  # Reveal the letter
            else:
                print("That letter doesn't appear in the word.")
                attempts -= 1
        if '_' not in word_display:
            print("You guessed the word!")
            print(' '.join(word_display))
            print("You survived!")
        else:
            print("You ran out of attempts. The word was: " + chosen_word)
            print("You lost!")

    else:
        print("Invalid Choice")

while True:
    men=input("Do you want to continue or quit\nPress y for continue and n for exit")
    if men=='y':
        coderunner()
    else:
        break 
             




