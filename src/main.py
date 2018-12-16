# -*- coding: utf-8
from sys import exit
from workflow import Workflow3
from optparse import OptionParser
from show import *
from search import *

def main(wf):
    parser = OptionParser()
    parser.add_option(
        '-a',
        '--add',
        help    = 'Add a city',
        metavar = 'CITY_NAME',
        type    = 'string',
        dest    = 'add_city'
    )
    parser.add_option(
        '-s',
        '--search',
        help    = 'Searcy a city',
        metavar = 'CITY_NAME',
        type    = 'string',
        dest    = 'search_city'
    )
    parser.add_option(
        '-c',
        '--clear',
        help    = 'Remove all the saved cities',
        action  = 'store_true',
        dest    = 'clear'
    )

    options, args = parser.parse_args()

    if options.search_city:
        search_city(wf, options.search_city)
    elif options.add_city:
        add_city(wf, options.add_city)
    elif options.clear:
        clear_db(wf)
    else:
        show_times(wf, args)

    # Send the results to Alfred as XML
    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow3()
    exit(wf.run(main))
