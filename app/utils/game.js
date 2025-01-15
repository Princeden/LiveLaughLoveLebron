class Player{
    constructor(self, username, balance, value1, suit1, value2, suit2){
        this.balance = balance
        this.username = username
        cards = getCards()
        this.value1 = cards[value1]
        this.value2 = cards[value2]
        this.suit1 = cards[suit1]
        this.suit2 = cards[suit2]
    }
  }
class Table{
    constructor(self, players){
        this.p1 = players[0]
        this.p2 = players[1]
        this.p3 = players[2]
        this.p4 = players[3]
        this.p5 = players[4]
        this.p6 = players[5]
      }
}