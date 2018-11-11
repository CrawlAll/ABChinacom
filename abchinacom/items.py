# -*- coding: utf-8 -*-
import scrapy


class AbchinaItem(scrapy.Item):
    name = scrapy.Field()  # 网点名
    province = scrapy.Field()  # 省份
    city = scrapy.Field()  # 地市
    district = scrapy.Field()  # 地区
    address = scrapy.Field()  # 地址
    phone = scrapy.Field()  # 电话
    lng = scrapy.Field()  # 经度
    lat = scrapy.Field()  # 纬度
    url = scrapy.Field()  # 数据来源的url
    total_count = scrapy.Field()  # 该省份网点的总数
