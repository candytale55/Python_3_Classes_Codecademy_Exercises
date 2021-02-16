class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item


class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item *.001

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item *.00005




# why we would even want to have two different classes with two differently implemented methods to use the same method name. 
# This style is especially useful when we have an object for which it might not matter which class the object is an instance of. 
# Instead, we’re interested in whether that object can perform a given task.

# When two classes have the same method names and attributes, 
# we say they implement the same interface. An interface in Python usually refers to the names of the methods 
# and the arguments they take. Other programming languages have more rigid definitions of what an interface is, 
# but it usually hinges on the fact that different objects from different classes can perform the same operation 
# (even if it is implemented differently for each class).




# EXAMPLE (Doesn't work):
class Chess:
  def __init__(self):
    #self.board = setup_board()
    #self.pieces = add_chess_pieces()
   def play(self):
    print("Playing chess!")
 
class Checkers:
  def __init__(self):
    #self.board = setup_board()
    #self.pieces = add_checkers_pieces()
  
   def play(self):
    print("Playing checkers!")


# In Chess we define a constructor that sets up the board and pieces, and a .play() method. 
# Checkers also defines a .play() method. 
# If we have a play_game() function that takes an instance of Chess or Checkers, 
# it could call the .play() method without having to check which class the object is an instance of.

def play_game(chess_or_checkers):
  chess_or_checkers.play()
 
chess_game = Chess()
checkers_game = Checkers()
chess_game_2 = Chess()
 
for game in [chess_game, checkers_game, chess_game_2]:
  play_game(game)


# https://discuss.codecademy.com/t/if-a-methods-parameters-are-modified-is-it-still-considered-implementing-an-interface/361566
