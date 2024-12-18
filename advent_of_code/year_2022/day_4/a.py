from advent_of_code.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> str:
    fully_contained = 0

    for line in problem_input.lines():
        pairs = line.split(",")

        first_elf = set(
            range(int(pairs[0].split("-")[0]), int(pairs[0].split("-")[1]) + 1)
        )
        second_elf = set(
            range(int(pairs[1].split("-")[0]), int(pairs[1].split("-")[1]) + 1)
        )

        if (
            first_elf.intersection(second_elf) == second_elf
            or second_elf.intersection(first_elf) == first_elf
        ):

            fully_contained += 1

    return str(fully_contained)


def test() -> str:

    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
