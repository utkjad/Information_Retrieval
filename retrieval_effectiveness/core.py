"""
Homework - 5
Utkarsh J
"""
__author__ = "Utkarsh J"

from collections import defaultdict
import math

relevant_docs =  defaultdict(list)
document_dict = defaultdict(dict)
total_precision = defaultdict(int)
ideal_dcg_list = []
current_relevant = 0

def get_all_documents(path):
    """ Gets all ID and Score for particular query from results of HW4
    """
    with open(path, 'r') as file_obj:
            for line in file_obj.readlines():
                temp_list = line.split(' ')
                rank = int(temp_list[0][:-1])
                id = temp_list[1]
                score = float(temp_list[2][:-1])
                document_dict[rank]["id"] = int(id[id.find('-')+1:])
                document_dict[rank]["score"] = score

def read_relevence(query_id):
    """
    :param query_id: Get relevant documents w.r.t. query ID
    """
    with open('relevence.txt','r') as file_obj:
        for line in file_obj.readlines():
            temp_list = line.split(' ')
            if temp_list[0] == str(query_id):
                relevant_docs[query_id].append(int(temp_list[2][temp_list[2].find('-')+1:]))

def get_precision_and_recall(query_id):
    """
    :param query_id: Query ID
    Gets precision and recall for all documents from then result of HW4
    """
    total_relevant_documents = len(relevant_docs[query_id])
    #print "total_relevant_document" + str(total_relevant_documents)

    def _is_it_relevant(id):
        return bool(id in relevant_docs[query_id])

    global current_relevant
    for rank, values  in document_dict.iteritems():
        if _is_it_relevant(values['id']):
            current_relevant += 1
            document_dict[rank]["relevance"] = 1
        else:
            document_dict[rank]["relevance"] = 0

        document_dict[rank]["recall"] = float(current_relevant) / total_relevant_documents
        document_dict[rank]["precision"] = float(current_relevant) / rank
        if _is_it_relevant(values['id']):
            total_precision[query_id] += document_dict[rank]["precision"]

def precision_at_k(k):
    """
    :param k: Position
    precision at K
    """
    return document_dict[20]["precision"]

def mean_average_precision(input_query_id):
    """ Calculate precision for all documents given ion the input_query_id"""
    sum = 0
    for query_id in input_query_id:
        total_relevant_docs = len(relevant_docs[query_id])
        sum += (total_precision[query_id] / total_relevant_docs)
    return sum/len(input_query_id)

def get_actual_dcg():
    """ Calculated the actual DCG"""
    dcg = 0
    for rank, info in document_dict.iteritems():
        if rank == 1:
            dcg += info["relevance"]
        else:
            dcg += info["relevance"] * 1.0/float(math.log(rank,2))
        info["dcg"] = dcg

def get_ideal_dcg(id):
    """ gets ideal DCG"""
    # Get list
    global  ideal_dcg_list
    total_relevant_documents = len(relevant_docs[id])
    ideal_dcg = 1
    ideal_dcg_list.append(ideal_dcg)
    for rank in range(2,total_relevant_documents + 1):
        ideal_dcg += 1.0/float(math.log(rank,2))
        ideal_dcg_list.append(ideal_dcg)
    ideal_dcg_list += [ideal_dcg_list[-1]] * (100 - total_relevant_documents)

def get_ndcg():
    """ Calculates NDCG and stores it in the master dictionary named document_dict"""
    for rank,value,ideal_dcg in zip(document_dict.keys(), document_dict.values(), ideal_dcg_list ) :
        document_dict[rank]["ndcg"] = document_dict[rank]["dcg"] / ideal_dcg

def reintialize():
    """ Reinitialize entities before switching to the next query"""
    global ideal_dcg_list, current_relevant, document_dict
    ideal_dcg_list = []
    document_dict.clear()
    current_relevant = 0

if __name__ == "__main__":
    names = ['portable_operating_systems.txt', 'code_optimization_for_space_efficiency.txt', 'parallel_algorithms.txt']
    ids = [12, 13,19]
    for id, name in zip(ids, names):
        print "Query " + name + "(" + str(id) + ")"
        print "RANK ID SCORE RELEVANCE_LEVEL PRECISION RECALL NDCG"
        reintialize()
        read_relevence(id)
        get_all_documents(name)
        get_precision_and_recall(id)
        get_actual_dcg()
        get_ideal_dcg(id)
        get_ndcg()
        for key,value in document_dict.iteritems():
            print str(key) + " " + str(value["id"]) + " " +\
                  str(value["score"]) + " " +\
                  str(value["relevance"]) + " " +\
                  str(value["precision"]) + " " +\
                  str(value["recall"]) + " " +\
                  str(value["ndcg"])
    #     print "precision at 20 = " + str(precision_at_k(20))
    #     print ""
    #     print ""
    #     print ""
    # print "MAP = " + str(mean_average_precision(ids))