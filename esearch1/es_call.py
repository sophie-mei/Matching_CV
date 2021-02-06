from elasticsearch import Elasticsearch 
from elasticsearch_dsl import Search, Q 

def esearch(NOM="", compétence=""):      
    mot = Elasticsearch()      
    q = Q("bool", should=[Q("match", NOM=NOM),       
    Q("match", compétence=compétence)], minimum_should_match=1)  
    s = Search(using=mot, index="together").query(q)[0:20] 
    response = s.execute()
    #print('Total% d hits found.' % response.hits.total)     
    search = get_results(response)    
    return search  
def get_results(response): 
    results = []  
    for hit in response: 
        result = (hit.compétence)    
        results.append(result)  
    return results

if __name__ == '__main__':   
    print ("Sophie ZHANG : \ n", esearch (NOM = "ZHANG")) 
    print ("les 4 premiers python : \ n", esearch (compétence = "python") )