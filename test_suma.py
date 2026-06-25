def suma(a,b):
    return a+b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b
def es_par(numero):
    return numero % 2 == 0
def test_all():
    assert suma(5,5) == 10
    assert multiplicar(5,5) == 25
    assert dividir(10,2)
    assert dividir(10,0)
    assert es_par(2)
    assert es_par(3)
    
test_all()
print("Prueba Exitosa")