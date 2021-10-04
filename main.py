def get_minim(a, b, c):
    '''
    Determina minimul a 3 numere.
    Input:
    - a, b, c: intregi, numerele date
    Output:
    - minimul dintre a, b si c
    '''
    m = a
    if b < m:
        m = b
    if c < m:
        m = c
    return m

def is_prime(nr):
    '''
    TODO
    '''
    if nr < 2:
        return False
    for i in range(2, nr): # 2, 3, ..., nr - 1
        if nr % i == 0:
            return False

    return True

def test_is_prime():
    assert is_prime(-2) == False
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(15) == False
    assert is_prime(13) == True
    assert is_prime(103) == True
    assert is_prime(17*19) == False
    assert is_prime(666013) == True



def print_primes(lst):
    for i in range(len(lst)):
        if is_prime(lst[i]):
            print(f'Numarul {lst[i]} este prim')
        else:
            print(f'Numarul {lst[i]} nu este prim')

def get_nr_cu_cifrele_invers(nr):
    '''
    ...
    '''
    inv = []
    while nr:
        inv.append(str(nr % 10))
        nr = nr // 10

    return ''.join(inv)


def main():
    while True:
        print('1. Minimul a trei numere.')
        print('2. Determinare daca un nr e prim.')
        print('3. Afisare numerelor prime dintr-o lista.')
        print('4. Afisarea unui numar cu cifrele in ordine inversa.')
        print('x. Exit')
        optiune = input('Alegeti o optiune: ')
        if optiune == '1':
            nr1 = int(input('Dati primul numar: '))
            nr2 = int(input('Dati al doilea numar: '))
            nr3 = int(input('Dati al treilea numar: '))

            minim = get_minim(nr1, nr2, nr3)
            print(f'Minimul dintre {nr1}, {nr2}, {nr3} este {minim}')
        elif optiune == '2':
            nr = int(input('Numarul care doriti sa se verifice: '))
            if is_prime(nr):
                print('Numarul dat este prim!')
            else:
                print('Numarul dat nu este prim.')
        elif optiune == '3':
            numere_str = input('Dati numerele separate prin spatiu: ')
            numere_str_split = numere_str.split(' ')
            numere_int = []
            for nr_str in numere_str_split:
                numere_int.append(int(nr_str))
            print_primes(numere_int)
        elif optiune == '4':
            nr = int(input('Dati numarul: '))
            print('Cifrele in ordine inversa sunt:', get_nr_cu_cifrele_invers(nr))
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')
main()

