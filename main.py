# main.py
import os
import dotenv
import logging
import mongoengine as mongo
from modules.database import connect_to_database
from modules.web_scraping import scrape_webpage, extract_filename_from_url
from modules.file_processing import process_file
from constants import AR_ARCHIVE_BASE_URL

def main():
    #load environment variables
    dotenv.load_dotenv()
    # Filesystem constants
    filesystem_root_path = os.getenv("FILESYSTEM_ROOT_PATH")
    # Database constants
    dbConnectionString = os.getenv('DB_MONGODB_CONNECTION_STRING')

    # Connect to the database
    connect_to_database(dbConnectionString)

    # Scraping the webpage
    votings = scrape_webpage(AR_ARCHIVE_BASE_URL)

    # Process files
    for voting in votings:
        url = voting['href']
        logging.info(f"Fetching {url}")
        filename = extract_filename_from_url(url)
        file_path = os.path.join(filesystem_root_path, filename)
        process_file(url, filename, file_path)

if __name__ == "__main__":
    main()
