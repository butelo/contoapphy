import xml.sax.handler
class ArticleHandler(ContentHandler):
	"""
	A handler to deal with articles in XML
	"""

	def startElement(self, name, attrs):
		print "Start element:", name

