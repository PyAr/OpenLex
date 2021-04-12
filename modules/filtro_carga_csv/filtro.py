import csv
import collections
import argparse


dato = []
dato_in_column =[]

def filtrado(archivo_csv,ent_column):
    with open(archivo_csv, newline='') as File:
        input_data = csv.reader(File)

        for i, file in enumerate(input_data):
            if i == 0:
                column_dato = file.index(ent_column)
                dato.append(file[column_dato])
            if i > 0:
                dato.append(file[column_dato])

        key_dato = list(collections.OrderedDict.fromkeys(dato))

        for i,key in enumerate(key_dato):
            dato_in_column.append([key])

def cargado(sal_csv):
    with open(sal_csv, "w", newline='') as file:
        cargar = csv.writer(file)
        cargar.writerows(dato_in_column)
    file.close()

def parse_args():
    parser = argparse.ArgumentParser(description = "Este Script sirve para filtrar los csv que contengan una lista de jurisdicciones")
    parser.add_argument("archivo_csv", help="Archivo de entrada csv")
    parser.add_argument("ent_column", help="Nombre de columna de jurisdicciones")
    parser.add_argument("sal_csv", help="Archivo csv de salida")
    return parser.parse_args()


def main():
    args = parse_args()
    filtrado(args.archivo_csv,args.ent_column)
    cargado(args.sal_csv)


if __name__ == "__main__":
    main()
