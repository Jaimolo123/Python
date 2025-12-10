



def calcularPizza(tamanio, *args):

        if tamanio < 1 or  len(args)< 1:
            raise TypeError('Tamaño y los ingredientes deben de ser mayor que 1')

        return f"Has escogido una piza de {tamanio} porciones y con estos ingredientes {args}"

try:
  resul =  calcularPizza(3, "queso", "oregano", "tomate")
  print(resul)
except TypeError as e:
    print(e)

