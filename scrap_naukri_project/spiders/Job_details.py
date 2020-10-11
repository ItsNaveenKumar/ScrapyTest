import scrapy
from scrap_naukri_project.items import MemberItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import MapCompose

class JobDetails(scrapy.Spider):
	name = 'Job_details'
	start_urls = ['https://www.naukri.com/data-analyst-jobs-in-delhi-ncr']
	
	def parse(self,response):
		job_list = response.css('div.row')
		for job in job_list:
			job_loader = ItemLoader(MemberItem(),selector=job)
			job_loader.add_css('job_title','li.desig::text')
			job_loader.add_css('experience_required','span.exp::text')
			job_loader.add_css('location','span.loc > span::text')
			job_loader.add_css('company_name','span.org::text')
			job_loader.add_css('link_job_description','a.content::attr(href)')
			job_loader.add_css('keyskills','span.skill::text')
			job_loader.add_css('job_description','span.desc::text')
			job_loader.add_css('salary','span.salary::text')
			job_loader.add_css('posted_by','a.rec_name::text')
			
			yield job_loader.load_item()
	
	
	
			
		