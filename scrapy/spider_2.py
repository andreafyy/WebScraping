# -*- coding: utf-8 -*-
# Importing Libraries
import scrapy
import re

# Declaring Movies class
class Movies(scrapy.Item):
    Name = scrapy.Field()
    Link = scrapy.Field()
    Rating = scrapy.Field()
    Genre = scrapy.Field()
    Original_Language = scrapy.Field()
    Director = scrapy.Field()
    Producer = scrapy.Field()
    Writer = scrapy.Field()
    Release_Date_Streaming = scrapy.Field()
    Runtime = scrapy.Field()
    Production_Co = scrapy.Field()
    Aspect_Ratio = scrapy.Field()
    Sound_Mix = scrapy.Field()
    Release_Date_Theaters = scrapy.Field()
    Box_Office = scrapy.Field()

# Declaring Spider
class LinksSpider(scrapy.Spider):
    # Spider Name
    name = 'movies'
    allowed_domains = ['https://www.rottentomatoes.com/top/bestofrt/']
    try:
        # Opening links file to go through each individual movie information
        with open("links.csv", "rt", encoding='utf-8') as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    # Scrapy Parse
    def parse(self, response):
        # Declaring class object
        m = Movies()

        # Name of movie
        name = response.xpath('//h1[@data-qa = "score-panel-movie-title"]/text()').getall()
        m['Name'] = name

        # Links of the movie
        m['Link'] = response.request.url

        # Rating of the movie
        rating = response.xpath(
            '//li[@data-qa="movie-info-item"]/div[@data-qa="movie-info-item-label" and text() = "Rating:"]/following-sibling::div/text()').getall()
        if rating:
            m['Rating'] = (re.sub("\s\s+", " ", rating[0])).strip()
        else:
            m['Rating'] = ""

        # Genre of the movie
        genre = response.xpath(
            '//li[@data-qa="movie-info-item"]/div[@data-qa="movie-info-item-label" and text() = "Genre:"]/following-sibling::div/text()').getall()
        if genre:
            m['Genre'] = (re.sub("\s\s+", " ", genre[0])).strip()
        else:
            m['Genre'] = ""

        # Original Language of the movie
        original_language = response.xpath(
            '//li[@data-qa="movie-info-item"]/div[@data-qa="movie-info-item-label" and text() = "Original Language:"]/following-sibling::div/text()').getall()
        if original_language:
            m['Original_Language'] = (re.sub("\s\s+", " ", original_language[0])).strip()
        else:
            m['Original_Language'] = ""

        # Director of the movie
        director = response.xpath(
            '//li[@data-qa="movie-info-item"]/div[@data-qa="movie-info-item-label" and text() = "Director:"]/following-sibling::div/a/text()').getall()
        if director:
            m['Director'] = (re.sub("\s\s+", " ", director[0])).strip()
        else:
            m['Director'] = ""

        # Producer of the movie
        producer = response.xpath(
            '//li[@data-qa="movie-info-item"]/div[@data-qa="movie-info-item-label" and text() = "Producer:"]/following-sibling::div/a/text()').getall()
        if producer:
            m['Producer'] = (re.sub("\s\s+", " ", producer[0])).strip()
        else:
            m['Producer'] = ""

        # Writer of the movie
        writer = response.xpath(
            '//li[@data-qa="movie-info-item"]/div[@data-qa="movie-info-item-label" and text() = "Writer:"]/following-sibling::div/a/text()').getall()
        if writer:
            m['Writer'] = (re.sub("\s\s+", " ", writer[0])).strip()
        else:
            m['Writer'] = ""


        # Release Date of the movie on streaming sites
        release_date = response.xpath(
            '//li[@data-qa="movie-info-item"]/div[@data-qa="movie-info-item-label" and text() = "Release Date (Streaming):"]/following-sibling::div/time/text()').getall()
        if release_date:
            m['Release_Date_Streaming'] = (re.sub("\s\s+", " ", release_date[0])).strip()
        else:
            m['Release_Date_Streaming'] = ""

        # Run time of the movie
        runtime = response.xpath(
            '//li[@data-qa="movie-info-item"]/div[@data-qa="movie-info-item-label" and text() = "Runtime:"]/following-sibling::div/time/text()').getall()
        if runtime:
            m['Runtime'] = (re.sub("\s\s+", " ", runtime[0])).strip()
        else:
            m['Runtime'] = ""

        # Production CO of the movie
        production_co = response.xpath(
            '//li[@data-qa="movie-info-item"]/div[@data-qa="movie-info-item-label" and text() = "Production Co:"]/following-sibling::div/text()').getall()
        if production_co:
            m['Production_Co'] = (re.sub("\s\s+", " ", production_co[0])).strip()
        else:
            m['Production_Co'] = ""

        # Aspect Ratio of the movie
        aspect_ratio = response.xpath(
            '//li[@data-qa="movie-info-item"]/div[@data-qa="movie-info-item-label" and text() = "Aspect Ratio:"]/following-sibling::div/text()').getall()
        if aspect_ratio:
            m['Aspect_Ratio'] = (re.sub("\s\s+", " ", aspect_ratio[0])).strip()
        else:
            m['Aspect_Ratio'] = ""

        # Sound mix of the movie
        sound_mix = response.xpath(
            '//li[@data-qa="movie-info-item"]/div[@data-qa="movie-info-item-label" and text() = "Sound Mix:"]/following-sibling::div/text()').getall()
        if sound_mix:
            m['Sound_Mix'] = (re.sub("\s\s+", " ", sound_mix[0])).strip()
        else:
            m['Sound_Mix'] = ""

        # Box office collection of the movie
        box_office = response.xpath(
            '//li[@data-qa="movie-info-item"]/div[@data-qa="movie-info-item-label" and text() = "Box Office (Gross USA):"]/following-sibling::div/text()').getall()
        if box_office:
            m['Box_Office'] = (re.sub("\s\s+", " ", box_office[0])).strip()
        else:
            m['Box_Office'] = ""

        # Release date in theaters of the movie
        release_date_theaters = response.xpath(
            '//li[@data-qa="movie-info-item"]/div[@data-qa="movie-info-item-label" and text() = "Release Date (Theaters):"]/following-sibling::div/time/text()').getall()
        if release_date_theaters:
            m['Release_Date_Theaters'] = (re.sub("\s\s+", " ", release_date_theaters[0])).strip()
        else:
            m['Release_Date_Theaters'] = ""

        yield m