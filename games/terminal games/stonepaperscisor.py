import random
def stone(value):
    if value==0:
        print('''   PAPER         ___..__
          __..--""" ._ __.'
                      "-..__
                    '"--..__";
         ___        '--...__"";
            `-..__ '"---..._;"
                  """"----'       ''')
    elif value==1:
        print('''. Stone
                 ;';.
                 ';.  ';..;'  '
                   ';. '      ' .;'
                    .;' - =   .;'
                  .;',  ,  ,  ::
                .;'.;'.;'.;' .;'
              .;'.;'.;'.;' .;'  
              ';.';.';.';.;''')
    else :
        print(''' SCISOR
            .-.  _
            | | / )
            | |/ /
           _|__ /_
          / __)-' )
          \  `(.-')
           > ._>-'
          / \/''')

system_choice=random.randint(0,2)
user_choice=int(input("Enter 0->Paper 1->stone 2->Scisor"))
if user_choice > 3 and user_choice <0:
    print("invalid Choice")
else:
    print("****--sytem choice--*****")
    stone(system_choice)
    print("\n***--user choice---*****")
    stone(user_choice)
    if user_choice==system_choice:
        print("its Draw")
    elif system_choice==2 and user_choice==0:
        print("You loose")
    elif system_choice >user_choice or (user_choice==2 and system_choice==1):
        print("You Win")
    else:
        print("You Loose")





