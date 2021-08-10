import random
FILE_HANDLER = None


def show_case():
    name = input("Enter your goodname : ")
    print("Welcome %s to Hangman game ...! "%name)
    print("___"*50)
    print("Try to complete the game in 10 attempts : ")

def file_opener(address):
    global FILE_HANDLER 
    FILE_HANDLER = open(address,'r')
    word_list = list(FILE_HANDLER)
    word=random.choice(word_list)
    word = word[:len(word)-1]
    word_shower(word)

def aborter():
    global FILE_HANDLER 
    FILE_HANDLER.close()

def man_show(attempt):
    if attempt == 9:
        print(''' 
                  __ __ 
                 | ^ ^ |
                 |__ __|           
                 ''')
        print("Oops...wrong guess")
        print("9 attempts left.")

    
    elif attempt == 8:
        print('''
                  __ __ 
                 | ^ ^ |
                 |__-__|   
                   / \\
                     
        ''')
        print("Oops...wrong guess")
        print("8 attempts left.")

    elif attempt == 7:
        print('''
                  __ __ 
                 | ^ ^ |
                 |__-__|   
                   /|\\
                        
        ''')
        print("Oops again...wrong guess")
        print("7 attempts left.")


    elif attempt == 6:
        print('''
                  __ __ 
                 | - - |
                 |__.__|   
                   /|\\
                   /     
        ''')
        print("AAAaaahh..??")
        print("6 attempts left.")


    elif attempt == 5:
        print('''
                            
                  __ __        
                 | . . |        
                 |__-__|___ ___   
                   /|\\
                   / \   
        ''')
        print("Guessed Wrong..5 attempts left.")

    
    elif attempt == 4:
        print('''
                            
                  __ __        
                 | . . |       | 
                 |__-__|___ ___|   
                   /|\\
                   / \   
                 =======
        ''')
        print("Guessed Wrong...4 attempts left.")

    
    elif attempt == 3:
        print('''
                           
                  __ __        |
                 | 0 . |       | 
                 |__-__|___ ___|   
                   /|\\
                   / \ 
                 =======  
        ''')
        
        print("Guessed wrong...3 attempts left.")


    elif attempt == 2:
        print('''
                           _________
                  __ __        |
                 | 0 . |       | 
                 |__-__|___ ___|   
                   /|\\
                   / \  
                 =========   
        ''')
        
        print("Guessed wrong...2 attempts left.")


    elif attempt == 1:
        print('''
                            \_____/
                  __ __        |
                 | 0 . |       | 
                 |__-__|___ ___|   
                   /|\\
                   / \   
                 ========
        ''')
        print("DANGER ZONE...!!..1 attempt left.")


    else:
        if attempt == 0:
            print('''
                             ><!!!///??//><
                      __ __        |
                     | * . |       | 
                     |__-__|___ ___|   
                       /|\\
                       / \   
            ''')
            print("Really...you lost..!! ")
            print("U let a kind men die..:((")
            
    
    
    
    
def word_shower(word):
    attempt=10
    
    guess_made=""
    
    while len(word) > 0:
        main =""
        
        for letter in word:
            if letter in guess_made:
                main = main + letter
            else:
                main = main + "-"
        if main == word:
            print("\nThe Word is : ",word)
            print("YOU WON...:))")
            break

        
        print("Guess the word ",main)
        guess=input()

        
        if guess.isalpha() == 1:
           guess_made = guess_made + guess
        else:  
            print(" Enter a valid a guess : ")
            guess=input()
        
        if guess not in word:
            attempt = attempt-1
            man_show(attempt)
            if attempt==0:
             print("The letter was : %s ...try your luck next time...:( "%word)
             break

            
                
if __name__=="__main__":    
    show_case()
    file_opener("/home/karuna/Programs/Projects/Hangman_game/1-1000.txt")
    aborter()
    