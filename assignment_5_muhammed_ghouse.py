import random,sys


cards_list=[1,2,3,4,5,6,7,8,9,10]#Cards in the Deck
players_hand_of_cards=[]#Cards in the Players hand

dealers_hand_of_cards=[]#Cards in the Dealers hand
shuffled_cards=[]
player_total=0
dealer_total=0
player_card=0#try empty string maybe
dealer_card=0
deal=21





#######################------------------THINGS TO DO------------------#############
####################  CREATE a Player_turn function


def main():
    play_again=""
    game_status=input("Game start...'y' for yes / 'n' for no...:  ")
    if game_status=="y" or game_status=="Y":
        if play_again=="Y" or "y":


                #Cards in the Players hand
            players_hand_of_cards.clear()

            dealers_hand_of_cards.clear()#Cards in the Dealers hand


            global cards_list
            cards_list=[1,2,3,4,5,6,7,8,9,10]
            player_total=0
            dealer_total=0
            player_card=0#try empty string maybe
            dealer_card=0
            deal=21
            play_again=""


        shuffle(cards_list)#Shuffles the cards

        shuffled_cards=cards_list
        card_1=shuffled_cards.pop()
        players_hand_of_cards.append(card_1)
        card_2=shuffled_cards.pop()
        players_hand_of_cards.append(card_2)
        dealer_card_1=shuffled_cards.pop()
        dealers_hand_of_cards.append(dealer_card_1)
        dealer_card_2=shuffled_cards.pop()
        dealers_hand_of_cards.append(dealer_card_2)

        #the game starts and all cards have been dealt

        print(f'Your cards:{players_hand_of_cards} Dealer Has two cards, only one is visible: {dealer_card_1}' )


#        player_action=input("Hit or Stay?")
        player_action_H_or_S(players_hand_of_cards,shuffled_cards,dealers_hand_of_cards)
        #if player_action=="h" or player_action=="H":
#            player_hit(shuffled_cards,players_hand_of_cards)


                #if len(shuffled_cards)==0 and player_total > dealer_total and player_total<= 21:
                    #print("You are closer to 21 and you won")
                    #break
                #elif len(shuffled_cards)==0 and player_total < dealer_total and dealer_total <=21:

                    #print("The dealer is closer to 21, you lost")
                    #break




            #elif player_action=="s" or player_action=="S":
##############################STAND##########################

            #    dealer_turn(dealers_hand_of_cards,dealer_card_2,shuffled_cards,dealer_card)



    elif game_status=="n" or game_status=="N":
        print("The Program has Exited")#exits the program


    else:
        print("invalid character,quiting the program...")#invalid character at prompt game start Yes or No

    #Check if the cards left in deck is 0 or empty

#-------------------------------CUSTOM FUNCTIONS---------------------------------------#

def stand(dealer_card_2_arg,dealers_hand_of_cards_arg,dealer_total_arg,player_total_arg):


    if player_total_arg > dealer_total_arg and player_total_arg<= 21:

        print("You are closer to 21 and you won")

    elif player_total_arg < dealer_total_arg and dealer_total_arg <=21:

        print("The dealer is closer to 21, you lost")



def shuffle(cards_to_shuffle):
    random.shuffle(cards_to_shuffle)
    return cards_to_shuffle

def player_hit(player_card_arg,shuffled_cards_arg,players_hand_of_cards_arg):


    player_card_arg=shuffled_cards_arg.pop()
    players_hand_of_cards_arg.append(player_card_arg)
    print(f"You picked up a {players_hand_of_cards[-1]}, Here are all of the cards in your hand {players_hand_of_cards}")
    if calculate_player_total(players_hand_of_cards_arg) == 21:
        print("You got exactly 21, your turn is over, dealers turn starting...")
        dealer_turn(dealers_hand_of_cards,shuffled_cards,dealer_card)

    elif calculate_player_total(players_hand_of_cards_arg)>21:
        print(f"\n------------------>You Lost or Bust you got over 21\nHere are Your Latest STATS:\nYou picked up a {players_hand_of_cards[-1]}, Here are all of the cards in your hand {players_hand_of_cards}\n .")
        #game_status="l"
        play_again=input("Do you wanna play again?")
        if play_again=="Y" or play_again=="y":

            main()
        elif play_again=="N" or play_again=="n":
            game_status="n"
            sys.exit("quting")
        else:
            print("invalid character...quiting the game")
            sys.exit()
    return player_card,shuffled_cards_arg,players_hand_of_cards_arg

def calculate_player_total(players_hand_of_cards_arg):

    player_total=0
    for x in players_hand_of_cards_arg:
        player_total+=x


    return player_total



def calculate_dealer_total(dealers_hand_of_cards_arg):
    dealer_total=0

    for i in dealers_hand_of_cards_arg:
        dealer_total+=i


    return dealer_total

