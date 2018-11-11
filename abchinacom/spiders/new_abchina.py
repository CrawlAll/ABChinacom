# -*- coding: utf-8 -*-
import json
import scrapy
from abchinacom.items import AbchinaItem


class NewAbchinaSpider(scrapy.Spider):
    name = 'new_abchina'
    allowed_domains = ['abchina.com']

    def start_requests(self):
        base_url = 'http://app.abchina.com/branch/common/BranchService.svc/Branch?p=-1&c=-1&b=-1&q=&t=1&z=0&i={}'
        for i in range(1135):
            yield scrapy.Request(url=base_url.format(i), callback=self.detail_parse)

    def detail_parse(self, response):
        item = AbchinaItem()
        detail = json.loads(response.text)

        total_count = detail.get('TotalCount')

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
        else:
            self.logger.error('该页面为空 check一下 {}'.format(response.url))
