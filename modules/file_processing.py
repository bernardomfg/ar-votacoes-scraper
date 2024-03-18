# modules/file_processing.py
import re
import mongoengine as mongo
from datetime import datetime
from urllib.request import urlretrieve
from constants import FILENAME_DATE_PATTERN
from model.file import File
from modules.web_scraping import extract_filename_from_url

def extract_date_from_filename(filename):
    """
    Extracts the date from the filename based on the specified pattern.
    
    Args:
        filename (str): The filename from which to extract the date.

    Returns:
        str or None: The extracted date string or None if no match found.
    """
    match = re.search(FILENAME_DATE_PATTERN, filename)
    return match.group() if match else None

def process_file(url, filename, file_path):
    """
    Processes a file by extracting information and saving it to the database.

    Args:
        url (str): The URL of the file.
        filename (str): The filename.
        file_path (str): The local file path.

    Returns:
        None
    """
    voting_date = extract_date_from_filename(filename)
    
    if voting_date is None:
        logging.error(f"No valid voting date found in filename: {filename}")
        return
    
    file_doc = File(
        file_url=url,
        isParsed=False,
        filename=filename,
        localFilePath=file_path,
        created=datetime.now(),
        votingDate=voting_date
    )

    logging.info(f"Processing file:{file_doc.filename}")
    try:
        file_doc.save()
        urlretrieve(file_doc.file_url, file_doc.localFilePath)
        print("Inserted Successfully!", file_doc.filename)
    except mongo.errors.NotUniqueError:
        print("File already exists in the database, skipping.")
