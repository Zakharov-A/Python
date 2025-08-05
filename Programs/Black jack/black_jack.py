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


class Game:
    def __init__(self, player_name: str) -> None:
        self.cards = DeskCard()
        self.player = Player(name = player_name)


    def start(self) -> None:
        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()
        print(self.player.hand)


def main() -> None:
    name = input("Your name ")
    game = Game(name)
    game.start()


if __name__ == '__main__':
    main()    
