import importlib
from enum import Enum
from os import mkdir
from pathlib import Path
from shutil import copy
from time import perf_counter_ns
from typing import cast
from typing_extensions import Annotated
from rich import print

import typer

from solver import Solver

app = typer.Typer(
    help="Advent of Code",
    add_completion=False,
)


class Part(str, Enum):
    part_a = "a"
    part_b = "b"


@app.command()
def solve(
    year: int,
    day: int,
    part: Part,
    test: bool = False,
) -> None:
    """
    Run a solution.
    """
    try:
        solution = cast(
            Solver, importlib.import_module(f"{year}.day{day}.{part.value}")
        )

        timer_start = perf_counter_ns()
        res = solution.test() if test else solution.run()
        timer_stop = perf_counter_ns()
        delta = timer_stop - timer_start

        print(f"[green]Result: {res}[/]")
        print(f"[blue]Run time: {delta / 1000 ** 2}[/]")

    except ModuleNotFoundError:
        print(f"[bold red]:boom: Solution not found.[/]")


@app.command()
def scaffold(
    year: Annotated[
        int, typer.Argument(help="Which year to scaffold the solution for.")
    ],
    day: Annotated[int, typer.Argument(help="Which day")],
) -> None:
    """
    Scaffold a new solution
    """

    base_path = Path("advent-of-code")
    solution_path = base_path / f"{year}" / f"day{day}"
    template_path = base_path / "template.py"

    try:
        mkdir(solution_path)

        copy(template_path, solution_path / "a.py")
        copy(template_path, solution_path / "b.py")
    except FileExistsError:
        print(f"[bold yellow]:warning: Directory {year}/day{day} already exists.[/]")

    (solution_path / "input.a").touch()
    (solution_path / "input.b").touch()
    (solution_path / "test.a").touch()
    (solution_path / "test.b").touch()

    print("[blue]Done![/]")


if __name__ == "__main__":
    app()
