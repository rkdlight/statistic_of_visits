from lxml import etree
from datetime import datetime, timedelta


class Statistic:
    """
        class to get the amount of the time persons were somewhere from xml
        and sort it by person's name or time period.
    """

    def __init__(self, path):
        """
        :param path: str - path to xml file with statistic data
        """
        self.path = path

    def data_generator(self, path):
        """
        This generator function parse xml file by iterparse and return objects with parsed data
        :param path: str - path to xml file with statistic data
        :return: object {'person_name':'name', 'start': datetime, 'end': datetime}
        """

        context = etree.iterparse(path, tag='person')
        for event, element in context:
            person_name = element.attrib['full_name']
            for child in element:
                if child.tag == 'start':
                    start = datetime.strptime(child.text, "%d-%m-%Y %H:%M:%S")
                else:
                    end = datetime.strptime(child.text, "%d-%m-%Y %H:%M:%S")

            yield {
                'person_name': person_name,
                'start': start,
                'end': end
            }

            element.clear()
            while element.getprevious() is not None:
                del element.getparent()[0]
        del context

    def get_amount_for(self, date=None, person_name=None):
        """
        This function sort statistic data by date, period and by person name
        and return amount of time from sorted data. If parameters is None function return amount of all time
        :param date: tuple - (start_date, end_date) if both items are not empty, then it is sorted by period,
                            if end_date is empty, then it is sorted by one date,
                            if date is None, then sorted only by person name
        :param person_name: str - sort data by person_name
        :return: timedelta - amount of time from sorted data
        """

        data = self.data_generator(self.path)
        amount = timedelta()

        # if filters is None return amount of all time
        if (date is None or date[0] is None) and person_name is None:
            for person in data:
                amount += person['end'] - person['start']

            return amount

        # if only person name is not empty, sort only by this parameter
        if date is None:
            for person in data:
                if person['person_name'] == person_name:
                    amount += person['end'] - person['start']

            return amount

        end_date = None
        if len(date) == 2:
            start_date, end_date = date
        else:
            start_date,  = date

        # parse datetime objects from strings
        start_date = datetime.strptime(start_date, "%d-%m-%Y").date()
        if end_date is not None:
            end_date = datetime.strptime(end_date, "%d-%m-%Y").date()

        for person in data:

            person_start = person['start'].date()

            statistic_filter = False

            # filter by period and person name
            if end_date is not None and person_name is not None:
                if start_date <= person_start < end_date and person['person_name'] == person_name:
                    statistic_filter = True

            # filter by period
            elif end_date is not None:
                if start_date <= person_start < end_date:
                    statistic_filter = True

            # filter by date and person name
            elif person_name is not None:
                if person_start == start_date and person['person_name'] == person_name:
                    statistic_filter = True

            # filter by date
            else:
                if person_start == start_date:
                    statistic_filter = True

            if statistic_filter:
                amount += person['end'] - person['start']

        return amount
