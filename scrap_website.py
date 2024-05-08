import os
from bs4 import BeautifulSoup
import requests
import re
import datetime



def generate_web_pages(latest_year):
    """
    Generates a dictionary of web page URLs for CVF conferences from 2013 to the latest year.
    
    Args:
        latest_year (int): The latest year for which web pages need to be generated.
        
    Returns:
        dict: A dictionary containing web page URLs for each year.
    """
    
    web_page_directory = {}
    for year in range(latest_year, (datetime.datetime.now().year) +1 ):
        web_page_directory[year] = []
        for conference in ('WACV', 'ICCV', 'CVPR'):
            generated_url = f'https://openaccess.thecvf.com/{conference}{year}'
            web_page_directory[year].append(generated_url)
    return web_page_directory


""" 

Contact developer for the rest of the source code

"""