lass carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def acelerar(self):
        print('o carro esta acelerando.')
    def frear(self):
        print('o carro esta freando.')

#exemplo de criaçao de abjetos a partir de uma classe:

carro1 = carro('ford', 'mustang')
carro2 = carro('chevrolet', 'camaro')

#exemplo de acesso a tributos e chamada de metodos 
print(carro1.marca)      #saida: ford
print(carro2.modelo)     #saida: camaro

carro1.acelerar()       #saida: o carro esta acelerando.
carro2.frear()          #saida: o carro esta freando.


class carroEsportivo(carro):
    def __init__(self, marca, modelo, potencia):
        super().__init__(marca, modelo)
        self.potencia = potencia

    def turbo(self):
        print('ativando o turbo!')

carro_esportivo  = carroEsportivo('ferrari', '458 italia', 570)
carro_esportivo.acelerar()  #saida : carro esta acelerando.
carro_esportivo.turbo()      #saida :