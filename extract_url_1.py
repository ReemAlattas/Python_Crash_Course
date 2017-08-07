# page = contents of a web page

# page = '<a href="http://udacity.com">Hello world</a>'

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

Solution 1
sub_str = '<a href='
start_link = page.find(sub_str)

start = page.find(sub_str)
stop = page[start:].find('>') + start

# print start
# print stop

url = page[start+9:stop-1]

# print url