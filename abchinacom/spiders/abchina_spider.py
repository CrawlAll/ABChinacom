# -*- coding: utf-8 -*-
import json
import scrapy
from abchinacom.items import AbchinaItem


class AbchinaSpider(scrapy.Spider):
    name = 'abchina_spider'
    allowed_domains = ['abchina.com']
    base_url = 'http://app.abchina.com/branch/common/BranchService.svc/Branch?p=320000&c=-1&b=-1&q=&t=1&z=0&i={}'

    def start_requests(self):
        url = 'http://app.abchina.com/branch/common/BranchService.svc/District'
        yield scrapy.Request(url=url, callback=self.province_parse)

    def province_parse(self, response):
        text = json.loads(response.text)
        page_num = 0

        for index, value in enumerate(text):
            province_id = value.get('Id')
            province_name = value.get('Name')
            self.logger.info('begin 第{}个 {}-{} 省份 spider......'.format(index + 1, province_id, province_name))

            yield scrapy.Request(url=self.base_url.format(province_id, page_num),
                                 meta={'page_num': page_num, 'province_id': province_id},
                                 callback=self.detail_parse)

    def detail_parse(self, response):
        item = AbchinaItem()
        detail = json.loads(response.text)
        page_num = response.meta['page_num']
        province_id = response.meta['province_id']

        # 获取该省份网点的总数
        total_count = detail.get('TotalCount')
        if page_num * 20 <= total_count:
            page_num += 1
            yield scrapy.Request(url=self.base_url.format(page_num),
                                 meta={'page_num': page_num, 'province_id': province_id},
                                 callback=self.detail_parse)
            bank_list = detail.get('BranchSearchRests')
            if bank_list:
                for info in bank_list:
                    name = info['BranchBank'].get('Name')
                    province = info['BranchBank'].get('Province')
                    city = info['BranchBank'].get('City')
                    district = info['BranchBank'].get('Borough')
                    address = info['BranchBank'].get('Address')
                    phone = [str(info['BranchBank'].get('PhoneNumber'))]
                    lng = str(info['BranchBank'].get('Longitude'))
                    lat = str(info['BranchBank'].get('Latitude'))
                    url = response.url

                    for field in item.fields:
                        item[field] = eval(field)
                    yield item
