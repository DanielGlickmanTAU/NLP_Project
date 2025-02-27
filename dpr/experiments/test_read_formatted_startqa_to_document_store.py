from dpr.experiments.flows import create_new_ds_and_new_retriever
from dpr.experiments.document_store import load_saved_document_store
from dpr.retrievers.retrieves import load_retriever

should_update_document_store = False

doc_dir = 'data/'
formated_file_name = doc_dir + 'startqa_corpus_formatted_for_documentstore.json'
# formated_file_name = doc_dir + 'sample_startqa_corpus_formatted_for_documentstore.jsonl'

formated_file_name = doc_dir + 'startqa_corpus_formatted_for_documentstore.json'
if should_update_document_store:
    create_new_ds_and_new_retriever(formated_file_name)

    print('done')

# loading existing store
else:
    document_store = load_saved_document_store()
    retriever = load_retriever(document_store)
    print('1')
