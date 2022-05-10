





def askYorN(question):
    """asks a yes or no question and returns answer as yes or no. to use type askYorN(Your Question as a string)"""
    while True:
        answer = input(question)
        if answer.lower() == "yes" or answer.lower() == "y":
            print("yes")
            answer = "yes"
            break
        elif answer.lower() == "no" or answer.lower() == "n":
            print("no")
            answer = "no"
            break
        else:
            print("not a valid answer")
    return answer
#random Functions
def flipCoin():
    """Flips a coin and returns result as Heads or Tails. to use type flipCoin()"""
    import random
    result = random.choice["Heads","Tails"]
    return result
def roll_die(HIGH):
    """Rolls a dice between 1 and Maximum of your choice. to use type roll_die(Your Maximum #)"""
    import random
    result = random.randrange(1, HIGH)
    return result
def getNum_inRng(question,LOW, HIGH):
    """User chooses a number between Your Min and your Max. to use type getNum_inRng"""
    while True:
        answer = input(question)
        try:
            answer = int(answer)
            if answer >= LOW:
                if answer <= HIGH:
                    return answer
                else:
                    print("to high")
            else:
                print("to low")
        except:
            print("not a valid option")


#Card Functions
def shuffle_deck(deck):
    """Shuffles a list and returns it shuffled. to use type (list of choice name = shuffle_deck(list of choice))"""
    import random
    random.shuffle(deck)
    return deck
def deal_card(deck):
    """Deals top card from deck. to use type deal_card(deck)"""
    card = deck.pop(0)
    return card
def pickRanCard(deck):
    """Picks random card from deck. to use type pickRanCard(deck)"""
    import random
    pos = random.randint(0,len(deck))
    card = deck.pop(pos)
    return card

# sum = 0
# for i in range(3):
#     sum += roll_die(6)
#
# sum = sum / 3
# print(sum)
#
# input()

# answer = getNum_inRng(1, 10)
# print(answer)
# list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# print(list)
# list = shuffle_deck(list)
# print(list)
# card = deal_card(list)
# print(card)
# print(list)
# card = pickRanCard(list)
# print(card)