async function getNeededCards(n) {
    const url = `https://deckofcardsapi.com/api/deck/new/draw/?count=${n}`;
    
    try {
        const response = await fetch(url);  // HTTP
        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
        }

        const data = await response.json();  // JSON
        return data.cards || []; 
    } catch (error) {
        console.error("Error:", error.message);
    }
}
async function getCards() {
    const data = await getNeededCards(52);  // Fetch one deck
    const cardData = data.map(card => ({
        value: card.value,
        suit: card.suit
    }));
    return cardData;
}
class Card{
    constructor(rank, suit) {
      this.rank = rank;
      this.suit = suit;
    }
}
class Player{
    constructor(self, username, balance, i){
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
    constructor(players){
        this.p1 = players[0]
        this.p2 = players[1]
        this.p3 = players[2]
        this.p4 = players[3]
        this.p5 = players[4]
        this.p6 = players[5]
        this.center = [];
        this.pot = 0;

      }

}