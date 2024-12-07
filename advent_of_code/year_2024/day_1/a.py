from advent_of_code.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> str:
    list_lines = problem_input.lines()

    first_list = sorted([int(x.split()[0]) for x in list_lines])
    second_list = sorted([int(x.split()[-1]) for x in list_lines])

    distance = 0

    for i in range(len(first_list)):
        distance += abs(first_list[i] - second_list[i])

    return str(distance)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
