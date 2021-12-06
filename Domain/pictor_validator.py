from Domain.pictor import Pictor
from Repository.repository import Repository


class ValidarePictor:
    def validare_pictor(self, pictor: Pictor):
        erori= []
        if pictor.nume =='':
            erori.append('Numele nu poate fi gol.')
        if pictor.stil not in ['abstract', 'clasic', 'modern']:
            erori.append('Stilul poate fi doar abstract, clasic, modern')
        if erori:
            raise ValueError(erori)
