# -*- coding: utf-8
import pendulum
import json
import re

def parse(base, args):
    '''
    :param base: pendulum.datetime
    :param args: string
    :rtype: tuple (pendulum.datetime, string)
    '''
    pat = re.compile('^(\d{1,2})([/:])?(?(2)(\d{1,2}))$')
    ret = base
    city = ''

    for arg in args:
        result = re.match(pat, arg)
        if not result:
            city += arg + ' '

        elif result.group(2) == ':':
            ret = ret.set(hour = int(result.group(1)), minute = int(result.group(3)))

        elif result.group(2) == '/':
            ret = ret.set(month = int(result.group(1)), day = int(result.group(3)))

        else: # only number
            ret = ret.set(day = int(result.group(1)))

    return ret, city.rstrip()

def get_city_obj_by_name(db, name):
    '''
    :param db: list
    :param name: string
    :rtype: dict
    '''
    for obj in db:
        if obj['city'] == name:
            return obj
    return None

def set_format(dt, obj, f):
    title = u'{}: {}'.format(obj['city'], dt.format(f))
    subtitle = u'{} ({}) • {}'.format(obj['country'], obj['country_code'], obj['timezone'])
    icon = 'flags/{}.png'.format(obj['country'].lower().replace(' ', '_'))
    return (title, subtitle, icon)

def show_times(wf, args):
    '''
    :param args: string
    '''
    db = wf.stored_data('citydb')
    if not db:
        wf.add_item(u'No city in database',
                    u'Please add a city using "timezone add [CITY NAME]"',
                    valid = False)
        return

    now = pendulum.now()
    now, city = parse(now, args)
    if city:
        tmp = get_city_obj_by_name(db, city)
        if not tmp:
            wf.add_item(u'No such city in database',
                        u'Please add the city using "timezone add [CITY NAME]"',
                        valid = False)
            return
        now = now.in_timezone(tmp['timezone'])

    f = 'h:mm A, MMM DD'
    for obj in db:
        dst = now.in_tz(obj['timezone'])
        title, subtitle, icon = set_format(dst, obj, f)
        wf.add_item(title = title,
                    subtitle = subtitle,
                    arg = title,
                    valid = True,
                    icon = icon)

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
