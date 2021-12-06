from Domain.tablou import Tablou
from Domain.tablou_validator import ValidareTablou
from Repository.repository import Repository


class TablouService:
    def __init__(self,
                 tablou_repository: Repository,
                 tablou_validator: ValidareTablou,
                 pictor_repository: Repository,
                 ):
        self.tablou_repository = tablou_repository
        self.pictor_repository = pictor_repository
        self.tablou_validator = tablou_validator

    def add_tablou(self, id_tablou, id_pictor, titlu, pret, an):
        """
        TODO
        """
        tablou = Tablou(id_tablou, id_pictor, titlu, pret, an)
        self.tablou_repository.create(tablou)
        self.tablou_validator.validare_tablou(tablou)

    def get_all(self):
        return self.tablou_repository.read()


    def ord_pictori_nr_tabl(self, an):
        """
        {pictor: id_pictor, nr_tab: numarul de tablouri}
        """
        id_pict_nr_tab = {}
        for pictor in self.pictor_repository.read(): #pentru fiecare pictor
            id_pict_nr_tab[pictor.id_entity] = 0 #atribuie 0 in dictionar la fiecare id al pictorului
        for tablou in self.tablou_repository.read(): #pentru fiecare tablou
            if tablou.an>=an: #daca anul tabloului e mai mare decat anul dat
                id_pict_nr_tab[tablou.id_pictor] += 1 #numara tabloul
        resultat=[]
        for id_pictor in id_pict_nr_tab: #pentru fiecare id din dictionar creeaza
                                        # lista de dictionare cu detaliile pictorului
                                        #si numarul de tablouri
            resultat.append({'Pictor': self.pictor_repository.read(id_pictor), 'nr_tab': id_pict_nr_tab[id_pictor]})
        return sorted(resultat, key=lambda x: x['nr_tab'], reverse=True) #ordoneaza desc lista de dict dupa nr_tab

    def gaseste_pictor_an_dat(self, anul):
        '''
        Gaseste pictorii care au facut tablouri intr un an dat
        '''

        lst = []
        for tablou in self.tablou_repository.read():
            if tablou.an == anul:
                pictor = self.pictor_repository.read(tablou.id_pictor)
                lst.append({'pictor': pictor.id_entity, 'tablou': tablou.titlu})
        return lst

    def cel_mai_scump_tablou(self):
        lst = {} #luam o lista goala  in care vom pune cel mai scump tablou pr fiecare gen
        for tablou in self.tablou_repository.read(): #iau fiecare tablou
            pictor = self.pictor_repository.read(tablou.id_pictor) #iau fiecare pictor
            if pictor.stil not in lst: #daca stilul nu se gaseste in lst
                lst[pictor.stil] =tablou #atribui lui lst[stil] tabloul gasit
            for stil in lst:#parcurg lista cu tablouri
                pret = lst[stil].pret #atribui pretul fiecarui tablou dintr un anume stil
                if stil == pictor.stil: #daca stilul tabloului e egal cu stilul pictorului
                    if tablou.pret > pret:#daca petul tabloului e mai mare decat pretul deja gasit stilului x
                        lst[stil] = tablou #modific in dictionar si pun tabloul cu pretul mai mare
        new_list = [] #fac o lista noua
        for stil in lst: #pentru fiecare stil din dictionar
            new_list.append({"stil": lst, "pret":lst[stil].pret}) #adaug in lista tabloul din dictionar si pretul lui
        return new_list

