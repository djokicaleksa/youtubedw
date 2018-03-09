import scrapy
import os
import sys


class YouTubeSpider(scrapy.Spider):
    name = "youtube"

    def start_requests(self):
        urls = [
	    "https://www.youtube.com/watch?v=Fek5f1laY5M"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for links in response.css('div.content-wrapper a::attr(href)').extract():
            next_page = "https://www.youtube.com" + links
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
            yield {
                'link':next_page
            }
            os.system("youtube-dl --extract-audio --audio-format mp3 " + next_page)
