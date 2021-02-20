import random
# library that we use in order to choose 
# on random words from a list of words

name = input("What is your name? ")
# Here the user is asked to enter the name first
 
print("Good Luck ! ", name)
 
words = ['rainbow', 'computer', 'science', 'programming', 
         'python', 'mathematics', 'player', 'condition', 
         'reverse', 'water', 'board', 'geeks','monitor',
         'lamp','notebook','rehab','smartphone','alien',
         'nation','occupation','motor','money','fame',
         'cash','belt','motivation','cucumber','tomato',
         'potato','drug','love','weather','kitchen','shopping',
         'christmas','manners','mashup','mobile',
         'number','competition','collaboration','college',
         'university','army','athlete','enemy','aeroplane',
         'astronaut','apple','building','application',
         'restaurant','movie','music','song','party','alarm',
         'radio','speed','death','batch','opera','enigma',
         'teddy','chair','table','almond','picture',
         'photograph','album','single','multiple','rural',
         'urban','region','police','pandemic','password',
         'instagram','facebook','snake','chocolate','flower',
         'mouse','books','calendar','dictionary',
         'religion','racquet','remember','jacket',
         'badminton','shuttle','flight','airport','train',
         'station','coach','camera','catalogue','caramel',
         'cheese','smile','prototype','painting',
         'youtube','internet','corridoor','kangaroo',
         'compact','comrade','cement','story','thanks',
         'telephone','realistic','controller',
         'playstation','console','launch','release'] 
 
# Function chooses a random word from the specified list

word = random.choice(words)

print("Choose Difficulty :")
print("1) EASY")
print("2) MEDIUM")
print("3) HARD")
print("4) LEGENDARY")
choice=int(input())
if choice==1:
    turns=12
elif choice==2:
    turns=9
elif choice==3:
    turns=5
elif choice==4:
    turns=3
else :
    print("WRONG INPUT")
    input("PRESS ENTER TO EXIT!")
 
 
print("Guess the characters")
 
# initializing guesses with vowels 
guesses = 'aeiou'
 
 
 
while turns > 0:
     
    # failure counter
    failed = 0
     
    # storing one character at a time in char 
    for char in word: 
         
        # checking if that character is present in guesses
        if char in guesses: 
            print(char,end=' ')
             
        else: 
            print("_",end=' ')
             
            # failure value incremented accordingly
            failed += 1
             
 
    if failed == 0:
        # 0 failures mean that the user has won
        print("You Win") 
        input('Press Enter to Exit')
        
        break
     
    # if the character doesn't match , user is given another chance
    print()
    guess = input("Guess a character:")
     
    # every character will be added in guesses 
    guesses += guess 
     
    # checking if the guess is not a part of the word
    if guess not in word:
         
        # a turn will be reduced 
        turns -= 1
         
        
        # and “Wrong” will be given as output 
        print("Wrong")
         
        # printing number of turns left for the user
        print("You have", + turns, 'more guesses')
         
         
        if turns == 0:
            print("You Lose")
            print("The correct word was '",word,"'")
            input('Press Enter to Exit...')
