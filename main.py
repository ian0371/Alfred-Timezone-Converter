# -*- coding: utf-8
from sys import exit
from workflow import Workflow3
from optparse import OptionParser
from tzconv import *

__version__ = '1.1'

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
    wf = Workflow3(update_settings={
        # Your username and the workflow's repo's name.
        'github_slug': 'ian0371/Alfred-Timezone-Converter',

        # The version (i.e. release/tag) of the installed workflow.
        # If you've set a Workflow Version in Alfred's workflow
        # configuration sheet or if a `version` file exists in
        # the root of your workflow, this key may be omitted
        'version': __version__,

        # Optional number of days between checks for updates.
        'frequency': 7,

        # Force checking for pre-release updates.
        # This is only recommended when distributing a pre-release;
        # otherwise allow users to choose whether they want
        # production-ready or pre-release updates with the
        # `prereleases` magic argument.
        'prereleases': '-beta' in __version__
    })

    if wf.update_available:
        # Download new version and tell Alfred to install it
        wf.start_update()
    exit(wf.run(main))
