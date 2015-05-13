#encoding:UTF-8
import urllib2
import sys
from sgmllib import SGMLParser
class getUpdates(SGMLParser):
    def reset(self):
        self.IDlist = []
        self.flag = False
        self.getdata = False
        self.verbatim = 0
        SGMLParser.reset(self)
        
    def start_div(self, attrs):
        if self.flag == True:
            self.verbatim +=1
            return
        for k,v in attrs:
            if k == 'id' and v == 'content':#确定进入了<div class='entry-content'>
                self.flag = True
                return

    def end_div(self):#遇到</div>
        if self.verbatim == 0:
            self.flag = False
        if self.flag == True:#退出子层div了，层数减1
            self.verbatim -=1

    def start_h2(self, attrs):
        if self.flag == False:
            return
        self.getdata = True
        
    def end_h2(self):#遇到</p>
        if self.getdata:
            self.getdata = False

    def handle_data(self, text):#处理文本
        if self.getdata:
            self.IDlist.append(text)
            
    def printID(self):
        for i in self.IDlist:
            print i
    
reload(sys)
sys.setdefaultencoding('utf8')
url = "http://www.ishuhui.com/"
data = urllib2.urlopen(url).read()
data = data.encode('utf8','ignore')
output = open('tout.html','w')
output.write(data)
lister = getUpdates()
lister.feed(data)
lister.printID()