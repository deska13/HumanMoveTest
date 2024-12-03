from runner_and_tournament import Runner, Tournament
from unittest import TestCase, skipIf


class TournamentTest(TestCase):
    is_frozen = True
    
    @classmethod
    def setUpClass(cls):
        cls.usain = Runner('Усейн', 10)
        cls.andrew = Runner('Андрей', 9)
        cls.nick = Runner('Ник', 3)
        cls.results = []

    @classmethod
    def tearDownClass(cls):
        for result in cls.results:
            print(result)
        del cls.results
        del cls.usain
        del cls.andrew
        del cls.nick

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_first(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.results.append({key: value.name for key, value in result.items()})
        assert result[1] == self.usain, f"first place is {self.usain.name}, not {result[1].name}"
        assert result[2] == self.nick, f"second place is {self.nick.name}, not {result[2].name}"

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_second(self):
        tournament = Tournament(90, self.nick, self.andrew)
        result = tournament.start()
        self.results.append({key: value.name for key, value in result.items()})
        assert result[1] == self.andrew, f"first place is {self.andrew.name}, not {result[1].name}"
        assert result[2] == self.nick, f"second place is {self.nick.name}, not {result[2].name}"

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_third(self):
        tournament = Tournament(90, self.nick, self.andrew, self.usain)
        result = tournament.start()
        self.results.append({key: value.name for key, value in result.items()})
        assert result[1] == self.usain, f"first place is {self.usain.name}, not {result[1].name}"
        assert result[2] == self.andrew, f"second place is {self.andrew.name}, not {result[2].name}"
        assert result[3] == self.nick, f"third place is {self.nick.name}, not {result[3].name}"

if __name__ == '__main__':
    import unittest
    unittest.main()
