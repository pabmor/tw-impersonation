import pdb
import twitter
from time import sleep
from datetime import datetime, timezone, timedelta

class Impersonator:

	def __init__(self, users):
		self.start_time = datetime.now(timezone.utc) - timedelta(days=3)
		#TODO pass keys as parameter
		self.api = twitter.Api(consumer_key='jv7jaJRwMSdZokEdgvvJ6vY3k',
	                      consumer_secret='8hl2xeQ2IuYJnBQrF4pgoZdH1I4arPxip1jJoEcBVPebMgPyc7',
	                      access_token_key='817160799819010048-PPnDnUu2uZqmuXMgIgfMGZ4oZr3SXqm',
	                      access_token_secret='Uv4uWr5lqCnaA7zjzcIzkIU87KZz31lJJ8cyYUn315e8E')
		self.users = users
	
	def str_to_datetime(self, dt_str):
		return datetime.strptime(dt_str, '%a %b %d %H:%M:%S %z %Y')

	def is_new(self, status):
		print(self.str_to_datetime(status.created_at))
		print('>', self.start_time)
		return self.str_to_datetime(status.created_at) > self.start_time
		
	def was_impersonated(self, status, imp_statuses):
		return status.id in imp_statuses
		
	def impersonate(self, status, imp_statuses):
		try:
			content = status.text.encode('utf-8')
			content = content.decode('latin-1')
			print("val to post", content)
			result = self.api.PostUpdates(content)
			imp_statuses.append(status.id);
			print("Status Impersonated :", status)
			print()
		except twitter.error.TwitterError as te:
			print("Exception: ", te.args)
		except UnicodeEncodeError as ee:
			print("Exception: ", ee.args)


	def start(self, refresh_rate=1):
		pdb.set_trace()
		while True:
			sleep(refresh_rate * 1)
			for user, impersonated_statuses in self.users.items():
				since_status = None
				if len(impersonated_statuses) != 0:
					since_status = impersonated_statuses[-1]
				user_timeline = self.api.GetUserTimeline(screen_name=user, since_id=since_status)
				for status in user_timeline:
					if self.is_new(status=status) and not self.was_impersonated(status=status, imp_statuses=impersonated_statuses):
						self.impersonate(status=status, imp_statuses=impersonated_statuses)		
		
			

