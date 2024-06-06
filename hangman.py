import random

class HangmanGame:
  def __init__(self, wordbank):
    self.word = wordbank
    
  def play(self):
    pass

  def get_guess(self):
    pass

  def display_word(self):
    pass

  def display_image(self):
    #CVAHSD
    pass

  def display_guessed_letters(self):
    pass
  
    

class Word:
  def __init__(self, letters):
    self.letters = []

  def guess_letter(self):
    pass

  def check_word(self):
    pass

  def check_for_win(self):
    pass


class Pictures:
  def __init__(self):
    pass

  def get_picture(self):
    pass

class Wordbank:
  def __init__(self):
    #All possible words listed below
    self.words = ["button",
                  "represent",
                  "dangerous",
                  "lounge",
                  "ordinary",
                  "pedestrian",
                  "ferry",
                  "cell",
                  "resign",
                  "lawyer"]

    self.word = "temp"
  
  def create_words(self): #assigns self.word to a random word from the self.words array
    self.word = self.words[random.randint(0, self.words.__len__())]
    pass

  def get_word(self): #Returns the value of self.word
    return self.word

if __name__ == "__main__":
  wordbank = Wordbank()
  wordbank.create_words()
  #print(wordbank.get_word()) for debugging
  game = HangmanGame(wordbank.get_word())
  game.play()
  

