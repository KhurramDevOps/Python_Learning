import random

class Game:
    def __init__(self, name: str, description: str) -> None:  
        self.name: str = name
        self.description: str = description

    def get_info(self) -> None:
        print(f"Game: {self.name}")
        print(f"Description: {self.description}")

    def start(self) -> None:
        self.play()

    def play(self) -> None:
        raise NotImplementedError("Subclasses must implement this method.")


class HighLow(Game):
    def __init__(self) -> None:  
        super().__init__("High Low", "Guess if your number is higher than or lower than the computer's.")

    def play(self) -> None:
        self.game()

    def welcome_message(self) -> None:
        print("Welcome to the High-Low Game!")
        print("Guess if your number is higher or lower than the computer's.")

    def generate_numbers(self) -> tuple[int, int]:
        player_number: int = random.randint(1, 100)
        computer_number: int = random.randint(1, 100)
        return player_number, computer_number

    def get_player_guess(self) -> str:
        while True:
            guess: str = input("Do you think your number is 'higher' or 'lower' than the computer's number? ").strip().lower()
            if guess in ["higher", "lower"]:
                return guess
            print("Invalid input. Please enter 'higher' or 'lower'.")

    def check_guess(self, player_number: int, computer_number: int, guess: str) -> bool:
        if guess == "higher":
            return player_number > computer_number
        elif guess == "lower":
            return player_number < computer_number

    def play_round(self) -> bool:
        player_number, computer_number = self.generate_numbers()
        print(f"\nYour number is: {player_number}")
        guess: str = self.get_player_guess()

        is_correct: bool = self.check_guess(player_number, computer_number, guess)
        if is_correct:
            print("Correct guess! You scored a point.")
            return True
        else:
            print("Incorrect guess.")
            print(f"The computer's number was: {computer_number}")
            return False

    def game(self) -> None:
        rounds: int = 5
        score: int = 0
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
    def __init__(self) -> None:  
        super().__init__("Number Guess", "Guessing the computer's number")

    def play(self) -> None:
        secret_number: int = random.randint(1, 99)
        print("I am thinking of a number between 1 and 99...")

        while True:
            try:
                guess: int = int(input("Enter a guess: "))
                if 1 <= guess <= 99:
                    if guess == secret_number:
                        print("Congratulations! You guessed the number.")
                        break
                    elif guess < secret_number:
                        print("Your guess is too low.")
                    else:
                        print("Your guess is too high.")
                else:
                    print("Please enter a number between 1 and 99.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")


class GameEngine:
    def __init__(self) -> None:  
        self.games: list[Game] = []  

    def add_game(self, game: Game) -> None:
        self.games.append(game)

    def menu(self) -> None:
        print("Available Games:")
        for i, game in enumerate(self.games, 1):
            print(f"{i}. {game.name}: {game.description}")

        while True:
            choice = input("Enter the number of the game you want to play (or 'q' to quit): ")
            if choice.strip().lower() == 'q':
                break

            try:
                choice: int = int(choice)
                if 1 <= choice <= len(self.games):
                    self.games[choice - 1].start()  # Call the start method of the chosen game
                else:
                    print("Invalid choice. Please enter a valid game number.")
            except ValueError:
                print("Invalid input. Please enter a number.")


# Create the game engine and add games
game_engine: GameEngine = GameEngine()  
game_engine.add_game(HighLow())  
game_engine.add_game(NumberGuess()) 

# Run the menu
game_engine.menu()
