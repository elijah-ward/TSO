"""
TSO CLI

This is the main entry into the application.
The initial configuration into this file is through the projects setup.py

This is meant to be as minimal as possible.
With other functions in this module as primary containers of the complexity
"""

import sys
import argparse

from . import command as tso_command


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
        "--startDateTime",
        help="The date time to begin the scheduling"
    )
    parser.add_argument(
        "--endDateTime",
        help="The date time to end the scheduling"
    )
    parser.add_argument(
        "--exportToFile",
        help="Whether to export to a file or not",
        action='store_true'
    )
    parser.add_argument(
        "--exportToBrowser",
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

    # Call the Pipeline with all arguments
    args.command(args)
