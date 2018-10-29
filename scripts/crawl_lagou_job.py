import scrapy
class LagouspiderSpider(scrapy.Spider):
    name = 'lagouspider'
    
    @property
    def start_urls(self):
        url_tmp1 = 'https://www.lagou.com/zhaopin/{}/?filterOption=3'
        return (url_tmp1.format(i) for i in range(2,31))
  

    def parse(self, response):
        for job in response.css('ul.item_con_list li'):
            yield {
                'name': job.css('div.list_item_top div.p_top h3::text').extract_first(),
                'salary_low' : (job.css('div.list_item_top div.p_bot span.money::text').extract_first().split('-'))[0],
                'salary_high' : (job.css('div.list_item_top div.p_bot span.money::text').extract_first().split('-'))[1],
                'experience_requirement' : (job.css('div.list_item_top div.li_b_l::text').extract_first().split(' / '))[0],
                'degree_requirement' : (job.css('div.list_item_top div.li_b_l::text').extract_first().split(' / '))[1],
                'company' : job.css('div.company_name a::text').extract_first(),
                'tags' : job.css('div.list_item_bot div.li_b_l span::text').extract_first()
                 }
 
