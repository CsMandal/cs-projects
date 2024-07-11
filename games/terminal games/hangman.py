import random

hangman=['''
     _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /  |
     |
     |___''',
     '''
     _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
     |___''',
      '''
     _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
     |___''',
         '''
     _________
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
     |___''',
     '''
     ________
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
     |___''',
    '''
         _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
     |___''',
    '''
         _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
     |___''',
    '''
         _______
     |/      |
     |      
     |      
     |       
     |      
     |
     |___'''
         ]

word_list=['apple','tree','bannana','guava','coconut']
choose_word=random.choice(word_list)
word_length=len(choose_word)
display=[]
for i in range(word_length):
    display+="_"

end_of_game=7

while end_of_game!=0:
    guess_letter=input("Guess A Letter").lower()
    flag = False
    for i in range(word_length):
        letter=choose_word[i]
        if guess_letter==letter:
            display[i]=guess_letter
            flag=True
    print("".join(display))
    if not flag:
        end_of_game-=1
        print(hangman[end_of_game])
    if "_" not in display:
        print("YOU WIN!")
        break
if end_of_game==0:
    print("YOU LOOSE!")
print("GAME OVER!")

