import csv
import collections
import argparse

DATA_IN_COLUMN = []


def filtered_csv(file_csv, ent_column):
    global DATA_IN_COLUMN
    with open(file_csv, newline='') as file_:
        input_data = csv.DictReader(file_)
        data = [file[ent_column] for file in input_data]
        key_data = list(collections.OrderedDict.fromkeys(data))
        DATA_IN_COLUMN = [[row] for row in key_data]


def upload(out_csv):
    with open(out_csv, "w", newline='') as file_:
        uploading = csv.writer(file_)
        uploading.writerows(DATA_IN_COLUMN)
    file_.close()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Este Script filtra los csv que contengan la lista de jurisdicciones")
    parser.add_argument(
        "file_csv", help="Archivo de entrada csv")
    parser.add_argument(
        "ent_column", help="Nombre de columna de jurisdicciones")
    parser.add_argument(
        "out_csv", help="Archivo csv de salida")
    return parser.parse_args()


def main():
    args = parse_args()
    filtered_csv(args.file_csv, args.ent_column)
    upload(args.out_csv)


if __name__ == "__main__":
    main()
