import random
name=''
follower=0
actor_dict=[
            {'name':'akshay','follower':30},
            {'name':'sharukh','follower':35},
            {'name':'salman','follower':32},
            {'name':'amir','follower':56},
            {'name':'ajay','follower':43},
            {'name':'katrina','follower':41},
            {'name':'kareena','follower':52},
            {'name':'sonam','follower':41},
            {'name':'sunny','follower':78},
            {'name':'pankaj','follower':89},
            {'name':'nawajuddin','follower':78},
            {'name':'manoj','follower':90}
            ]

print("Welcome to the GUESS game ")
stop=False
score=0
first = random.choice(actor_dict)
second = random.choice(actor_dict)
while not stop:
    if first['name']==second['name']:
        second=random.choice(actor_dict)
    guess = input(f"Choose A for {first['name']} or B  for {second['name']}")
    if guess=="a" and first['follower']>second['follower']:
        score+=1
        print(f"Correct !! score : {score}")
    elif guess=='b' and second["follower"]>first['follower']:
        score+=1
        print(f"Correct !! score : {score}")
    else:
        stop=True
    first=second
    second=random.choice(actor_dict)

print(f"YOU SCORE {score} ")
print("game over")

