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
/* class Card{
    constructor(rank, suit) {
      this.rank = rank;
      this.suit = suit;
    }
} */
class Player{
    constructor(username, balance){
        this.balance = balance
        this.username = username
        this.hand = [];
    }
    receieveCard(card){
        this.hand.push(card); 'Note cards are dictionaries'
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
    'Call game with players'
}
async function game(players) {
    let deck = await getCards();  

    const players = [];
    'Add players'
    
    for (let i = 0; i < 6; i++) {
        players[i].receiveCard(deck.pop());  // First card
        players[i].receiveCard(deck.pop());  // Second card
    }

    // Deal community cards (Flop, Turn, River)
    const center = [];

    // Flop (3 cards)
    for (let i = 0; i < 3; i++) {
        center.push(deck.pop());
    }

    // Turn (1 card)
    center.push(deck.pop());

    // River (1 card)
    center.push(deck.pop());
}