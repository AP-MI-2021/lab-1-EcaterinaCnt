from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Pictor(Entity):
    nume: str
    stil: str
