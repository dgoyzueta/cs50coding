import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) < 3:
        print("Too few arguments")
        return
    if len(sys.argv) > 3:
        print("Too many arguments")
        return
    if sys.argv[1][-3:] != "csv":
        print("First argument is not a csv file")
        return
    if sys.argv[2][-3:] != "txt":
        print("Second argument is not a txt file")
        return

    # TODO: Read database file into a variable
    db_list = []
    with open(sys.argv[1]) as database:
        reader = csv.DictReader(database)
        for row in reader:
            db_list.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as text:
        line = text.readlines()
        # subject variable has the DNA sequence of the subject being analyzed
        subject = line[0]

    # TODO: Find longest match of each STR in DNA sequence
    # str dictionary has all the STR with its max counts found in the subject variable
    str = {}
    for key in db_list[0].keys():
        if key != "name":
            str[key] = longest_match(subject, key)

    # TODO: Check database for matching profiles
    for record in db_list:
        found = True
        for key in str:
            if key in record:
                if str[key] != int(record[key]):
                    found = False
                    break
        if found:
            print(record["name"])
            break
    if not found:
        print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
