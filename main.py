import requests
import json
import psycopg2
from pathlib import Path
from dotenv import dotenv_values


def create_cannabis_db(database, user, password, host, port):
    conn = psycopg2.connect(
        database=f'{database}', user=f'{user}', password=f'{password}', host=f'{host}', port=f'{port}'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS cannabis (
        id int PRIMARY KEY,
        uid varchar(255) NOT NULL,
        strain varchar(255) NOT NULL,
        cannabinoid_abbreviation varchar(255) NOT NULL,
        cannabinoid varchar(255) NOT NULL,
        terpene varchar(255) NOT NULL,
        medical_use varchar(255) NOT NULL,
        health_benefit varchar(255) NOT NULL,
        category varchar(255) NOT NULL,
        type varchar(255) NOT NULL,
        buzzword varchar(255) NOT NULL,
        brand varchar(255) NOT NULL
        );''')
    except SyntaxWarning:
        print('Create table error')


def insert_values(database, user, password, host, port, values: list):
    conn = psycopg2.connect(
        database=f'{database}', user=f'{user}', password=f'{password}', host=f'{host}', port=f'{port}'
    )
    conn.autocommit = True
    cursor = conn.cursor()

    for value in values:
        cursor.execute(f'''INSERT INTO cannabis (id, uid, strain, cannabinoid_abbreviation, cannabinoid, 
                    terpene, medical_use, health_benefit, category, type, buzzword, brand)
                    VALUES ({value['id']}, '{value['uid']}', '{value['strain']}', 
                    '{value['cannabinoid_abbreviation']}', '{value['cannabinoid']}', '{value['terpene']}', 
                    '{value['medical_use']}', '{value['health_benefit']}', '{value['category']}', '{value['type']}', 
                    '{value['buzzword']}', '{value['brand'].replace("'", '"')}');''')

    conn.commit()
    conn.close()


def get_values(url):
    get_items = requests.get(url)
    text = get_items.text
    t = json.loads(text)
    return t


def main():
    url = 'https://random-data-api.com/api/cannabis/random_cannabis?size=10'
    values = get_values(url)
    auth = dotenv_values(Path(__file__).resolve().parent / '.env')
    database = auth['database']
    user = auth['user']
    password = auth['password']
    host = auth['host']
    port = auth['port']
    create_cannabis_db(database, user, password, host, port)
    insert_values(database, user, password, host, port, values)


if __name__ == '__main__':
    main()
