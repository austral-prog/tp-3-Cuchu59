def slice_simple():
    texto = "Awesome"
    texto_low = texto.lower()
    print(texto_low[0:3])
    print(texto_low[2:5])
    print(texto_low[0:4] + texto_low[-3:]) # print(texto)  tambien funciona jeje


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
