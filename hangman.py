import random

class HangmanGame:
  def __init__(self, word):
    self.target = Word(word)
    self.is_won = False
    print(self.target.word)
    
  def play(self):
    self.target.guess_letter(input("Input char: ")) 
    #Player guesses a character in the word
    #Should make some failsafes
    #additionally, we should give the user the ability to outright guess the word

    if self.target.check_for_win() == True:
      self.is_won = True
    
    if self.is_won == False:
      self.play()
    else:
      print("You win!!")
    

  def get_guess(self):
    pass

  def display_word(self):
    #use the hidden_word array for this
    pass

  def display_image(self):
    pass

  def display_guessed_letters(self):
    pass
  
    

class Word:
  def __init__(self, word):
    self.word = word #The target word
    self.hidden_word = [] #An array that stores all of the indexes of self.word that the player has guessed

  def guess_letter(self, char):
    counter = 0 #Keeps track of the index of the array that we are looping through
    print("word:", self.word)

    for letter in self.word: #loops for every letter in self.word
      if char == letter: #Checks for the match
        if counter not in self.hidden_word: #stops double ups
          self.hidden_word.append(counter) #add the index of the match if the player makes a correct match
      counter += 1 #increments the index counter before the next check

    print(self.hidden_word) #For debugging

  def check_word(self, guess):
    if guess == self.word:
      return True
    else:
      return False

  def check_for_win(self):
    if self.hidden_word.__len__() == self.word.__len__(): 
      #Checks if there are the same amount of discovered indexes as total indexes
      #print("Do the thing")
      return True
    return False

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
    self.word = self.words[random.randint(0, self.words.__len__()) - 1]
    pass

  def get_word(self): #Returns the value of self.word
    return self.word

if __name__ == "__main__":
  wordbank = Wordbank()
  wordbank.create_words()
  game = HangmanGame(wordbank.get_word())
  game.play()
  

