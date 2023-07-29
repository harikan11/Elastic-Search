import json


#def standard_analyzer(query):
    #q = {
        #"analyzer": "standard",
        #"text": query
    #}
    #return q


def basic_search(query):
    q = {
        "query": {
            "query_string": {
                "query": 'PO Box 79464'
            }
        }
    }
    return q


def search_with_field(query, field):
    q = {
        "query": {
            "match": {
                field: query
            }
        }
    }
    return q


def multi_match(query, fields=['salon_name', 'ratings'], operator='or'):
    q = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "operator": operator,
                "type": "best_fields"
            }
        }
    }
    return q


def agg_multi_match_q(query, fields=['salon_name', 'ratings'], operator='or'):
    q = {
        "size": 500,
        "explain": True,
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "operator": operator,
                "type": "best_fields"
            }
        },
        "aggs": {
            "Services Filter": {
                "terms": {
                    "field": "facial.keyword","hairspa.keyword"
                    "size": 10
                }
            },
            
            
            
        }
    }

    q = json.dumps(q)
    return q


def agg_q():
    q = {
        "size": 0,
        "aggs": {
            "Category Filter": {
                "terms": {
                    "field": "ratings",
                    "size": 10
                }
            }
        }
    }

    return q


def agg_multi_match_and_sort_q(query, fields, operator='or',sort_num=10):
    print(fields)
    print(query)
    print('sort num is ', sort_num)
    q = {
        "size": sort_num,
        "sort": [
            {"views": {"order": "desc"}},
        ],
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "operator": operator,
                "type": "best_fields"
            }
        },
        "aggs": {
            "Services Filter": {
                "terms": {
                    "field": "facial.keyword",
                    "size": 10
                }
            },
            
        }
    }
    q = json.dumps(q)
    return q
