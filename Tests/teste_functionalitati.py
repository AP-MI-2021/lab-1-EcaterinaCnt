from Domain.pictor import Pictor
from Domain.pictor_validator import ValidarePictor
from Domain.tablou_validator import ValidareTablou
from Repository.repository_json import JsonRepository
from Service.pictor_service import PictorService
from Service.tablou_service import TablouService


def run_all_tests():
    test_adauga_pictor()
    test_adauga_tablou()
    test_ordonare_tablouri()


def clear_file(filename):
    with open (filename, 'w') as f:
        pass

def test_adauga_pictor():
    clear_file('test_pictor.json')
    pictor_repository = JsonRepository('test_pictor.json')
    pictor_validator = ValidarePictor()
    pictor_service = PictorService(pictor_repository, pictor_validator)

    pictor_service.add_pictor('1','f','abstract')
    pictor_service.add_pictor('2','g','clasic')

    pictori = pictor_service.get_all()
    assert len(pictori)==2
    assert pictori[0].id_entity == '1'
    assert pictori[1].id_entity == '2'
    assert pictori[0].nume == 'f'

def test_adauga_tablou():
    clear_file('test_pictor.json')
    pictor_repository = JsonRepository('test_pictor.json')
    pictor_repository.create(Pictor('1','f','abstract'))
    pictor_repository.create(Pictor('2','g','clasic'))

    clear_file('test_tablouri.json')
    tablou_repository = JsonRepository('test_tablouri.json')
    tablou_validator = ValidareTablou()
    tablou_service = TablouService(tablou_repository, tablou_validator, pictor_repository)
    tablou_service.add_tablou('1', '2', 'k', 2000, 2002)
    tablouri = tablou_service.get_all()

    assert len(tablouri)==1
    assert tablouri[0].id_entity == '1'
    assert tablouri[0].pret == 2000

def test_ordonare_tablouri():
    clear_file('test_pictor.json')
    pictor_repository = JsonRepository('test_pictor.json')
    pictor_repository.create(Pictor('1', 'f', 'abstract'))
    pictor_repository.create(Pictor('2', 'g', 'clasic'))
    pictor_repository.create(Pictor('3', 'h', 'modern'))

    clear_file('test_tablouri.json')
    tablou_repository = JsonRepository('test_tablouri.json')
    tablou_validator = ValidareTablou()
    tablou_service = TablouService(tablou_repository, tablou_validator,
                                   pictor_repository)
    tablou_service.add_tablou('1', '2', 'k', 2000, 2002)
    tablou_service.add_tablou('2', '2', 'l', 2001, 2010)
    an = 2000
    tablouri_ordonate = tablou_service.ord_pictori_nr_tabl(an)
    assert tablouri_ordonate[0]['Pictor'].id_entity =='2'
    assert tablouri_ordonate[0]['nr_tab']==2




