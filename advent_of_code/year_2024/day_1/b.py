from advent_of_code.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> str:
    list_lines = problem_input.lines()

    first_list = [int(x.split()[0]) for x in list_lines]
    second_list = [int(x.split()[-1]) for x in list_lines]

    hits: dict[int, int] = {}
    similarity_score = 0

    for n in second_list:
        try:
            hits[n] += 1
        except KeyError:
            hits[n] = 1

    for n in first_list:
        try:
            similarity_score += n * hits[n]
        except:
            pass

    return str(similarity_score)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
