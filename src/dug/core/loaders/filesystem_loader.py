from pathlib import Path
from typing import Iterator

from ._base import InputFile


def load_from_filesystem(filepath: InputFile) -> Iterator[Path]:

    filepath = Path(filepath)

    if not filepath.exists():
        raise ValueError(f"Unable to locate {filepath}")

    if filepath.is_file():
        yield filepath
    else:
        yield from filepath.glob("**/*")
