import ir_datasets
dataset = ir_datasets.load("lotte/lifestyle/dev/forum")
for qrel in dataset.qrels_iter():
    qrel # namedtuple<query_id, doc_id, relevance, iteration>