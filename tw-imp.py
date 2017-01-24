import sys
from impersonator import Impersonator
from serialization import Serializer

def main():
	print("Welcome to twitter impersonation.")
	serializer = Serializer()
	data = serializer.load()
	if data is None:
		users = {"TheEllenShow" : [], "LEIitalia" : []}
	else:
		users = data
	try:
		impersonator = Impersonator(users)
		refresh_rate = 1 #minutes
		impersonator.start(refresh_rate)
	except SystemExit:
		serializer = Serializer()
		serializer.save(impersonator.users)
if(__name__ == "__main__"):
	sys.exit(main())
	