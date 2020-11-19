import sys
import os
import math
import re
import json

IndexFolderName = "IndexFolder"
ContentFolderName = "../ContentFolder"
queriesFile = "Queries.txt"
termIdFile = "TermIDFile.json"
invertedIndex = "InvertedIndex.json"
outputFile = "Output.txt"

k = 5
N = 1006
# term_doc_dic: key is termID, value is list of docsID
term_doc_dic = {}
# dic of each token weight in query
query_w_dic = {}
# wtf_doc_Dic {docID: {termID: ft}}
doc_w_dic = {}
TermID_file = "TermIDFile.json"
DocumentID_file = "DocumentIDFile.json"
Tokens_num_file = "Tokens_num.txt"
Stats = "Stats.txt"
# FolderName = "/../FolderName/"

def test_term_termID(term):
    # takes in a term Term, and return the corresponding TermID
    load_f = open(TermID_file, 'r')
    load_dict = json.load(load_f)
    load_f.close()
    return load_dict[term]["termID"]

def update_doc_freq_for_term(termID):
    # to take a TermID and return its inverted list iList
    load_f = open(invertedIndex, 'r')
    load_dict = json.load(load_f)
    load_f.close()
    for d in dict(load_dict[str(termID)]).keys():
        print("doc id isis: " + d)
        if d not in doc_w_dic.keys():
            doc_w_dic[d] = {}
        doc_w_dic[d][str(termID)] = load_dict[str(termID)][d]

# take termID and add to term_doc_dic
def make_term_doc_dic(termID):
    with open(invertedIndex, 'r') as load_f:
        load_dict = json.load(load_f)
        inverted = (dict)(load_dict[termID])
        term_doc_dic[termID] = inverted.keys()
        load_f.close()

def test_docID_doc(docID):
    # take a DocumentID and returns the document name it corresponds to
    load_f = open(DocumentID_file, 'r')
    load_dict = json.load(load_f)
    docName = load_dict[str(docID)]["doc_name"]
    load_f.close()
    return docName

def calculateQueryWTF(tf_all_docs):
    w_tf = 1 + math.log(tf_all_docs, 10)
    return w_tf

def ranker(IndexFolderName, ContentFolderName):
    # cosine similarity and vector space ranking
    queries = open(queriesFile, 'r')
    lines = queries.readlines()
    # get termId, frequency of the term
    with open(termIdFile, 'r') as load_f:
        load_dict = json.load(load_f)
    load_f.close()
    # run for every query line
    out = open(outputFile, "w+")
    for line in lines:
        line = line.strip()
        print("line is: " + line)
        terms = re.split("[\s]+", line)
        print("terms is: " + str(terms))
        # calculate weight division for query and doc of each term
        div_query_w = 0

        termID_list = []
        for t in terms:
            termID = load_dict[t]["termID"]
            termID_list.append(termID)
            if termID not in term_doc_dic.keys():
                make_term_doc_dic(str(termID))
            # get number of docs that have the term
            tf_all_docs = len(term_doc_dic[str(termID)])
            print("tf_all_docs: " + str(tf_all_docs))
            if query_w_dic.__contains__(termID):
                continue
            query_w_dic[termID] = calculateQueryWTF(tf_all_docs)
            print("query_w_dic[termID]: " + str(query_w_dic[termID]))
            # print("termID is: " + str(termID) + " wtf is: " + str(query_w_dic[termID]))
            idf = math.log(N/tf_all_docs, 10)
            print("idf is: " + str(idf))
            w = query_w_dic[termID] * idf
            print("w is: " + str(w))
            query_w_dic[termID] = w
            div_query_w += w * w
            # update doc_w_dic doc wtf for every term
            update_doc_freq_for_term(termID)
        print("doc_w_dic for freq: " + str(doc_w_dic))
        print("termID_list is: " + str(termID_list))
        print("term_doc_dic is: " + str(term_doc_dic))
        # calculate and update query_w_dic
        for i in query_w_dic:
            if len(terms) == 1:
                query_w_dic[i] = 1
            else:
                query_w_dic[i] = query_w_dic[i]/math.sqrt(div_query_w)
        print("query_w_dic lala is: " + str(query_w_dic))

        # calculate and update doc_w_dic
        for d in doc_w_dic.keys():
            div_doc_w = 0
            for t in dict(doc_w_dic[d]).keys():
                if t in dict(doc_w_dic[d]).keys():
                    doc_w_dic[d][t] = 1 + math.log((float)(doc_w_dic[d][t]), 10)
                    div_doc_w += doc_w_dic[d][t] * doc_w_dic[d][t]
            if len(terms) == 1:
                doc_w_dic[d][t] = 1
            else:
                doc_w_dic[d][t] = doc_w_dic[d][t] / math.sqrt(div_doc_w)
        print("doc_w_dic lala is: " + str(doc_w_dic))

        # calculate score for each doc
        score = {}
        for t in termID_list:
            for d in term_doc_dic[str(t)]:
                if d not in score.keys():
                    score[d] = 0.0
                if str(t) in dict(doc_w_dic[d]).keys():
                    score[d] += (float)(query_w_dic[t]) * (float)(doc_w_dic[d][str(t)])
        print("score is: " + str(score))

        # write into output.txt
        ranked_score = sorted(score, key=score.get, reverse=True)

        out.write(line + "\n")
        out.write(str(terms) + "\n")
        idx = 0
        for doc_id in ranked_score:
            if idx == k:
                break
            out.write(doc_id + "\t" + test_docID_doc(doc_id) + "\n")
            f = open(ContentFolderName+"/" + test_docID_doc(doc_id), "r")
            fb = f.read(200)
            out.write(fb + "\n")
            # 200 bytes of contents in the doc
            out.write(str(score[doc_id]) + "\n")
            line = ""
            for i in range(len(terms)):
                termID = termID_list[i]
                # print("termID is: " + str(doc_w_dic[str(doc_id)].keys()))
                print("termID is: " + str(termID))
                print("doc_w_dic is: " + str(doc_w_dic[str(doc_id)].keys()))
                if str(termID) in doc_w_dic[str(doc_id)].keys():
                    strs = str((float)(query_w_dic[t]) * (float)(doc_w_dic[d][str(t)]))
                    print("strs is: " + strs)
                    line += terms[i] + ":" + strs + "; "
                else:
                    line += terms[i] + ":" + "0.0; "
            line.strip("; ")
            out.write(line+"\n")
            out.write("\n")
            idx += 1
        out.write("\n\n")
    out.close()
ranker(IndexFolderName, ContentFolderName)








