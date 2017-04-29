import sys
from impersonator import Impersonator
from configuration.values import targets, refresh_rate

def main():
	print("Welcome to twitter impersonation.")
	if len(targets) == 0:
		print("No targets detected, configure your targets first.")
	
	impersonator = Impersonator()
	impersonator.start(targets, refresh_rate)
if(__name__ == "__main__"):
	sys.exit(main())
	