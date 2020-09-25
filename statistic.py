from xml_parser import Statistic
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to xml file with data")
    parser.add_argument("-s", "--start", help="start date for filter")
    parser.add_argument("-e", "--end", help="end date for filter")
    parser.add_argument("-n", "--person_name", help="person name for filter")
    args = parser.parse_args()

    statistic = Statistic(path=args.path)

    print(statistic.get_amount_for(date=(args.start, args.end), person_name=args.person_name))



