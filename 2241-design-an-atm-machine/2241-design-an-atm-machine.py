from typing import List

class Banknote:
    def __init__(self, denomination: int, count: int = 0):
        self._denomination = denomination
        self._count = count

    def add_banknotes(self, count: int):
        self._count += count

    def remove_banknotes(self, count: int):
        self._count -= count

    def total_value(self):
        return self._denomination * self._count

    @property
    def denomination(self):
        return self._denomination

    @property
    def count(self):
        return self._count


class ATM:
    def __init__(self):
        self._banknotes = [
            Banknote(20),
            Banknote(50),
            Banknote(100),
            Banknote(200),
            Banknote(500)
        ]

    def deposit(self, banknotes_count: List[int]) -> None:
        for i, count in enumerate(banknotes_count):
            self._banknotes[i].add_banknotes(count)

    def withdraw(self, amount: int) -> List[int]:
        withdrawn_banknotes = [0, 0, 0, 0, 0]
        remaining_amount = amount

        for banknote in reversed(self._banknotes):
            num_banknotes_to_withdraw = min(banknote.count, remaining_amount // banknote.denomination)
            withdrawn_banknotes[self._denomination_index(banknote.denomination)] = num_banknotes_to_withdraw
            remaining_amount -= num_banknotes_to_withdraw * banknote.denomination

        if remaining_amount == 0:
            for i, banknote in enumerate(self._banknotes):
                banknote.remove_banknotes(withdrawn_banknotes[i])
            return withdrawn_banknotes
        else:
            return [-1]

    @staticmethod
    def _denomination_index(denomination: int) -> int:
        return [20, 50, 100, 200, 500].index(denomination)

 
