import os
import xerox
import mechanize

br=mechanize.Browser()
br.set_handle_robots(False)
br.open('http://pastebin.ubuntu.com')
br.select_form(nr=0)
path=raw_input("enter file path - ")
s=open(path,"r").read()
br.form["poster"]=os.popen("whoami").read()
br.form["content"]=s
br.submit()

l=[x for x in br.links()]
link="http://pastebin.ubuntu.com"+l[0].url[:len(l[0].url)-6]
print "link is " + link
xerox.copy(link)
print "It's copied to the clipboard !"
