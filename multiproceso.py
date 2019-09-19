import os
from multiprocessing import Pool

def multiplicar(valor1, valor2):
    valor = valor1 * valor2
    print(valor)
    return valor


if __name__ == '__main__':
    pass

    valores = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

    valores = [(2, 3)]

    print("Number of cpu : ", os.cpu_count())
    with Pool(processes=os.cpu_count()) as pool:
        results = pool.starmap(multiplicar, valores)

        outputs = [result for result in results]
        print(outputs)


