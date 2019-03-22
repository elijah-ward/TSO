"""
Pipeline

The main process of using all the different entities in the TSO system.
"""

from tso.importer import data_importer
from tso.importer import transformer
from tso.scheduler import scheduler
from tso.exporter import exporter

# TODO: Need to move this to an external config.json with global configs for the tool
sampleConfigJsonForScheduler = {
    'slew_rate': 0.8,
    'filters': {
        'filter': {('MSE', 'EXAMPLE'): 10 }
    }
}


def cli_pipeline(args):
    print("Inside Main CLI Pipeline")
    print(args)

    cfht_imported_data = data_importer.get_observations()

    tso_observation_requests = transformer.transform_cfht_observing_blocks(cfht_imported_data)

    schedule = scheduler.generate_schedule(sampleConfigJsonForScheduler, args.startDateTime, args.endDateTime)

    exporter.export_to_console(schedule)
    if args.exportToFile:
        exporter.export_to_file(schedule)

    if args.exportToBrowser:
        exporter.export_to_browser
