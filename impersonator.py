import twitter
from time import sleep
from datetime import datetime, timezone, timedelta
from data import Db

class Impersonator:

	def __init__(self):
		self.start_time = datetime.now(timezone.utc)
		#TODO pass keys as parameter
		self.api = twitter.Api(consumer_key='jv7jaJRwMSdZokEdgvvJ6vY3k',
	                      consumer_secret='8hl2xeQ2IuYJnBQrF4pgoZdH1I4arPxip1jJoEcBVPebMgPyc7',
	                      access_token_key='817160799819010048-PPnDnUu2uZqmuXMgIgfMGZ4oZr3SXqm',
	                      access_token_secret='Uv4uWr5lqCnaA7zjzcIzkIU87KZz31lJJ8cyYUn315e8E')
		self.db = Db()
		
	def _str_to_datetime(self, dt_str):
		return datetime.strptime(dt_str, '%a %b %d %H:%M:%S %z %Y')

	def _is_new(self, status):
		return self._str_to_datetime(status.created_at) > self.start_time
		
	def _was_impersonated(self, status, imp_statuses):
		status = self.db.get_status(status.id, status.user.id)
		return status is not None
		
	def _impersonate(self, status, imp_statuses):
		try:
			content = status.text
			result = self.api.PostUpdates(content)
			imp_statuses.append(status.id);
			print("Status Impersonated :", status)
			print()
			
		except twitter.error.TwitterError as te:
			print("Exception: ", te.args)
		except UnicodeEncodeError as ee:
			print("Exception:  Unicode not printable")


	def start(self, users, refresh_rate=60):
		self.users = users
		while True:
			print("Sleeping for " + repr(refresh_rate) + " minutes")
			sleep(refresh_rate)
			print("Sleep ended")
			for user in self.users:
				since_status = None
				if len(impersonated_statuses) != 0:
					since_status = impersonated_statuses[-1]
				user_timeline = self.api.GetUserTimeline(screen_name=user, since_id=since_status)
				for status in user_timeline:
					if self._is_new(status=status) and not self._was_impersonated(status=status, imp_statuses=impersonated_statuses):
						self._impersonate(status=status, imp_statuses=impersonated_statuses)		
		
			

