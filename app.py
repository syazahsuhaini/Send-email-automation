import argparse

from email_text import *
from email_send import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Send E-mail automation',
        description='Auto send an email.',
        epilog='by Syaza')
    
    parser.add_argument('--write',   # -- indicate as flag
                        action='store_true',    # if flag is in the argument, return TRUE for args.write
                        help='Send email.')
    
    parser.add_argument('month_year',   # -- indicate as flag
                        nargs='*',    # need 2 arguments
                        default=None,
                        help='Month and year of the timesheets.')
    
    args = parser.parse_args()

    if args.write:
        if args.month_year is None or len(args.month_year) != 2:
            print("Error: you must provide month and year for renaming, e.g., 'January 2025'")
        else:
            month, year = args.month_year
            text_content = text_template(month, year)
            send_process(month, year, text_content)
    
    if not args.write:
        print("No flags provided. Nothing will run.")