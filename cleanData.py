
DATES = ["2014-01-22", "2014-01-23", "2014-01-24", "2014-01-25", "2014-01-26", "2014-01-27", 
         "2014-01-28", "2014-01-29", "2014-01-30", "2014-01-31", "2014-02-01", "2014-02-02", 
         "2014-02-03", "2014-02-04", "2014-02-05", "2014-02-06", "2014-02-07", "2014-02-08", 
         "2014-02-09"]

for d in DATES:
	filename = "data/sleep-" + d + ".json"
	newFilename = "data/cleaned/sleep-" + d + ".json"
	
	f = open(filename, 'r')
	n = open(newFilename, 'w')
	t = f.read()
	t = t[1:]
	t = t[:-1]
	t = t.replace('\\','')
	print t
	n.write(t)
	n.close()
	f.close()