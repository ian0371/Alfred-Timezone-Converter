import json
import sqlite3

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
        return

    for row in c.fetchall():
        wf.add_item(title = make_title(row),
                    subtitle = make_subtitle(row),
                    arg = json.dumps(row),
                    valid = True
        )

