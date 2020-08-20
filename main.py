import csv
import networkx as nx
import json
# import matplotlib.pyplot as plt
my_dict={}
with open('DBLP-SIGWEB/paper_authors.csv','rt') as obj:
  table = csv.reader(obj,delimiter=',')
  for row in table:
    key=int(row[0])
    if key in my_dict:
      my_dict[key].append(int(row[1]))
    else:
      my_list=[]
      my_list.append(int(row[1]))
      my_dict[key]=my_list
print(my_dict[1458185])
# x = set()
# for key,value in my_dict.items():
#   for val in value:
#     x.add(val)
# print(len(x))

# with open('DBLP-SIGWEB/my_dict.json', 'w') as fp:
#     json.dump(my_dict, fp)
print(len(my_dict))
co_author={}
isolated_authors=[]
for paper,authors in my_dict.items():
    if len(authors)==1:
      # print('hi')
      isolated_authors.append(authors[0])
      continue
    for author in authors:
      for assoc_auth in authors:
        if assoc_auth!=author:
          if author in co_author.keys():
            if assoc_auth in co_author[author].keys():
              co_author[author][assoc_auth] += 1
            else:
              co_author[author][assoc_auth]=1
          else:
            temp={}
            temp[assoc_auth]=1
            co_author[author]=temp;
isolated_authors=list(set(isolated_authors))
for auth in isolated_authors:
  if auth in co_author.keys():
    isolated_authors.remove(auth)


 
# with open('DBLP-SIGWEB/co_authors.json', 'w') as fp:
#     json.dump(co_author, fp)

print(len(co_author))
author_scores={}
with open('DBLP-SIGWEB/authors_info.csv','rt') as obj:
  table = csv.reader(obj,delimiter=',')
  for row in table:
    key=int(row[0])
    author_scores[key] = float(row[1])
print(author_scores[81384593792])
# seed_scores={}
# for key in co_author.keys():
#   seed_scores[key]=author_scores[key]
# with open('DBLP-SIGWEB/seed_scores.json', 'w') as fp:
#     json.dump(seed_scores, fp)    


G=nx.DiGraph();
for author,assocs in co_author.items():
  for author2,edge in assocs.items():
    G.add_edge(author,author2,weight=edge)

for author in isolated_authors:
  G.add_node(author)

# print(G.edges(data=True))
# pos=nx.spring_layout(G)
# nx.draw(G,pos)
# labels = nx.get_edge_attributes(G,'weight')
# nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
# plt.savefig('DBLP-SIGWEB/graph2.png')

pr = nx.pagerank(G,personalization=author_scores,max_iter=100)
# for author in isolated_authors:
#   pr[author]=author_scores[author]
print(len(pr))
with open('DBLP-SIGWEB/pagerank_100.json', 'w') as fp:
    json.dump(pr, fp)

i=0
for key,value in pr.items():
  print(key)
  print(value)
  i=i+1
  if i==10:
    break






