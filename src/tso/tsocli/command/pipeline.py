"""
Pipeline

The main process of using all the different entities in the TSO system.
"""

from tso.importer import data_importer
from tso.importer import transformer
from tso.scheduler import scheduler
from tso.exporter import exporter


def cli_pipeline(args):
    print("Inside Main CLI Pipeline")
    print(args)

    cfht_imported_data = data_importer.get_observations()

    tso_observation_requests = transformer.transform_cfht_observing_blocks(cfht_imported_data)

    schedule = scheduler.generate_schedule()
    # TODO: Need to boostrap in the Config.json stuff here for eli
    sampleConfigJsonForScheduler = {
        'slew_rate': 0.8,
        'filters': {
            'filter': {
                ('MSE', 'Dummy'): 10
            }
        }
    }

    exporter.export_to_console(schedule)
    if args.export_to_file:
        exporter.export_to_file(schedule)
