"""
Exporter

The main function of this module is to provide a method in which we will be exporting data from scheduling.

The simple case is exporting to the console.
The more complex case is exporting it to a reusable file for CFHT Schedulers
"""

import pandas
from astropy.table.jsviewer import DEFAULT_CSS

custom_css = """
body::before {
    content: "TSO | Observe Freely";
    position: absolute;
    top: 0;
    font-size: 50px;
    margin-top: 25px;
    margin-left: 40px;
    font-weight: bold;
    font-family: monospace;
}
body {
    margin-top: 150px;
    background-color: rgb(230, 230, 230);
    margin-left: 30px;
}
"""


def export_to_console(schedule):
    print(schedule.to_table())


def export_to_file(schedule):
    print("Printing schedule to file...")
    schedule_table = schedule.to_table()
    schedule_df = schedule_table.to_pandas()
    schedule_df.to_csv('./schedule.csv')


def export_to_browser(schedule):
    print("Displaying schedule in browser...")
    schedule_table = schedule.to_table()
    schedule_table.show_in_browser(
        jsviewer=True,
        css=DEFAULT_CSS+custom_css
    )
    # there is also show_in_notebook if we want to use an ipy thing