def dealer_hit(dealer_card_arg,shuffled_cards_arg,dealers_hand_of_cards_arg):

    dealer_card_arg=shuffled_cards_arg.pop()
    dealers_hand_of_cards_arg.append(dealer_card_arg)
    return dealer_card_arg,shuffled_cards_arg,dealers_hand_of_cards_arg



def dealer_turn(dealers_hand_of_cards_arg,shuffled_cards_arg,dealer_card_arg):
    print("---Its the dealers turn")
    print(f"The dealer total {calculate_dealer_total(dealers_hand_of_cards_arg)}Its the dealers turn, the dealer turns over the hidden card \n{dealers_hand_of_cards_arg[-1]}, he has {dealers_hand_of_cards_arg} in his hand, \n")


    while True:

        print(f"the dealers current stats: his hand is {dealers_hand_of_cards}\nHis total is {calculate_dealer_total(dealers_hand_of_cards)}")
        print(f"Cards in deck{len(shuffled_cards_arg)}")
        cards_in_deck=len(shuffled_cards_arg)
        if calculate_dealer_total(dealers_hand_of_cards_arg)<=16:


            print(f"the dealer is hitting...")

            dealer_hit(dealer_card_arg,shuffled_cards_arg,dealers_hand_of_cards_arg)
            print(f"the dealers hand is {dealers_hand_of_cards}\nHis total is {calculate_dealer_total(dealers_hand_of_cards)}")
            print(f"Cards in deck{len(shuffled_cards_arg)}")
            continue



        elif cards_in_deck==0:
            print(len(shuffled_cards_arg))
            print("Out of cards")
            play_again=input("Do you wanna play again?")
            if play_again=="Y" or play_again=="y":


                main()
            elif play_again=="N" or play_again=="n":
                game_status="n"
                sys.exit("quting")
            else:
                print("invalid character...quiting the game")


            #->break

        elif calculate_dealer_total(dealers_hand_of_cards_arg)>=17 and calculate_dealer_total(dealers_hand_of_cards_arg)<21:
            print(f"the dealer is standing.... his total is {calculate_dealer_total(dealers_hand_of_cards)}")
            return players_hand_of_cards,shuffled_cards,dealers_hand_of_cards
            player_action_H_or_S(players_hand_of_cards,shuffled_cards,dealers_hand_of_cards)
            if len(shuffled_cards_arg)==0:
                print(len(shuffled_cards_arg))
                print("Out of cards")
                play_again=input("do you wanna play again?")
                if play_again=="Y" or play_again=="y":


                    main()

                elif play_again=="N" or play_again=="n":
                    game_status="n"
                    sys.exit("quting")
                else:
                    print("invalid character...quiting the game")

                #sys.exit()
                    #create plater turn function and call it
        elif calculate_dealer_total(dealers_hand_of_cards_arg)==21:
            print(f"Dealer has won, he has {calculate_dealer_total(dealers_hand_of_cards)}")
            play_again=input("Do you wanna play again?")
            if play_again=="Y" or play_again=="y":


                main()
            elif play_again=="N" or play_again=="n":
                game_status="n"
                sys.exit("quting")
            else:
                print("invalid character...quiting the game")

        elif calculate_dealer_total(dealers_hand_of_cards_arg)>21:
            print(f"Dealer Busts-YOU WON!, dealer had {calculate_dealer_total(dealers_hand_of_cards)}--You had {calculate_player_total(players_hand_of_cards)}")
            play_again=input("Do you wanna play again?")
            if play_again=="Y" or play_again=="y":


                main()
            elif play_again=="N" or play_again=="n":
                game_status="n"
                sys.exit()



def player_action_H_or_S(players_hand_of_cards_arg,shuffled_cards_arg,dealers_hand_of_cards_arg):
    while calculate_player_total(players_hand_of_cards_arg) <21:

        player_action=input("hit or Stay?")






        if player_action=="h" or player_action=="H":

            player_hit(player_card,shuffled_cards_arg,players_hand_of_cards_arg)

        #elif calculate_player_total(players_hand_of_cards) == 21:
            #print("You got exactly 21, your turn is over, dealers turn starting...")
            #dealer_turn(dealers_hand_of_cards,dealer_card_2,shuffled_cards,dealer_card)

        #elif calculate_player_total(players_hand_of_cards)>21:
            #print(f"You picked up a {players_hand_of_cards[-1]}, Here are all of the cards in your hand {players_hand_of_cards}\n You Lost or Bust you got over 21.")
            #break



        elif player_action=="s" or player_action=="S":

            dealer_turn(dealers_hand_of_cards_arg,shuffled_cards_arg,dealer_card)



        else:
            print("Invalid Character...Quiting the game")
            sys.exit()


if __name__=='__main__':
    main()
