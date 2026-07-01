class Player:

    def __init__(self, name, score, level):
        self.name = name
        self.score = score
        self.level = level

    def increase_score(self, points):
        self.score += points
        print(points, "points added.")

    def level_up(self):
        self.level += 1
        print("Level Up!")

    def show_progress(self):
        print("\nPlayer Name:", self.name)
        print("Score:", self.score)
        print("Level:", self.level)


# Create object
player1 = Player("Vaibhav", 100, 1)

# Show initial progress
player1.show_progress()

# Update score and level multiple times
player1.increase_score(50)
player1.level_up()

player1.increase_score(100)
player1.level_up()

# Show final progress
player1.show_progress()