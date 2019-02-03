# -*- coding: utf-8
import json
import sqlite3

def make_title(obj):
    title = u'{}'.format(obj['city'])
    if obj['subdiv1']:
        title += u', {} ({})'.format(obj['subdiv1'], obj['subdiv1_code'])

    if obj['subdiv2']: # subdiv2
        title += u', {} ({})'.format(obj['subdiv2'], obj['subdiv2_code'])

    title += u', {} ({})'.format(obj['country'], obj['country_code'])
    return title

def make_subtitle(obj):
    return u'{}, {}'.format(obj['continent'], obj['timezone'])

def search_city(wf, city):
    try:
        conn = sqlite3.connect('db/db.db')
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
        return

    for row in c.fetchall():
        obj = {
            'city':          row[0],
            'country':       row[1],
            'country_code':  row[2],
            'subdiv1':       row[3],
            'subdiv1_code':  row[4],
            'subdiv2':       row[5],
            'subdiv2_code':  row[6],
            'continent':     row[7],
            'timezone':      row[8],
        }
        wf.add_item(title = make_title(obj),
                    subtitle = make_subtitle(obj),
                    arg = json.dumps(obj),
                    valid = True,
                    icon = u'flags/{}.png'.format(obj['country'].lower(). replace(' ', '_'))
        )

