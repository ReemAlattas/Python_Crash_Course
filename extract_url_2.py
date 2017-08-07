# page = contents of a web page

# page = '<a href="http://udacity.com">Hello world</a>'

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

# Solution 2
sub_str = '<a href='
start_link = page.find('<a href=')
start_q = page.find('"', start_link)
end_q = page.find('"',start_q+1)
url = page[start_q+1:end_q]
print url