import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {} # заготовили переменную для отчета

    def setUp(self):
        self.usejn = Runner('usejn', 10)
        self.andrej = Runner('andrej', 9)
        self.nik = Runner('nik', 3)

    @classmethod
    def tearDownClass(cls):
        print("\nAll Results:")
        for place, participant in cls.all_results.items():
            print(f"{place}-е место: {participant}")

    def test_usain_and_nik(self):
        # Забег с Усэйном и Ником
        tour = Tournament(90, self.usejn, self.nik)
        results = tour.start()

        # Сохраняем результаты для финального вывода
        self.__class__.all_results.update(results)

        # Проверяем, что последним финишировал Ник
        last_place = max(results.keys())
        self.assertTrue(results[last_place] == 'nik')

    def test_andrej_and_nik(self):
        # Забег с Андреем и Ником
        tour = Tournament(90, self.andrej, self.nik)
        results = tour.start()

        # Сохраняем результаты для финального вывода
        self.__class__.all_results.update(results)

        # Проверяем, что последним финишировал Ник
        last_place = max(results.keys())
        self.assertTrue(results[last_place] == 'nik')

    def test_usain_andrej_and_nik(self):
        # Забег с Усэйном, Андреем и Ником
        tour = Tournament(90, self.usejn, self.andrej, self.nik)
        results = tour.start()

        # Сохраняем результаты для финального вывода
        self.__class__.all_results.update(results)

        # Проверяем, что последним финишировал Ник
        last_place = max(results.keys())
        self.assertTrue(results[last_place] == 'nik')


if __name__ == '__main__':
    unittest.main()
