import sys
import argparse

from . import command as tso_command

def initialize_import_parser(subparser):
    import_parser = subparser.add_parser(
        "import",
        aliases=['i'],
        help="Import: import data from the observation database"
    )  # import from SQL DB  -
    import_parser.set_defaults(command=tso_command.import_command)

    return import_parser


def initialize_schedule_parser(subparser):
    schedule_parser = subparser.add_parser(
        "schedule",
        aliases=['s'],
        help="Schedule: schedule observations"
    )  # Add schedule dates. To and From. step pattern for
    schedule_parser.set_defaults(command=tso_command.schedule_command)

    return schedule_parser


def initialize_optimize_parser(subparser):
    optimize_parser = subparser.add_parser(
        "optimize",
        aliases=['o'],
        help="Optimize: optimize schedule(s)"
    )  #TODO: Not needed?
    optimize_parser.set_defaults(command=tso_command.optimize_command)

    return optimize_parser


def initialize_export_parser(subparser):
    export_parser = subparser.add_parser(
        "export",
        aliases=['e'],
        help="Export: export optimized schedule(s)"
    )  # Export will be easy-- to what file, filename, default file name
    export_parser.set_defaults(command=tso_command.export_command)

    return export_parser


def main():

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

    tso_parser.add_argument("-f", help="Some Foo")

    subparsers = tso_parser.add_subparsers()
    import_parser = initialize_import_parser(subparsers)
    schedule_parser = initialize_schedule_parser(subparsers)
    optimize_parser = initialize_optimize_parser(subparsers)
    export_parser = initialize_export_parser(subparsers)

    # Display the hep if no arguments are passed
    if len(sys.argv) == 1:
        tso_parser.print_help(sys.stderr)
        sys.exit(1)

    args = tso_parser.parse_args()
    args.command(args)


if __name__ == '__main__':
    main()
