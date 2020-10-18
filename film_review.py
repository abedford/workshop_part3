import argparse
import csv
parser = argparse.ArgumentParser(description='Rate a film from 1-5')
parser.add_argument('--film',
                    help='name of the film')
parser.add_argument('--stars', type=int, choices=range(1, 6),
                    help='stars you would give the film from 1 to 5')

args = parser.parse_args()

with open("C:\\Work\\Exercises\\workshop_part3\\film_review.txt", "a+") as f:
    f.write("{0}, {1}\r\n".format(args.film, args.stars))
