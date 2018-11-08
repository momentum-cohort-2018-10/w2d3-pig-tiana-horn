import random

class Dice:
    def __init__(self, side):
        self.side = side
    
    def __str__(self):
        return "f{self.side}"
    
    def __eq__(self, other):
        return self.side == other.side
    
    def roll(self):
        """rolls the dice and turns up a number """
        roll= random.randint(1, 6)
        return roll



class Score:
    def __init__(self, dice):
        self.turn_score = []
        self.total_score = []
        self.dice = dice
    
    def add(self, roll):
        """adds individual scores to the score list"""
        self.turn_score.append(roll)
    
    def get_turn_score(self):
        if self.dice.side == 1:
            self.turn_score == 0
        else:
            return self.dice.side

def get_score(self):
    for roll in self.turn_score:
        
        return roll + (roll+1)
    
    total_turn_score == get_score(self)

def get_total_score(self):
    total_score = 0
        total_score = total_score + total_turn_score


class Player:
    
    def __init__(self, human, computer, play, score, dice):
        
        self.human = human
        self.computer = computer
        self.play = play
        self.score = score
        self.dice = dice
    
    def __eq__(self, other):
        
        return (self.human == other.human
                and self.computer == other.computer)
    
    def player_human_input():
        rolls= input("R for Roll, H for Hold and P for Pass").lower()
        return rolls
    
    def player_human_play():
        if input == "r":
            print(dice.roll)
        elif input == "h":
            print(total_turn_score, total_score)
        else:
            print(total_turn_score, total_score)


def player_computer_play():
    if total_score < 20:
        turn_score == other.turn_score
        else:
            random.choice("r", "p")

class Game:
    def __init__(self):
        self.player_score = Score()
        self.computer_score = Score()


# # pass

#Random player is chosen to start the Game
#Player gets turn
#Player then rolls dice
#Dice lands on a side
#That side value is recorded for the player's score (in list)
#The player is prompted whether or not they want to pass or roll
#Turn with stay on player or switch players
#Create counter