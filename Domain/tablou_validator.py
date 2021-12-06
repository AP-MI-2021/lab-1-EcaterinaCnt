from Domain.tablou import Tablou


class ValidareTablou:
    def validare_tablou(self, tablou: Tablou):
        erori = []
        if tablou.id_pictor is None:
            erori.append('id-ul nu poate fi nul')
        if tablou.titlu =='':
            erori.append('titlul nu poate fi gol')
        if tablou.pret <=0:
            erori.append('pretul nu poate fi negatv')
        if tablou.an <=0:
            erori.append('anul nu poate fi negativ')
        if erori:
            raise ValueError(erori)
