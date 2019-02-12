import csv

def csv_create():
    headers = ('id', 'name', 'age')
    rows = [('1001', 'tom', 10), ('2002', 'jerry', 8)]
    with open('wtf.csv', 'w', newline='') as f:
        f_csv = csv.writer(f )
        f_csv.writerow(headers)
        f_csv.writerows(rows)


def csv_read():
    with open('wtf.csv', 'r') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        print(headers)
        for row in f_csv:
            print(row)

if __name__ == '__main__':
    csv_read()