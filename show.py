# -*- coding: utf-8
import pendulum
import json

def make_title(obj, t, f):
    tz = pendulum.timezone(obj[8])
    if not f:
        f = 'h:mm A, MMM DD'

    title = u'{}: {}'.format(obj[0], tz.convert(t).format(f))
    return title

def make_subtitle(obj):
    return u'{} ({}) • {}'.format(obj[1], obj[2], obj[8])

def list_city(wf, city):
    citydb = wf.stored_data('citydb')
    if not citydb:
        wf.add_item(u'No city in database',
                    u'Please add a city using "timezone add [CITY NAME]"')
        return

    if not city: # show current time
        now = pendulum.now()
        for row in citydb:
            title = make_title(row, now, wf.stored_data('format'))
            wf.add_item(title = title,
                        subtitle = make_subtitle(row),
                        arg = title,
                        valid = True,
                        icon = 'flags/{}.png'.format(row[1].lower(). replace(' ', '_'))
            )
        return

    for row in citydb:
        wf.add_item(title = make_title(row),
                    subtitle = make_subtitle(row),
                    valid = True,
                    icon = 'flags/{}.png'.format(row[1].lower(). replace(' ', '_'))
        )
    return

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
