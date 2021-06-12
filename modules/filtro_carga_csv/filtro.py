import csv
import collections
import argparse

data = []
data_in_column = []

def filtered_csv(file_csv, ent_column):
    global data
    global data_in_column
    with open(file_csv, newline = '') as File:
        input_data = csv.DictReader(File)
        for file in input_data:
            data.append(file[ent_column])
        key_data = list(collections.OrderedDict.fromkeys(data))
        data_in_column = [[row] for row in key_data]

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
    filtered_csv(args.file_csv, args.ent_column)
    upload(args.out_csv)

if __name__ == "__main__":
    main()
