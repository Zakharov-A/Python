import random

class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def get_value(self) -> int:
        if self.rank in 'AJQK':
            return 10
        else:
            return " A23456789".index(self.rank)


    def  get_rank(self) -> str:
        return f"{self.suit}{self.rank}"  


class DeskCard:
    def __init__(self) -> None:
        _rank = "A23456789AJQK"
        _suit = "SHDC"
        self.__cards = [Card(r, s) for s in _suit for r in _rank]
        random.shuffle(self.__cards)


    def get_card(self) -> Card:
        return self.__cards.pop()


class Player:
    def __init__(self, name: str) -> None:
        self._hand = []
        self.count = 0
        self.name = name


    @property
    def hand(self) -> str:
        return f"Cards in hand: {self._hand}; Points: {self.count}"
    

    @hand.setter
    def hand(self, card: Card) -> None:
       self.count += card.get_value()
       self._hand.append(card.get_rank())


class Dealer(Player):
    # def get_card(self, cards: DeskCard):
    #     while self.count < 18:
    #         self.hand = cards.get_card() 
      def get_card(self, cards: DeskCard):
        while self.count < 21:
            _card = cards.get_card()
            if _card.get_value() + self.count <= 21:
                self.hand = _card
            else:
                break    

class Game:
    def __init__(self, player_name: str) -> None:
        self.cards = DeskCard()
        self.player = Player(name = player_name)
        self.dealer = Dealer(name='Dealer')


    def print_count(self) -> str:
        return f"\n{self.player.name}:\n{self.player.hand}\n{self.dealer.name}:\n{self.dealer.hand}"    


    def check_count(self) -> None:
        if self.player.count > 21:
            print(f"You lost", self.print_count()) 
        elif self.dealer.count > 21 and self.player.count <= 21:
            print(f"You won!!!", self.print_count())
        elif self.dealer.count == self.player.count:
            print(f"The game ended in a draw!!!", self.print_count())     
        elif self.dealer.count > self.player.count:
            print(f"You lost!", self.print_count())
        elif self.dealer.count < self.player.count:
            print(f"You won!", self.print_count())    
           
                       


    def start(self) -> None:
        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()

        self.dealer.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()
        print(self.player.hand)
        while self.player.count < 21:
            answer = input("Do you want get a card? y/n\nYour choice: ")
            if answer == 'y':
                self.player.hand = self.cards.get_card()
                print(self.player.hand)
            elif answer == 'n':
                self.dealer.get_card(self.cards)
                break
        self.check_count()        
 

def main() -> None:
    name = input("Your name: ")
    game = Game(name)
    game.start()


if __name__ == '__main__':
    main()    
