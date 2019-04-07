"""
Pipeline

The main process of using all the different entities in the TSO system.
"""

from tso.importer import data_importer
from tso.importer import transformer
from tso.scheduler import scheduler
from tso.exporter import exporter
from tso.scheduler.utils import generate_mock_requests as gr

tso_epilog = """\n\n
     ______________
    /_  __/ __/ __ \\
     / / _\ \/ /_/ /
    /_/ /___/\____/
    ---------------
    Observe Freely
    ---------------\n\n"""


def cli_pipeline(args, config):
    print(tso_epilog)
    print(args)

    cfht_imported_data = data_importer.get_observations(config.get_database_config())

    tso_observation_requests = transformer.transform_cfht_observing_blocks(cfht_imported_data)

    schedule = scheduler.generate_schedule(config.get_telescope_config(), args.startDateTime, args.endDateTime, gr.generate_mock_requests(5))

    exporter.export_to_console(schedule)
    if args.exportToFile:
        exporter.export_to_file(schedule)

    if args.exportToBrowser:
        exporter.export_to_browser(schedule)
