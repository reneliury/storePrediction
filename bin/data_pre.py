# coding: utf-8

import csv
import re
company_data="data/company_data.csv"
god_data="data/God_File.csv"	

def load_company_data(company_data,god_data):
	#load company_data
	file=open(company_data,'rU')
	reader = csv.reader(file)
	companyIndex={}#公司指数的map，key为公司号，value为字典（季度：[涨跌，day1_index,day2_index...])
	
	for line in reader:
		segs=line[0].strip().split("|||")
		cNum=re.findall('\d+',segs[0])[0]
		date=segs[1]
		quarter=int(time_to_quarter(date))
		indexValue=segs[2]#指数值
		if cNum not in companyIndex:
			companyIndex[cNum]={}
		elif quarter not in companyIndex[cNum]:
			companyIndex[cNum][quarter]=["",indexValue]#第一个存放涨跌
		else:
			companyIndex[cNum][quarter].append(indexValue)
	#load_god_data
	file=open(god_data,'rU')
	reader = csv.reader(file)
	for line in reader:
		segs=line
		valid=segs[0]
		cNum=segs[1]
		quarter=int(segs[2])
		up_down=segs[3]
		companyIndex[cNum][quarter][0]=up_down
	return companyIndex

		
def time_to_quarter(date):#返回第几个季度
	date_y_m_d=get_y_m_d(date)
	quarter= (int(date_y_m_d[0])-2011)*4+(int(date_y_m_d[1]))/4+1
	return str(quarter)
def get_y_m_d(date):
	segs=date.split("-")
	year=segs[0]
	month=segs[1]
	day=segs[2]
	return year,month,day

if __name__=='__main__':
	companyIndex=load_company_data(company_data,god_data)
	file_object=open('data/data.pre','w+')
	for cNum in companyIndex:
		for quarter in companyIndex[cNum]:
			for index in range(len(companyIndex[cNum][quarter])-1):
				file_object.write(cNum+"\t"+str(quarter)+"\t"+str(index+1)+"\t"+companyIndex[cNum][quarter][0]+"\t"+companyIndex[cNum][quarter][index+1]+"\n")
	file_object.close()
