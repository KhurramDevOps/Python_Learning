import random

class Game:
    def __init__(self, name, description):  
        self.name = name
        self.description = description

    def get_info(self):
        print(f"Game: {self.name}")
        print(f"Description: {self.description}")

    def start(self):
        self.play()


class HighLow(Game):
    def __init__(self):  
        super().__init__("High Low", "Guess if your number is higher than or lower than the computer's.")

    def play(self):
        self.game()

    def welcome_message(self):
        print("Welcome to the High-Low Game!")
        print("Guess if your number is higher or lower than the computer's.")

    def generate_numbers(self):
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        return player_number, computer_number

    def get_player_guess(self):
        guess = input("Do you think your number is 'higher' or 'lower' than the computer's number? ").strip().lower()
        return guess

    def check_guess(self, player_number, computer_number, guess):
        if guess == "higher":
            return player_number > computer_number
        elif guess == "lower":
            return player_number < computer_number
        else:
            print("Invalid guess. Please enter 'higher' or 'lower'.")
            return None

    def play_round(self):
        player_number, computer_number = self.generate_numbers()
        print(f"\nYour number is: {player_number}")
        guess = self.get_player_guess()

        is_correct = self.check_guess(player_number, computer_number, guess)
        if is_correct is None:
            print("Invalid guess. Try again.")
            return False
        elif is_correct:
            print("Correct guess! You scored a point.")
            return True
        else:
            print("Incorrect guess.")
            print(f"The computer's number was: {computer_number}")
            return False

    def game(self):
        rounds = 5
        score = 0
        self.welcome_message()

        for round_num in range(1, rounds + 1):
            print(f"\nRound {round_num}")
            if self.play_round():
                score += 1

        print("\nGame Over!")
        print(f"Your final score is: {score} out of {rounds}")
        if score > rounds / 2:
            print("Congratulations, you won!")
        else:
            print("Better luck next time!")


class NumberGuess(Game):
    def __init__(self):  
        super().__init__("Number Guess", "Guessing the computer's number")

    def play(self):
        secret_number = random.randint(1, 99)
        print("I am thinking of a number between 1 and 99...")

        while True:
            guess = int(input("Enter a guess: "))
            if guess == secret_number:
                print("Congratulations! You guessed the number.")
                break
            elif guess < secret_number:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")


class GameEngine:
    def __init__(self):  
        self.games = []  

    def add_game(self, game):
        self.games.append(game)

    def menu(self):
        print("Available Games:")
        for i, game in enumerate(self.games, 1):
            print(f"{i}. {game.name}: {game.description}")

        while True:
            choice = input("Enter the number of the game you want to play (or 'q' to quit): ")
            if choice == 'q':
                break

            try:
                choice = int(choice)
                if 1 <= choice <= len(self.games):
                    self.games[choice - 1].start()  # Call the start method of the chosen game
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


# Create the game engine and add games
game_engine = GameEngine()  
game_engine.add_game(HighLow())  
game_engine.add_game(NumberGuess()) 

# Run the menu
game_engine.menu()