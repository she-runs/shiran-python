
def triface(word):
	"""
	Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
	"""	
	for i in range(0, len(word)-5):
		if word[i]==word[i+1]:
			if word[i+2]==word[i+3]:
				if word[i+4]==word[i+5]:
					return True
	return False

print "triface result for the string '%s' : %s" % ("abbccnmmAabbcc", triface("abbccnmmAabbcc"))
print "triface result for the string '%s' : %s" % ("aabbcc", triface("aabbcc"))
print "triface result for the string '%s' : %s" % ("abccddee0123", triface("abccddee0123"))
print "triface result for the string '%s' : %s" % ("llkkbmm", triface("llkkbmm"))
print "triface result for the string '%s' : %s" % ("aaaazz", triface("aaaazz"))
print "triface result for the string '%s' : %s" % ("bbcCdd", triface("bbcCdd"))
print "triface result for the string '%s' : %s" % ("", triface(""))
print "triface result for the string '%s' : %s" % ("vcbfbngmgnddbbnn", triface("vcbfbngmgnddbbnn"))

