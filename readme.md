# Sneazr

Sneazr is a super simple plugin for Nose that adds Growl notifications.  

## Installation

First you need Growl installed and you will need to install their python library.  For instructions on installing Growl's python library, see their [documentation](http://growl.info/documentation/developer/python-support.php "Growl Python Library Info").

After that it should be as easy as

	easy_install sneazr
	
After installation you can do..

	nosetests --with-sneazr
	
..and a summary of its results will be spit out through Growl.  Happy Days!

For instructions on using it with [watchr](http://github.com/mynyml/watchr "Watchr on GitHub") to get continuous testing behaviour check out [this post](http://jessejoelmiller.com/2010/07/continuous-testing-with-nose-and-watchr/ "Continuous testing with Nose and Watchr")

