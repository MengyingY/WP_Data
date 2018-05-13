# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import html.parser as hp
import pandas as pd


def addRowstolinkdf(df,lt,lu):
    i=df.iloc[:,0].size
    df.loc[i,'linkTitle']=lt
    df.loc[i,'linkUrl']=lu



class MyHtmlParser(hp.HTMLParser):
 
    def __init__(self,ldf):
        hp.HTMLParser.__init__(self)
        self.linkdf=ldf
    
    def _attr(self,attrlist, attrname):
            for attr in attrlist:
                if attr[0]==attrname:
                    return attr[1]
            return NULL
        
    def handle_starttag(self, tag, attrs):
        if tag=='a':
            lti=self._attr(attrs, 'title')
            lui=self._attr(attrs, 'href')
            addRowstolinkdf(self.linkdf,lti,lui)
            


def extract_link(df,htmlcode):
    #str='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> <html xmlns="http://www.w3.org/1999/xhtml">  <head>   <title></title>   <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />  </head>  <body> <div class="editable"> <h2><img title="photo" src="/mailings/377/tmpl/583/IMG_20130904_221341.jpg" alt="photo" width="450" height="450" border="0" /></h2> <p><strong><span style="color: #333333;">大家好，我是Vincent,是公司AE部门新来的同事，初来乍到，希望大家多多指教！</span></strong></p> <p><span style="color: #333333;">我平时的爱好是：摄影，旅游，游戏，篮球，和游泳，希望和有共同爱好的小伙伴们交流和切磋！另外，我曾留法7年，所以有法语感兴趣的朋友可以跟我说哈！</span></p> <h3><span style="color: #808080;">联系方式有：</span></h3> <p><span style="color: #808080;">微博：<a style="text-decoration: underline;" title="DMDlink 1" href="http://weibo.com/lfscn" target="_blank"><span style="text-decoration: underline;"><span style="color: #808080; text-decoration: underline;">cocacoldnotcola</span></span></a></span></p> <p><span style="color: #808080;">微信：cocacold</span></p> <p><strong><span style="color: #333333;">Hello everyone, I'm Vincent, I just arrive at WP AE department, hope have a great time with you guys!</span></strong></p> <p><span style="color: #333333;">My hobbies are photography, travel, video games, basketball and swimming, I'm glad to communicate this subjects with you guys. By the way, I've studied in France for 7 years, so I'm a french speaker, if you interested in french or France, please feel free to discuss that with me. </span></p> <h3><span style="color: #333333;">Contact:</span></h3> <p><span style="color: #333333;">By weibo:<a style="text-decoration: underline;" title="DMDlink 2" href="http://weibo.com/lfscn" target="_blank"><span style="text-decoration: underline;"><span style="color: #333333; text-decoration: underline;">cocacoldnotcola</span></span></a></span></p> <p><span style="color: #333333;">By wechat:cocacold</span></p> <p><a style="text-decoration: underline;" title="DMDlink 3" href="{$WEBLINK}" target="email">{$create_date}</a></p> </div> </body> </html>'''
    myparser=MyHtmlParser(df)
    myparser.feed(htmlcode)
    myparser.close()
    return myparser.linkdf

if __name__=='__main__':
    linkdf=pd.DataFrame(
               columns={'linkTitle','linkUrl'}
                )
    extract_link(linkdf,'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> <html xmlns="http://www.w3.org/1999/xhtml">  <head>   <title></title>   <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />  </head>  <body> <div class="editable"> <h2><img title="photo" src="/mailings/377/tmpl/583/IMG_20130904_221341.jpg" alt="photo" width="450" height="450" border="0" /></h2> <p><strong><span style="color: #333333;">大家好，我是Vincent,是公司AE部门新来的同事，初来乍到，希望大家多多指教！</span></strong></p> <p><span style="color: #333333;">我平时的爱好是：摄影，旅游，游戏，篮球，和游泳，希望和有共同爱好的小伙伴们交流和切磋！另外，我曾留法7年，所以有法语感兴趣的朋友可以跟我说哈！</span></p> <h3><span style="color: #808080;">联系方式有：</span></h3> <p><span style="color: #808080;">微博：<a style="text-decoration: underline;" title="DMDlink 1" href="http://weibo.com/lfscn" target="_blank"><span style="text-decoration: underline;"><span style="color: #808080; text-decoration: underline;">cocacoldnotcola</span></span></a></span></p> <p><span style="color: #808080;">微信：cocacold</span></p> <p><strong><span style="color: #333333;">Hello everyone, I'm Vincent, I just arrive at WP AE department, hope have a great time with you guys!</span></strong></p> <p><span style="color: #333333;">My hobbies are photography, travel, video games, basketball and swimming, I'm glad to communicate this subjects with you guys. By the way, I've studied in France for 7 years, so I'm a french speaker, if you interested in french or France, please feel free to discuss that with me. </span></p> <h3><span style="color: #333333;">Contact:</span></h3> <p><span style="color: #333333;">By weibo:<a style="text-decoration: underline;" title="DMDlink 2" href="http://weibo.com/lfscn" target="_blank"><span style="text-decoration: underline;"><span style="color: #333333; text-decoration: underline;">cocacoldnotcola</span></span></a></span></p> <p><span style="color: #333333;">By wechat:cocacold</span></p> <p><a style="text-decoration: underline;" title="DMDlink 3" href="{$WEBLINK}" target="email">{$create_date}</a></p> </div> </body> </html>''')
   