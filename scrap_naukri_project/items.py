import scrapy

class MemberItem(scrapy.Item):
	job_title = scrapy.Field()
	experience_required = scrapy.Field()
	location = scrapy.Field()
	company_name = scrapy.Field()
	link_job_description = scrapy.Field()
	keyskills = scrapy.Field()
	job_description = scrapy.Field()
	salary = scrapy.Field()
	posted_by = scrapy.Field()
	