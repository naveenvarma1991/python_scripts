#!usr/bin/python3

import webbrowser

url = 'http://bitbucket.com'

# Open URL in new browser window
webbrowser.open_new(url) # opens in default browser

# Opens in safari browser
webbrowser.get('safari').open_new(url)

# Open URL in a new tab
webbrowser.open_new_tab(url) # opens in default browser

# Opens in safari browser
webbrowser.get('safari').open_new_tab(url)
