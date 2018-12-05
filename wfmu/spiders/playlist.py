# -*- coding: utf-8 -*-
import scrapy
from pprint import pprint


class PlaylistSpider(scrapy.Spider):
    """ This function parses a sample response. Some contracts are mingled with this docstring.

    @scrapes Artist Album Track
    """
    name = 'playlist'
    allowed_domains = ['wfmu.org']
    start_urls = ['http://wfmu.org/playlists/shows/{}'.format(i) for i in range(70001, 77500)]
    # start_urls = ['http://wfmu.org/playlists/shows/29715']

    def parse(self, response):
        title = response.xpath('//h2/text()').extract()
        title = ' '.join(title).strip()
        title = title.split(':')

        try:
            profile = title[0]
        except IndexError:
            profile = ''
        try: 
            playlist_date = title[1].strip().replace('Playlist\nfrom ','')
        except IndexError:
            playlist_date = ''


        rows = response.xpath('//tr')
        for row in rows:
            data = row.xpath('.//td[@class="song"]/font/text()').extract()
            data = [i.strip() for i in data]

            try:
                label = data[3]
            except IndexError:
                label = ''
            try:
                artist = data[0]
                if artist == '':
                    raise IndexError
            except IndexError:
                continue
            try:
                track = data[1]
                if track == '':
                    raise IndexError
            except IndexError:
                continue
            try:
                album = data[2]
                if album == '':
                    raise IndexError
            except IndexError:
                continue

            try:
                item = {
                    'Url': response.url,
                    'Profile': profile,
                    'Playlist Date': playlist_date,
                    'Artist': artist,
                    'Track': track,
                    'Album': album,
                    'Label': label,
                    }
                yield item
            except IndexError:
                pass
