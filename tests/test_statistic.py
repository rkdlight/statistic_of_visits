import unittest
from xml_parser import Statistic
from datetime import timedelta


class TestStatistic(unittest.TestCase):

    def setUp(self):
        self.statistic = Statistic('data.xml')

    def test_get_amount_for_all(self):
        # amount for one date
        result_test = timedelta(hours=29, minutes=20)
        result = self.statistic.get_amount_for()
        self.assertEqual(result, result_test)

    def test_get_amount_for_date(self):
        # amount for one date
        result_test = timedelta(hours=9)
        result = self.statistic.get_amount_for(date=("21-12-2011",))
        self.assertEqual(result, result_test)

    def test_get_amount_for_period(self):
        # amount for period
        result_test = timedelta(hours=17)
        result = self.statistic.get_amount_for(date=("21-12-2011", "23-12-2011"))
        self.assertEqual(result, result_test)

    def test_get_amount_for_period_and_person_name(self):
        # amount for period and by person name
        result_test = timedelta(hours=8, minutes=0)
        result = self.statistic.get_amount_for(date=("21-12-2011", "23-12-2011"), person_name='a.stepanova')
        self.assertEqual(result, result_test)

    def test_get_amount_for_person_name(self):
        # amount for person name
        result_test = timedelta(hours=15, minutes=20)
        result = self.statistic.get_amount_for(person_name='i.ivanov')
        self.assertEqual(result, result_test)


if __name__ == '__main__':
    unittest.main()
