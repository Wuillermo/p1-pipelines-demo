from calculadora import suma

def test_suma_basica():
    assert suma(2, 3) == 5

def test_suma_negativos():
    assert suma (-1, -2) == -3