
""" OpenWeatherMap (экспорт)
Сделать скрипт, экспортирующий данные из базы данных погоды,
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.
Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]

При выгрузке в html можно по коду погоды (weather.id) подтянуть
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions
Экспорт происходит в файл filename.
Опционально можно задать в командной строке город. В этом случае
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.
"""

import csv
import json
import sqlite3
import argparse

import hw08_openweather as ow

w = ow.Weather()
def get_data(city, country_code='RU'):
    data = w.get_data(city, country_code)
    if data:
        return data
    else:
        raise IOError('No such information in the database')

if __name__ == '__main__':
    print('''Hint:
        export_openweather.py --csv filename [<город>]
        export_openweather.py --json filename [<город>]
        export_openweather.py --html filename [<город>]
    ''')

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str,
        help='specify filename for output')
    parser.add_argument("--csv",  action='store_true', help='output csv')
    parser.add_argument("--json", action='store_true', help='output json')
    parser.add_argument("--html", action='store_true', help='output html')
    args = parser.parse_args()

    data = get_data(args.filename)

    if args.csv:
        with open(args.filename+'.csv', 'w') as csvfile:
            fieldnames = data[0]._asdict().keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({i:i for i in fieldnames})
            for row in data:
                writer.writerow(row._asdict())

    elif args.json:
        with open(args.filename+'.json', 'w') as jfile:
            new_list = []
            for row in data:
                new_list.append(row._asdict())
            j_obj = json.dumps(new_list)
            json.dump(j_obj, jfile)

    elif args.html:
        from yattag import Doc

        doc, tag, text = Doc().tagtext()

        with tag('html'):
            with tag('body'):
                for row in data:
                    with tag('p', id = 'main'):
                        text(str(row))

        result = doc.getvalue()
        with open(args.filename+'.html', 'w') as hfile:
            hfile.write(result)

