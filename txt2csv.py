# coding=utf-8
import csv
import codecs


def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')


with codecs.open("../duowan_user.txt", 'r', "gbk") as f1, open("duowan_output.csv", 'wb') as f2:
    dialect = csv.Sniffer().sniff(f1.read(1024))
    f1.seek(0)
    print(dialect.delimiter)
    lineCount = 0
    while True:
        lines = f1.readlines(1000)
        if not lines:
            break
        # reader = csv.reader(lines,delimiter=dialect.delimiter)
        reader = csv.reader(utf_8_encoder(lines), delimiter=dialect.delimiter)
        writer = csv.writer(f2, delimiter=',')
        for row in reader:
            writer.writerow(row)
            # writer.writerow([unicode(s).encode("utf-8") for s in row])
            lineCount += 1
            print row
            print lineCount
            # rows = csv.reader(f1, delimiter=dialect.delimiter)
            # writer = csv.writer(f2,delimiter=',')
            # writer.writerows(rows)
