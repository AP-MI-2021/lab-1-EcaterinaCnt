from Repository.exceptii import DuplicateIdError
from Service.pictor_service import PictorService
from Service.tablou_service import TablouService


class Console:
    def __init__(self,
                 pictor_service: PictorService, tablou_service: TablouService):
        self.pictor_service =pictor_service
        self.tablou_service = tablou_service

    def show_menu(self):
        print('a[car|loc|ord] - adaugare masina sau locatie sau comanda.')
        print('s[car|loc|ord] - show all masina sau locatie sau comanda.')
        print('x. Iesire')

    def run_console(self):
        while True:
            self.show_menu()
            opt = input('Alegeti optiunea: ')
            if opt == 'ap':
                self.handle_add_pictor()
            elif opt == 'at':
                self.handle_add_tablou()
            elif opt == 'ord':
                self.handle_ordonare()
            elif opt == 'sp':
                self.handle_show_all(self.pictor_service.get_all())
            elif opt == 'st':
                self.handle_show_all(self.tablou_service.get_all())
            elif opt == 'an_dat':
                self.handle_gaseste_pictor_an_dat()
            elif opt == 'scump':
                self.handle_show_all(self.tablou_service.cel_mai_scump_tablou())
            elif opt == 'x':
                break
            else:
                print('Comanda invalida, reincearca.')

    def handle_add_pictor(self):
        try:
            id_pictor = input('Dati id-ul pictor: ')
            nume = input('Dati nume: ')
            stil = (input('Dati stil abstract clasic modern: '))
            CNP =input('CNP: ')

            self.pictor_service.add_pictor(id_pictor, nume, stil)
        except DuplicateIdError as de:
            print('ID Duplicat:', de)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_show_all(self, objects):
        for obj in objects:
            print(obj)


    def handle_add_tablou(self):
        try:
            id_tablou = input('Dati id-ul tablou: ')
            id_pictor = input('Dati id-ul pictor: ')
            titlu = input('Dati titlu: ')
            pret= float(input('Dati pret: '))
            an= int(input('Dati an: '))
            self.tablou_service.add_tablou(id_tablou, id_pictor, titlu, pret, an)
        except DuplicateIdError as de:
            print('ID Duplicat:', de)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_ordonare(self):
            an= int(input('Dati an: '))
            self.handle_show_all(self.tablou_service.ord_pictori_nr_tabl(an))

    def handle_gaseste_pictor_an_dat(self):
        anul = int (input('Dati anul: '))
        self.handle_show_all(self.tablou_service.gaseste_pictor_an_dat(anul))
