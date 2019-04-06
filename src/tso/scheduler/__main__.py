from tso.scheduler import scheduler
from tso.scheduler.utils import generate_requests as gr
from tso.exporter import exporter

config = {
    'slew_rate': 0.8,
    'filters': {
        'filter': {('MSE', 'EXAMPLE'): 10 }
    }
}

N_BLOCKS = 5

def main():
    print('Inside the main Scheduler Application')

    requests = gr.generate_requests(N_BLOCKS)
    start_datetime = '2019-03-01 19:00'
    end_datetime = '2019-03-13 19:00'
    schedule = scheduler.generate_schedule(config, start_datetime, end_datetime, requests)
    print(schedule)
    exporter.export_to_console(schedule)

if __name__ == '__main__':
    main()
