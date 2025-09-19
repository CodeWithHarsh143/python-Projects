import random
import blackjack_art
import os


def cards():

    card = [11,2,3,4,5,6,7,8,9,10,10,10,10]

    return card

def art():

    print(f"{blackjack_art.blackjack_card}{blackjack_art.art_text}")

def start():

    s = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    return s

def Clear():
   if os.name=="nt":
      os.system("cls")
    
   art()

def logic(card):

    you = [random.choice(card),random.choice(card)] ; dealer = [random.choice(card)]

    s = sum(you)

    s_d = sum(dealer) 

    print(f"Your Cards: {you}, Current Score: {s} "  )

    print("Computer First Card: ",*dealer)

    while True:
    
       again = input("Type 'y' to get another card else Type 'n' :  ").lower()

       if again!="y":
          
          break
  
       Clear()

       n_c = random.choice(card)
          
       you.append(n_c)

       s+=n_c

       print(f"Your Cards: {you}, Current Score: {s} "  )

       print("Computer First Card: ",*dealer)

       if s>21:

            return print("'Burst'🥺, You lose  cards has exceeded the limit which is 21")      
        
    while s_d<=17 and  s_d<=s :

        n_d = random.choice(card)

        dealer.append(n_d)

        s_d+=n_d

    print(f"Your Cards: {you}, Current Score: {s} " )

    print(f"Dealer's Final hand: {dealer}   Dealer's Score: {s_d}")
        
    if s_d>s:

        print("You Lose 🫢")

    elif s_d==s:

        print("Draw 😑")

    else:
        print("You Win 🥳🍻")     

    

def Black_Jack():
   
   Start = start()

   if Start=="y":
      
      art()

      Cards = cards()

      logic(Cards)

   elif Start=="n":
      
      print("Thankyou for your Input, Please try other time when you have time 😊")

   else:
      print("Please Enter 'y' or 'n' ")
      
      Black_Jack()


if __name__=="__main__":
   Black_Jack()
      

      


      
   

   








        


            

        

          

          


        

        


        

        






