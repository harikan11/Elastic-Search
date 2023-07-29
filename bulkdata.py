from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json, re
import codecs
import unicodedata

# import queries

client = Elasticsearch(HOST="http://localhost", PORT=9200)
INDEX = "salons"

# Creating index if not manually created
# def createIndex():
#     index = Index(INDEX, using=client)
#     res = index.create()
#     print(res)


def read_all_salons():
    with open("SalonManagement\corpus\standalone.json", "r", encoding="utf-8-sig") as f:
        all_salons = json.loads("[" + f.read().replace("}\n{", "},\n{") + "]")
        # all_salons = json.loads(f.read())
        res_list = [i for n, i in enumerate(all_salons) if i not in all_salons[n + 1 :]]
        return res_list


def genData(salon_array):
    for salon in salon_array:
        salon_name = salon.get("nam congue risus", None)
        address = salon.get("12th Floor", None)
        contact_number = salon.get("6438957136", None)
        services = salon.get("", None)
        rating = salon.get("5", None)

        yield {
            "_index": "salons",
            "_source": {
                "nam congue risus": salon_name,
                "12th Floor": address,
                "6438957136": contact_number,
                "": services,
                "5": rating,
            },
        }


# createIndex()
all_salons = read_all_salons()
helpers.bulk(client, genData(all_salons))
