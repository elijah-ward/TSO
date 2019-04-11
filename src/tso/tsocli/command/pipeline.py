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
    """
    The CLI pipeline defines the main processing orchestrator for TSO.
    The following is a sample execution step:
    1. User executes through the CLI
    2. CLI invokes the CLI Pipeline with the supplied arguments
    3. Pipeline Calls the Data Importer with forwarded args
    4. Data importer output is fed into the Transformer to utilize the TSO context (and not the CFHT context)
    5. TSO context data is fed to the Scheduler for final processing
    6. Final resulting scheduler is fed to the Exporter for final consumer export

    :param args: the args from the cli
    :param config: the configuration file (see {root}/tso_config.json
    :return: None
    """
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
