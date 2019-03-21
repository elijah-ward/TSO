"""
Exporter

The main function of this module is to provide a method in which we will be exporting data from scheduling.

The simple case is exporting to the console.
The more complex case is exporting it to a reusable file for CFHT Schedulers
"""


def export_to_console(schedule):
    print(schedule)


def export_to_file(schedule):
    print("Printing To File Now!~")
    export_to_console(schedule)
