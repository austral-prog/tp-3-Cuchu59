def check_vowels():
    name = input('Ingrese un nombre: ')
    print('Contiene a: ' + str('a' in name.lower()))
    print('Contiene e: ' + str('e' in name.lower()))
    print('Contiene i: ' + str('i' in name.lower()))
    print('Contiene o: ' + str('o' in name.lower()))
    print('Contiene u: ' + str('u' in name.lower()))


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
