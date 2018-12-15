# encoding: utf-8
import csv
import json
import sqlite3

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

def make_title(obj):
    title = u'{0}'.format(*obj)
    if obj[3]: # subdiv1
        title += u', {3} ({4})'.format(*obj)

    if obj[5]: # subdiv2
        title += u', {5} ({6})'.format(*obj)

    title += u', {1} ({2})'.format(*obj)
    return title

def make_subtitle(obj):
    return u'{7}, {8}'.format(*obj)

def list_city(wf, city):
    citydb = wf.stored_data('citydb')
    if not citydb:
        wf.add_item(u'No city in database',
                    u'Please add a city using "timezone add [CITY NAME]"')

    for row in citydb:
        wf.add_item(title = make_title(row),
                    subtitle = make_subtitle(row),
                    valid = True
        )

def search_city(wf, city):
    try:
        conn = sqlite3.connect('db.db')
        c = conn.cursor()
        q = '''SELECT `city`.`name`, `country`.`name`, `country`.`code`,
                      `subdiv1_name`, `subdiv1_code`,
                      `subdiv2_name`, `subdiv2_code`,
                      `continent`.`name`, `timezone`
               FROM `city`
               LEFT JOIN `country`
                   ON `city`.`country_code` = `country`.`code`
               LEFT JOIN `continent`
                   ON `country`.`continent_code` = `continent`.`code`
               WHERE `city`.`name` LIKE ? LIMIT 25;'''
        c.execute(q, ['%'+city+'%'])
    except:
        pass

    for row in c.fetchall():
        wf.add_item(title = make_title(row),
                    subtitle = make_subtitle(row),
                    arg = json.dumps(row),
                    valid = True
        )

def add_city(wf, obj):
    citydb = wf.stored_data('citydb')
    obj = json.loads(obj)
    if not citydb:
        citydb = [obj]
    else:
        citydb.append(obj)
    wf.store_data('citydb', citydb)

def clear_db(wf):
    wf.store_data('citydb', None)
