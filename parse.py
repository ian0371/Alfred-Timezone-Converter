import csv
import sys
import sqlite3

# geoname_id,locale_code,continent_code,continent_name,country_iso_code,country_name,subdivision_1_iso_code,subdivision_1_name,subdivision_2_iso_code,subdivision_2_name,city_name,metro_code,time_zone,is_in_european_union

GEONAME_ID_IDX             = 0
LOCALE_CODE_IDX            = 1
CONTINENT_CODE_IDX         = 2
CONTINENT_NAME_IDX         = 3
COUNTRY_ISO_CODE_IDX       = 4
COUNTRY_NAME_IDX           = 5
SUBDIVISION_1_ISO_CODE_IDX = 6
SUBDIVISION_1_NAME_IDX     = 7
SUBDIVISION_2_ISO_CODE_IDX = 8
SUBDIVISION_2_NAME_IDX     = 9
CITY_NAME_IDX              = 10
METRO_CODE_IDX             = 11
TIME_ZONE_IDX              = 12
IS_IN_EUROPEAN_UNION_IDX   = 13

def read_line():
    with open('GeoLite2-City-Locations-en.csv', 'rt') as f:
        csvparser = csv.reader(f, delimiter=',')
        for row in csvparser:
            row = map(lambda x:unicode(x, 'utf-8'), row)
            yield row

def create_conn():
    try:
        conn = sqlite3.connect('db.db')
    except:
        print("Failed to connect to db.db")
        sys.exit(1)
    return conn

def create_db(conn):
    try:
        c = conn.cursor()
        c.execute('.read db.sql')
        c.close()
    except:
        print("Failed to create table from db.sql")
        sys.exit(2)
    return conn

def insert_timezone(conn):
    c = conn.cursor()
    read_line() # truncate the first line

    for row in read_line():
        data = [row[TIME_ZONE_IDX]]
        if not all(data):
            continue

        q = 'INSERT INTO `timezone`(`timezone`) VALUES(?)'
        try:
            c.execute(q, data)
            conn.commit()
        except Exception as e:
            pass

def insert_continent(conn):
    c = conn.cursor()
    read_line() # truncate the first line

    for row in read_line():
        data = [row[CONTINENT_NAME_IDX], row[CONTINENT_CODE_IDX]]
        if not all(data):
            continue

        q = 'INSERT INTO `continent`(`name`, `code`) VALUES(?, ?)'
        try:
            c.execute(q, data)
            conn.commit()
        except Exception as e:
            pass

def insert_country(conn):
    c = conn.cursor()
    read_line() # truncate the first line

    for row in read_line():
        data = [row[COUNTRY_NAME_IDX], row[COUNTRY_ISO_CODE_IDX], row[CONTINENT_CODE_IDX]]
        if not all(data):
            continue

        q = 'INSERT INTO `country`(`name`, `code`, `continent_code`) VALUES(?, ?, ?)'
        try:
            c.execute(q, data)
            conn.commit()
        except Exception as e:
            pass

def insert_city(conn):
    c = conn.cursor()
    read_line() # truncate the first line

    for row in read_line():
        data = [row[CITY_NAME_IDX], row[COUNTRY_ISO_CODE_IDX],
                row[SUBDIVISION_1_NAME_IDX], row[SUBDIVISION_1_ISO_CODE_IDX],
                row[SUBDIVISION_2_NAME_IDX], row[SUBDIVISION_2_ISO_CODE_IDX],
                row[TIME_ZONE_IDX]]
        if not all([data[0], data[1], data[-1]]):
            continue

        q = '''INSERT INTO `city`(`name`, `country_code`,
                                `subdiv1_name`, `subdiv1_code`,
                                `subdiv2_name`, `subdiv2_code`,
                                `timezone`)
             VALUES(?, ?, ?, ?, ?, ?, ?)'''
        try:
            c.execute(q, data)
            conn.commit()
        except Exception as e:
            pass

def main():
    conn = create_conn()
    # create_db(conn)
    insert_continent(conn)
    insert_timezone(conn)
    insert_country(conn)
    insert_city(conn)

if __name__ == "__main__":
    main()
