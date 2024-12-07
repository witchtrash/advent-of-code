import inspect
from pathlib import Path


class Input:
    __raw: str

    def __init__(self, path: Path):
        with open(path) as f:
            self.__raw = f.read()

    def raw(self, strip: bool = False) -> str:
        return self.__raw.strip() if strip else self.__raw

    def lines(self) -> list[str]:
        return self.raw(strip=True).split("\n")

    def ints(self) -> list[int]:
        return list(map(int, self.lines()))

    def csv(self) -> list[str]:
        return self.raw(strip=True).split("\n")[0].split(",")


def get_problem_input(test: bool = False) -> Input:
    """
    Get problem input automagically

    Note that input files have to be named input.a|b or test.a|b
    """

    caller_file = inspect.stack()[1].filename

    part = Path(caller_file).stem.split(".")[0]
    input_file_name = f"test.{part}" if test else f"input.{part}"

    input_path = Path(caller_file).parent / input_file_name

    return Input(input_path)
