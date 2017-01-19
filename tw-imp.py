import sys
from impersonator import Impersonator

def main():
	print("Welcome to twitter impersonation.")
	users = {"TheEllenShow" : [], "LEIitalia" : []}
	impersonator = Impersonator(users)
	refresh_rate = 1 #minutes
	impersonator.start(refresh_rate)

if(__name__ == "__main__"):
	sys.exit(main())
	