class Player:
    def __init_(self, username, balance):
        self.balance = balance
        self.username = username
    def get_cards(self):
        return 'A'
class Game:
    '''
    Four states: FIRST_ROUND, DRAW ,SECOND_ROUND, PAYOUT
    '''
    STATE = "FIRST_ROUND"
    card_dict = {}
    discard_dict = {}
    bet_dict = {}
    def __init__(self, players):
        self.card_dict = {}
        for i in range(0, len(players)):
            if i == 0:
                self.small_blind = player

            self.card_dict[player] = player # replace with function to get cards
    def get_moves(self, player):
        if STATE == "FIRST_ROUND":
            if small_blind == player:
                return ['BET']
            else: 
                return ['FOLD', 'CALL', 'RAISE']
        elif STATE == 'DRAW':
            return ['DISCARD']
        elif STATE == "SECOND_ROUND":
            return ['FOLD', 'CALL', 'RAISE']
        elif STATE == 'PAYOUT':
            return ['PAYOUT']
    '''
    IDEA: when someone presses the button to discard cards it would add that information to discard dict with the key being their username
    TO DO: implemn it

    '''
    def add_to_discard(self, player, cards):
        return

    # go through the discard dict and give player their new cards
    def redraw(self):
        return
        
    #
    #def
    
        
    

#class Table:
