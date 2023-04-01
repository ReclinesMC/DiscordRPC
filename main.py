# Sean A
# Custom Discord RPC Script
# This script will allow me to use custom discord RPC stuffs for my discord acc.
import pypresence as pyp
import os

appID = "1091551079457620068"
presence = pyp.Presence(appID)



def main():
	presence.connect()

	presence.update(state="Test")

if __name__ == "__main__":
	main()