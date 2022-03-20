# -*- coding: utf-8 -*-
"""
Royal Society of Chemistry web-scraper. Please get the permission from RSC before web-scraping.
"""

__author__ = "Shu Huang"
__email__ = "sh2009@cam.ac.uk"

import re
import requests
import urllib.request
from chemdataextractor.scrape.pub.rsc import RscSearchScraper
from selenium import webdriver
import time

def get_doi(query, pagenumber):
    """
    Find the DOIs of a topic in RSC
    :param query: <str> search topic
    :param pagenumber: <int> the page of the search items
    :return: <list> of <str> list of DOIs
    """
    scrape = RscSearchScraper(
        driver=webdriver.Firefox()).run(
        query,
        page=pagenumber)
    results = scrape.serialize()
    dois = [result['doi'] for result in results]
    return dois

def get_url(doi):
    """
    Find the full url address according to the DOI
    :param doi: <str> DOI
    :return: <str> url text
    """
    r = requests.get(
        'http://doi.org/' +
        doi,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'})
    result = re.findall(
        r'https://pubs.rsc.org/en/content/articlehtml/.*?"',
        r.text)
    result = result[0][:-1]
    return result

def download_doi(doi):
    """
    Download the paper according to the DOI
    :param doi: <str> DOI
    """
    url = 'https://doi-org.sheffield.idm.oclc.org/' + str(doi)
    webcontent = urllib.request.urlopen(url).read()
    #f.write(webcontent)
    print(webcontent)
    return
