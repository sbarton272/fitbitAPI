import json

DATES = ["2014-01-22", "2014-01-23", "2014-01-24", "2014-01-25", "2014-01-26", "2014-01-27", 
         "2014-01-28", "2014-01-29", "2014-01-30", "2014-01-31", "2014-02-01", "2014-02-02", 
         "2014-02-03", "2014-02-04", "2014-02-05", "2014-02-06", "2014-02-07", "2014-02-08", 
         "2014-02-09"]

headings = ["year", "month", "day", "wkday", "wknum", "totalSleep"]

outFilename = "website/totalSleepData.tsv"
sep = '\t'
outFile = open(outFilename, 'w')
outFile.write( sep.join(headings) + '\n' )

wkday = 2 # data starts on a wed

for d in DATES:
	filename = "data/cleaned/sleep-" + d + ".json"

	jsonData = open(filename)

	sleepData = json.load(jsonData)

	ln = sep.join(d.split('-')) + sep + str(wkday % 7 ) + sep + str(wkday / 7 ) + sep+ str(sleepData["summary"]["totalTimeInBed"]) + '\n'

	outFile.write(ln)

	jsonData.close()

	wkday += 1

outFile.close()