import datetime

class NullFixPipeline(object):
	def process_item(self,item,spider):
		
		try:
			item['experience_required']
		except KeyError:
			item['experience_required']='N/A'
		try:
			item['location']
		except KeyError:
			item['location']='N/A'
		try:
			item['link_job_description']
		except KeyError:
			item['link_job_description']='N/A'
		try:
			item['keyskills']
		except KeyError:
			item['keyskills']='N/A'
		try:
			item['job_description']
		except KeyError:
			item['job_description']='N/A'
		try:
			item['salary']
		except KeyError:
			item['salary']='N/A'
		return item