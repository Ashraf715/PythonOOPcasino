class Outcome:
    """
    Each number has a variety of Outcomes i.e. ("Red" 1:1)
    Test: test = Outcome("test",5), then test.winAmount(5) = 25
    Chapter 5, pages 37-43
    """
    def __init__(self, name:str, odds:int):
        self.name = str(name)
        self.odds = int(odds)

    def winAmount(self, amount:float) -> float:
        return self.odds * amount

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __ne__(self, other) -> bool:
        return self.name != other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self):
        return "{name:s} ({odds:d}:1)".format_map(vars(self))

    def __repr__(self):
        return "{class_:s}({name!r}, {odds!r})".format(class_=type(self).__name__, **vars(self))


class bin(frozenset):
    pass


class BinBuilder:
    """
    Creates all of the winning Outcomes and adds them to each bin on the wheel
    Each bin has 12-14 different ways that it can be a winner e.g. 1 can be straight, street, corner...
    Chapter 8, pages 53-58
    """

    def buildBins(self, wheel):
        pass

    def straightBets(self):
        """
        Bet on a single number paying at 35:1
        38 bets / 38 outcomes
        """
        outcomes = []
        outcomes.append((0, Outcome("0", 35)))
        for i in range(1, 37):
            outcomes.append((i, Outcome(str(i), 35)))
        outcomes.append((37, Outcome("00", 35)))
        return outcomes

    def splitBets(self):
        """
        Adjacent pair of numbers (column or row) paying at 17:1
        114 bets / 114 outcomes
        """
        outcomes = []
        return outcomes

    def streetBets(self):
        """
        3 numbers in a single row paying at 11:1
        12 possible bets / 36 outcomes
        """
        outcomes = []
        return outcomes

    def lineBets(self):
        """
        A 6 number block (2 street bets) paying at 5:1
        11 possible bets
        """
        outcomes = []
        possible_outcomes = {}
        return outcomes

    def dozenBets(self):
        """
        Each number is member of one of three dozens paying at 2:1
        3 possible bets
        """
        outcomes = []
        return outcomes

    def cornerBets(self):
        """
        A square of 4 numbers paying at 8:1
        22 possible bets / 88 outcomes
        """
        outcomes = []
        return outcomes

    def outsideBets(self):
        """
        All other bets e.g. Red/Black, Low/High, Even/Odd
        """
        outcomes = []
        return outcomes

test = Outcome(name="test", odds=5)

bb = BinBuilder()
print(bb.lineBets())

