from Domain.pictor import Pictor
from Domain.pictor_validator import ValidarePictor
from Repository.repository import Repository


class PictorService:
    def __init__(self,
                 pictor_repository: Repository,
                 pictor_validator: ValidarePictor):
        self.pictor_repository = pictor_repository
        self.pictor_validator = pictor_validator

    def add_pictor(self,
                id_pictor: str,
                nume: str,
                stil: str):
        """
        TODO
        """
        pictor = Pictor(id_pictor, nume, stil)
        self.pictor_validator.validare_pictor(pictor)
        self.pictor_repository.create(pictor)

    def get_all(self):
        return self.pictor_repository.read()

