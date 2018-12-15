# encoding: utf-8
import csv
import json

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

def list_city(wf, city):
    citydb = wf.stored_data('citydb')
    if not citydb:
        wf.add_item(u'No city in database',
                    u'Please add a city using "timezone add [CITY NAME]"')
        return

    for obj in citydb:
        wf.add_item(title = u'{}, {} ({})'
                            .format(obj['city'],
                                    obj['country'],
                                    obj['country_code']),
                    subtitle = u'{}, {}'
                               .format(obj['continent'],
                                       obj['tz']),
                    arg = json.dumps(obj),
                    valid = True
        )

def search_city(wf, city):
    with open('GeoLite2-City-Locations-en.csv', 'rt') as f:
        csvparser = csv.reader(f, delimiter=',')
        cnt = 0
        for row in csvparser:
            row = map(lambda x:unicode(x, 'utf-8'), row)
            if row[CITY_NAME_IDX].lower().startswith(city.lower()):
                obj = {'city': row[CITY_NAME_IDX],
                       'country': row[COUNTRY_NAME_IDX],
                       'country_code': row[COUNTRY_ISO_CODE_IDX],
                       'continent': row[CONTINENT_NAME_IDX],
                       'tz': row[TIME_ZONE_IDX],
                       }
                wf.add_item(title = u'{}, {} ({})'
                                    .format(obj['city'],
                                            obj['country'],
                                            obj['country_code']),
                            subtitle = u'{}, {}'
                                       .format(obj['continent'],
                                               obj['tz']),
                            arg = json.dumps(obj),
                            valid = True
                )
                cnt += 1
            if cnt > 20:
                break

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
