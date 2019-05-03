SS is an object that makes webscraping much easier.  

an example of its use:

create an object with the SexyScraper object 
>>> page = SexyScraper("https://en.wikipedia.org/wiki/Spider-Man")

-the html parser is set to html5lib as default but you can change this
by setting "self.parser" = to you whatever you want 

-use get_html method to retrieve html 
>>> page.get_html()

>>> page.parsed()
-after you parse the html you can use whatever BeautifulSoup method
you want to manipulate the html: prettify(), get_text(), ect. 

>>> page.find("title")
>>> page.find_item.get_text()
'Spider-Man - Wikipedia'

