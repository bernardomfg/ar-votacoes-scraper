# main.py
import datetime
import os
import dotenv
import logging
import sys
import mongoengine as mongo
from modules.database import connect_to_database
from modules.web_scraping import scrape_webpage, extract_filename_from_url
from modules.file_processing import process_file
from constants import AR_ARCHIVE_BASE_URL, AR_ARCHIVE_BASE_URL_YEAR_LOWER_BOUND, AR_ARCHIVE_BASE_URL_YEAR_SUFFIX

def main():

    #configure logging to stdout
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    #load environment variables
    dotenv.load_dotenv()
    # Filesystem constants
    filesystem_root_path = os.getenv("FILESYSTEM_ROOT_PATH")
    # Database constants
    dbConnectionString = os.getenv('DB_MONGODB_CONNECTION_STRING')

    # Connect to the database
    connect_to_database(dbConnectionString)

    # get the years to be scraped
    currentYear = datetime.now().year
    lowerBoundYear = AR_ARCHIVE_BASE_URL_YEAR_LOWER_BOUND
    years = range(lowerBoundYear, currentYear + 1)

    # get the url and suffix
    baseUrl = AR_ARCHIVE_BASE_URL
    urlSuffix = AR_ARCHIVE_BASE_URL_YEAR_SUFFIX


    #iterate over the years to get the votings
    for year in years:
         # Scraping the webpage
        scrapeUrl = baseUrl + urlSuffix + str(year)
        votings = scrape_webpage(scrapeUrl)

        # Process files
        for voting in votings:
            fileUrl = voting['href']
            logging.info(f"Fetching {fileUrl}")
            filename = extract_filename_from_url(fileUrl)
            file_path = os.path.join(filesystem_root_path, filename)
            process_file(fileUrl, filename, file_path)
   

if __name__ == "__main__":
    main()
