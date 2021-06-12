import csv
import collections
import argparse


data = []
data_in_column =[]

def filtered(file_csv,ent_column):
    with open(file_csv, newline='') as File:
        input_data = csv.reader(File)

        for i, file in enumerate(input_data):
            if i == 0:
                column_data = file.index(ent_column)
                data.append(file[column_data])
            if i > 0:
                data.append(file[column_data])

        key_data = list(collections.OrderedDict.fromkeys(data))

        for i,key in enumerate(key_data):
            data_in_column.append([key])

def upload(out_csv):
    with open(out_csv, "w", newline='') as file:
        cargar = csv.writer(file)
        cargar.writerows(data_in_column)
    file.close()

def parse_args():
    parser = argparse.ArgumentParser(description = "Este Script sirve para filtrar los csv que contengan una lista de jurisdicciones")
    parser.add_argument("file_csv", help="Archivo de entrada csv")
    parser.add_argument("ent_column", help="Nombre de columna de jurisdicciones")
    parser.add_argument("out_csv", help="Archivo csv de salida")
    return parser.parse_args()


def main():
    args = parse_args()
    filtered(args.file_csv,args.ent_column)
    upload(args.out_csv)


if __name__ == "__main__":
    main()
