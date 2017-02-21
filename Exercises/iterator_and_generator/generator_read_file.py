# Note: At no point in our generator solution did we ever create large
# temporary lists
# it was based on the concept of pipelining data between different components
wwwlog = open("big-access-log")
bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog)
bytes = (int(x) for x in bytecolumn if x != '-')
print "Total", sum(bytes)
