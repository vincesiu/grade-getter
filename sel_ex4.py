fp = open('logininfo.txt', 'r')
info = []
info.append((fp.readline()).strip())
info.append((fp.readline()).strip())
for line in info:
	print 1
	print line
fp.close()