import argparse
import csv

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--archivo", help='Archivo CSV a utilizar', default='semana_de_noticias.csv')
    #parser.add_argument("--config", help='Base a utilizar, prod y desa', default='configuration.json')
    
    args = parser.parse_args()

    #print (args.archivo)

def openCsv(file):
    resultado = set([])
    with open(file, newline='', encoding="utf8") as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        for fila in reader:
            for x in fila:
                if 'youtube.com' in x:
                    for y in (x.split()):
                        if 'youtube' in y:
                            if not 'google' in y:
                                resultado.add(y)
        for x in resultado:
            print(x)

openCsv(args.archivo)




