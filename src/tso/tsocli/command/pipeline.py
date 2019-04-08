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

    cfht_imported_data = data_importer.get_observations_with_args(
        db_config=config.get_database_config(),
        **vars(args)
    )

    tso_observation_requests = transformer.transform_cfht_observing_blocks(cfht_imported_data)
    mock_requests = gr.generate_mock_requests(5)

    schedule = scheduler.generate_schedule(
        config.get_telescope_config(),
        config.get_global_constraint_config(),
        args.start_date_time,
        args.end_date_time,
        args.no_weather_constraints,
        tso_observation_requests if True else mock_requests  # Set to False to use the mock_requests
    )

    exporter.export_to_console(schedule)
    if args.export_to_file:
        exporter.export_to_file(schedule)

    if args.export_to_browser:
        exporter.export_to_browser(schedule)
