import synchronization.scheduler as scheduler
import synchronization.synchronization as synchronization
import settings
import logging
import argparse
import os

def arg_parse ():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('-l', '--log', help='log filepath')
    arg_parser.add_argument('-s', '--source', help='source path')
    arg_parser.add_argument('-r', '--replica', help='replica path')
    arg_parser.add_argument('-i', '--interval', help='sync interval')

    return arg_parser.parse_args()

def get_init_parameters():
    args = arg_parse()
    params = {}

    if args.interval:
        params['sync_interval'] = int(args.interval)
    else:
        params['sync_interval'] = settings.sync_interval
    
    if args.log:
        if os.path.isdir(args.log):
            params['log_filepath'] = os.path.normpath(os.path.join(args.log, settings.log_filename)) 
        else:
            params['log_filepath'] = os.path.normpath(args.log)
    else:
        params['log_filepath'] = os.path.normpath(os.path.join(settings.log_filepath, settings.log_filename))

    if args.source:
        params['source'] = args.source
    else:
        params['source'] = settings.source_folder_path

    if args.replica:
        params['replica'] = args.replica
    else:
        params['replica'] = settings.replica_folder_path

    return params  

def set_logging_config(filepath):
    logging.basicConfig(filename=filepath, 
                        level=logging.INFO, filemode='w', 
                        format='%(asctime)s - %(levelname)s - %(message)s', 
                        datefmt='%d-%b-%y %H:%M:%S')

def main():
    params = get_init_parameters()
    set_logging_config(params['log_filepath'])

    logging.info('app starting...')

    synchronization.run_sync(params)
    # scheduler.run_scheduler(params, synchronization.run_sync)

if __name__ == '__main__':
    main()