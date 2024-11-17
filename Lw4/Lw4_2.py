# TODO импортировать необходимые молули
import csv
import json
import collections
from idlelib.iomenu import encoding

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(INPUT_FILENAME, OUTPUT_FILENAME) -> None:
      # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as infi:
        lines = [collections.OrderedDict(line) for line in csv.DictReader(infi)]

      # TODO Сериализовать в файл с отступами равными 4

        #print(a)
        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as oufi:
            json.dump(lines, oufi, indent=4)
            oufi.close()

if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
