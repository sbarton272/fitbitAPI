from temboo.Library.Fitbit.Sleep import GetSleep
from temboo.core.session import TembooSession
import json, datetime

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

# Get an InputSet object for the choreo
getSleepInputs = getSleepChoreo.new_input_set()

# Set inputs
getSleepInputs.set_Date("2014-02-06")
getSleepInputs.set_AccessToken(ACCESS_TOKEN)
getSleepInputs.set_AccessTokenSecret(ACCESS_TOKEN_SECRET)
getSleepInputs.set_ConsumerSecret(CONSUMER_SECRET)
getSleepInputs.set_ConsumerKey(CONSUMER_KEY)

# Execute choreo
getSleepResults = getSleepChoreo.execute_with_results(getSleepInputs)

print type(getSleepResults.get_Response())

dataFileName = "data/sleep-" + datetime.date.today().strftime("%Y-%m-%d") + ".json"
f = open(dataFileName, 'w')
json.dump(getSleepResults.get_Response(), f)