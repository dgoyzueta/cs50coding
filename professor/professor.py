import random
import sys

def main():
    problem = {}
    problems_list = []

    level = get_level()
    if level != None:

        for k in range(1,11):
            problem["X"] = generate_integer(level)
            problem["Y"] = generate_integer(level)
            problem["ADDITION"] = problem.get("X") + problem.get("Y")
            problems_list.append(problem)
            problem = {}

        correct_answers = 0
        problem_number = 0
        attempts_3 = 0

        while problem_number < 10:
            try:
                answer = input(str(problems_list[problem_number]["X"])+" + "+str(problems_list[problem_number]["Y"])+" = ").strip()
            except ValueError:
                print("EEE")
            except EOFError:
                print("\n")
                sys.exit("Incomplete exercise. You need to do 10 problems in total")
            else:
                if not answer.isdigit():
                  print("EEE")
                else:
                    if int(answer) == problems_list[problem_number]["ADDITION"]:
                        correct_answers = correct_answers + 1
                        problem_number = problem_number + 1
                    else:
                        print("EEE")
                        attempts_3 = attempts_3 + 1
                        if attempts_3 == 3:
                            print("This is the correct answer:", str(problems_list[problem_number]["ADDITION"]))
                            problem_number = problem_number + 1
                            attempts_3 = 0

        print("Score:", correct_answers)

def get_level():
    while True:
        try:
            level = input("Level: ").strip()
        except EOFError:
            print("\n")
            return None
        else:
            if level.isdigit():
                level = int(level)
                if level in [1,2,3]:
                    return level


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
