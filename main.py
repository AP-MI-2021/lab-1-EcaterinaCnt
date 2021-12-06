from Domain.pictor_validator import ValidarePictor
from Domain.tablou_validator import ValidareTablou
from Repository.repository_json import JsonRepository
from Service.pictor_service import PictorService
from Service.tablou_service import TablouService
from Tests.teste_functionalitati import run_all_tests
from User_Interface.console import Console


def main():

    pictor_repository = JsonRepository('pictori.json')
    pictor_validator =ValidarePictor()
    pictor_service = PictorService(pictor_repository, pictor_validator)

    tablou_repository = JsonRepository('tablou.json')
    tablou_validator = ValidareTablou()
    tablou_service = TablouService(tablou_repository,tablou_validator, pictor_repository)

    console = Console(pictor_service, tablou_service)
    console.run_console()

if __name__ == '__main__':
    run_all_tests()
    main()