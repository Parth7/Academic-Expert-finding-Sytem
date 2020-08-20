import csv
import operator
import json
import re
def search_query(input_query,inverted_index):
	paper_id=[]
	author_id=[]
	# pattern = re.compile('[\W_]+')
	# word = pattern.sub(' ',input_query)
	pattern = re.compile(input_query)
	for key in inverted_index.keys():
		if (pattern.search(key)):
			for paper in inverted_index[key]:
				paper_id.append(paper)
	paper_id=set(paper_id)
	paper_id=list(paper_id)
	return paper_id
def display_results(query):
	inverted_index={}
	with open('DBLP-SIGWEB/concepts.csv','rt') as obj:
		table = csv.reader(obj,delimiter=',')
		for row in table:
			key=row[1].lower()
			if key in inverted_index:
				inverted_index[key].append(int(row[0]))
			else:
				my_list=[]
				my_list.append(int(row[0]))
				inverted_index[key]=my_list
	with open('DBLP-SIGWEB/author_tags.csv','rt') as obj:
		table = csv.reader(obj,delimiter=',')
		for row in table:
			key=row[1].lower()
			if key in inverted_index:
				inverted_index[key].append(int(row[0]))
			else:
				my_list=[]
				my_list.append(int(row[0]))
				inverted_index[key]=my_list
	paper_authors={}
	with open('DBLP-SIGWEB/paper_authors.csv','rt') as obj:
		table = csv.reader(obj,delimiter=',')
		for row in table:
			key=int(row[0])
			if key in paper_authors:
				paper_authors[key].append(int(row[1]))
			else:
				my_list=[]
				my_list.append(int(row[1]))
				paper_authors[key]=my_list
	display_info={}
	with open('DBLP-SIGWEB/display_info.csv','rt') as obj:
		table = csv.reader(obj,delimiter=',')
		for row in table:
			key=int(row[0])
			my_list=[]
			my_list.append(row[1])
			my_list.append(row[2])
			my_list.append(row[3])
			my_list.append(row[4])
			my_list.append(row[5])
			my_list.append(row[6])
			display_info[key]=my_list
	pr={}
	with open('DBLP-SIGWEB/pagerank_100.json', 'r') as fp:
	    pr = json.load(fp)
	ppr={}
	for key,value in pr.items():
		key=int(key)
		value=float(value)
		ppr[key]=value
	pr=ppr
	# query = input("Search here: ")
	paper_list=search_query(query,inverted_index)
	if paper_list==[]:
		print("No Results found")
		exit(0)
	author_ids=[]
	for paper_id in paper_list:
		for author_id in paper_authors[paper_id]:
			author_ids.append(author_id)
	author_ids=list(set(author_ids))
	result=[]
	for author_id in author_ids:
		if author_id in pr.keys():
			result.append((author_id,pr[author_id]))
	if result==[]:
		print("No Results found")
		exit(0)
	final_res=sorted(result,key=lambda x:x[1],reverse=True)
	i=0
	final_display_list=[]
	for item in final_res:
		print("['Author_Name','Year_first','Year_last','Total_Publications','Citation_Count','Avg_cite']")
		print(display_info[item[0]])
		final_display_list.append(display_info[item[0]])
		i=i+1
		if i==7:
			break
	return final_display_list








