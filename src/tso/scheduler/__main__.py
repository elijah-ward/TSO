from tso.scheduler import scheduler

config = {
    'slew_rate': 0.8,
    'filters': {
        'filter': {('MSE', 'EXAMPLE'): 10 }
    }
}

def main():
    print('Inside the main Scheduler Application')

    start_datetime = '2019-03-01 19:00'
    end_datetime = '2019-03-13 19:00'
    scheduler.generate_schedule(config, start_datetime, end_datetime)



if __name__ == '__main__':
    main()
