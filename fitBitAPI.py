from temboo.Library.Fitbit.Sleep import GetSleep
from temboo.core.session import TembooSession
import json, datetime

DATES = ["2014-01-22"]
# DATES = ["2014-01-22", "2014-01-23", "2014-01-24", "2014-01-25", "2014-01-26", "2014-01-27", 
#          "2014-01-28", "2014-01-29", "2014-01-30", "2014-01-31", "2014-02-01", "2014-02-02", 
#          "2014-02-03", "2014-02-04", "2014-02-05", "2014-02-06", "2014-02-07", "2014-02-08", 
#          "2014-02-09"]

settings = {}
execfile("settings.conf", settings)
APP_KEY_NAME = settings["APP_KEY_NAME"]
APP_KEY = settings["APP_KEY"]
ACCESS_TOKEN = settings["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = settings["ACCESS_TOKEN_SECRET"]
CONSUMER_SECRET = settings["CONSUMER_SECRET"]
CONSUMER_KEY = settings["CONSUMER_KEY"]

session = TembooSession('sbarton272', APP_KEY_NAME, APP_KEY)
getSleepChoreo = GetSleep(session)

for d in DATES:
	# Get an InputSet object for the choreo
	getSleepInputs = getSleepChoreo.new_input_set()

	# Set inputs
	getSleepInputs.set_Date(d)
	getSleepInputs.set_AccessToken(ACCESS_TOKEN)
	getSleepInputs.set_AccessTokenSecret(ACCESS_TOKEN_SECRET)
	getSleepInputs.set_ConsumerSecret(CONSUMER_SECRET)
	getSleepInputs.set_ConsumerKey(CONSUMER_KEY)

	# Execute choreo
	getSleepResults = getSleepChoreo.execute_with_results(getSleepInputs)

	dataFileName = "data/sleep-" + d + ".json"
	f = open(dataFileName, 'w')
	json.dump(getSleepResults.get_Response(), f)