from lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> str:
    elves: list[int] = [0]

    for line in problem_input.lines():
        if line != "":
            elves[-1] += int(line)
        else:
            elves.append(0)

    elves = sorted(elves)
    return str(elves[-1] + elves[-2] + elves[-3])


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
