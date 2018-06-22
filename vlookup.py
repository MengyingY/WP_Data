#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 19:41:49 2018

@author: yangmengying1
"""

import pandas as pd
global rightdata, leftdata
rightdata=pd.read_csv('',encoding="gb2312")
leftdata=pd.read_csv('',encoding="gb2312")

def vlookup(leftdata,rightdata,searchcolumnld,searchcolumnrd,matchcolumn,destination):
    
    newdata=pd.merge(
            leftdata,
            rightdata,
            left_on=searchcolumnld,
            right_on=searchcolumnrd,
            how='left'
                
            )
    columns1=leftdata.columns.values.tolist()
    columns1.append(matchcolumn)
    newdata=newdata[columns1]
    newdata.to_csv('/Users/yangmengying1/Downloads/1.csv')

if __name__=='__main__':
    ls=input('请输入leftdata中作为匹配的列：')
    rs=input('请输入rightdata中作为匹配的列：')
    mc=input('请输入需要匹配的列：')
    dpath=input('请输入匹配结果存储路径：')
    vlookup(leftdata,rightdata,ls,rs,mc,dpath)

