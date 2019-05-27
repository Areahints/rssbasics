# author: Kc Nwaezuoke
# MIT License

# --------------------------
#  PunchNG.com
# --------------------------

## News title, link scraping

from engine import log
from engine import punch
from engine import engine

if __name__ == '__main__':
    # Define log file location
    log.set_custom_log_info('logs/error.log')

    # SSL or HTTPS ISSUE
    engine.verify_https_issue()

    # create scraping object
    punch_scrap = punch.Punch(punch.url_punch, log)

    # checking if we should redownload from url or not
    if engine.check_cache(punch.raw_html, punch.CACHE):
        punch_scrap.retrieve_webpage()
        punch_scrap.write_webpage_as_html()

    punch_scrap.read_webpage_from_html()
    punch_scrap.convert_data_to_bs4()
    #punch_scrap.print_beautiful_soup()
    punch_scrap.parse_soup_to_simple_html()
