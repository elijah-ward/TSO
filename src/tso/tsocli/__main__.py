"""
TSO CLI

This is the main entry into the application.
The initial configuration into this file is through the projects setup.py

This is meant to be as minimal as possible.
With other functions in this module as primary containers of the complexity
"""

import sys
import argparse
import os
import json
import datetime
from sys import maxsize as MAX_SIZE


from . import command as tso_command
from configuration import configuration_parser


def initialize_sub_parser(sub_parser):
    schedule_parser = sub_parser.add_parser(
        "schedule",
        aliases=['s'],
        help="Schedule: schedule observations"
    )

    add_arguments(schedule_parser)

    schedule_parser.set_defaults(
        command=tso_command.cli_pipeline
    )

    return schedule_parser


def add_arguments(parser):
    parser.add_argument(
        "--config-file",
        default="tso_config.json",
        help="The local path to your runtime config file (See the included tso_config.json for an example of format)"
    )
    parser.add_argument(
        "--start-date-time",
        default=datetime.datetime.now(),
        help="The date time to begin the scheduling"
    )
    parser.add_argument(
        "--end-date-time",
        default=datetime.datetime.now() + datetime.timedelta(days=7),
        help="The date time to end the scheduling"
    )
    parser.add_argument(
        "--max-program-priority",
        default=MAX_SIZE,
        help="The maximum program priority to query against (1 is highest priority)"
    )
    parser.add_argument(
        "--max-observation-priority",
        default=MAX_SIZE,
        help="The maximum block priority to query against (1 is highest priority)"
    )
    parser.add_argument(
        "--max-remaining-observing-chances",
        default=MAX_SIZE,
        help="Include only those blocks whose remaining observing chances is less than this value"
    )
    parser.add_argument(
        "--observation-duration-min",
        default=0,
        help="Include only those blocks whose duration is greater than or equal to this"
    )
    parser.add_argument(
        "--observation-duration-max",
        default=MAX_SIZE,
        help="Include only those blocks whose duration is less than or equal to this"
    )
    parser.add_argument(
        "--no-weather-constraints",
        help="Whether weather should be imported for this schedule",
        action="store_true"
    )
    parser.add_argument(
        "--export-to-file",
        help="Whether to export to a file or not",
        action='store_true'
    )
    parser.add_argument(
        "--export-to-browser",
        help="Display schedule in browser",
        action='store_true'
    )


def main(sys_args=None):
    if sys_args is None:
        sys_args = sys.argv[1:]

    tso_epilog = """
         ______________
        /_  __/ __/ __ \\
         / / _\ \/ /_/ /
        /_/ /___/\____/
        ---------------
        Observe Freely
        ---------------"""
    tso_parser = argparse.ArgumentParser(
        prog="tsocli",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="TSO (Telescope Scheduling Optimizer): Import, Schedule, Optimize, Export",
        epilog=tso_epilog
    )

    subparsers = tso_parser.add_subparsers(dest="which")

    main_sub_parser = initialize_sub_parser(subparsers)

    args = tso_parser.parse_args(sys_args)

    # Display the hep if no arguments are passed
    if len(sys_args) == 0:
        tso_parser.print_help(sys.stderr)
        sys.exit(1)
    elif (args.which == 's' or args.which == 'schedule') and len(sys_args) == 1:
        main_sub_parser.print_help()
        sys.exit(1)

    # Load the supplied config file
    if args.config_file is not None:
        config = configuration_parser.parse(args.config_file)

    # Call the Pipeline with all arguments and the loaded config file
    args.command(args, config)
