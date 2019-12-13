# WFMU Scraper
A webpage scraper that uses the python module scrapy. Originally designed to scrape the WFMU playlist archive where tracklists of radio shows are kept. This cycles through individual urls for the mixes and consolidates the scraped data into csv files.

Playlists on the WFMU site are organized by individual urls containing the tracklist for a single mixes. For example: http://wfmu.org/playlists/shows/29715 contains a playlist from a single mix in 2008. 

## Instructions

### 1. Download the file.
### 2. To avoid creating a very large output csv file, edit the playlist spider in wfmu/spiders/playlist.py to target specific mixes. Options:

Default value, targets mixes 1-80000 (advised to change!):
start_urls = ['http://wfmu.org/playlists/shows/{}'.format(i) for i in range(80000)]

to (single page):
start_urls = ['http://wfmu.org/playlists/shows/29715']

or smaller range (2000-3000):
start_urls = ['http://wfmu.org/playlists/shows/{}'.format(i) for i in range(2000, 3000)]


### 3. In command prompt go to the wfmu file folder and run the following command:

`scrapy crawl playlist -o output.csv`

This tells the scraper to use the 'playlist' spider and save the results in 'output.csv'.


## WFMU is a listener support radio station that relies on donations supporting its awesome programming. Please consider donating at [WFMU.org](http://wfmu.org)!
