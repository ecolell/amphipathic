import enum
from typing import Dict
from amphipathic.hydrophobic import cornette


class Author(enum.Enum):
    CORNETTE = 'cornette'


def select_table(
    author: Author = Author.CORNETTE,
    normalized: bool = True,
    scale: str = 'PRIFT',
) -> Dict[str, float]:
    table = {}
    if author == Author.CORNETTE:
        table = cornette.select_table(
            normalized=normalized,
            scale=scale,
        )
    return table
