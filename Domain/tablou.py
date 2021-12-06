from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Tablou(Entity):
    id_pictor: str
    titlu: str
    pret: float
    an: int
