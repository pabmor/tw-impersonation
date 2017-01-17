import pdb
import sys
import twitter
from datetime import datetime
from time import sleep


def main():
	print("Welcome to twitter impersonation.")
	
	api = twitter.Api(consumer_key='jv7jaJRwMSdZokEdgvvJ6vY3k',
	                      consumer_secret='8hl2xeQ2IuYJnBQrF4pgoZdH1I4arPxip1jJoEcBVPebMgPyc7',
	                      access_token_key='817160799819010048-PPnDnUu2uZqmuXMgIgfMGZ4oZr3SXqm',
	                      access_token_secret='Uv4uWr5lqCnaA7zjzcIzkIU87KZz31lJJ8cyYUn315e8E')

	pdb.set_trace()
	users_to_impersonate = {"TheEllenShow" : [], "LEIitalia" : []}
	start_time = datetime.now()
	impersonated_statuses = []
	refresh_rate = 10 #minutes

	while True:
		sleep(refresh_rate * 60)
		for user, impersonated_statuses in users_to_impersonate:
			since_status = None
			if len(impersonated_statuses) != 0:
				since_status = impersonated_statuses[-1]
			user_timeline = api.GetUserTimeline(screen_name=user, since_id=since_status)
			for status in user_timeline:
				if is_new(status=status) and not was_impersonated(status=status):
					impersonate(status=status)		
	


def str_to_datetime(dt_str):
	return datetime.strptime(dt_str, '%a %b %d %H:%M:%S %z %Y')

def is_new(status):
	return str_to_datetime(status.created_at) > start_time
	
def was_impersonated(status):
	return status.id in impersonated_statuses
	
def impersonate(status):
	try:
		result = api.PostUpdates(status)
		impersonated_statuses.append(status.id);
		print("Status Impersonated :", status)
		print()
	except twitter.error.TwitterError as te:
		print("Exception: ", te.args)
		

if(__name__ == "__main__"):
	sys.exit(main())
	