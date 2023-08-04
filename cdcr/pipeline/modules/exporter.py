from cdcr.structures import DocumentSet
from cdcr.util.document_exporter import DocumentExporter
import datetime
import json

def document_export(document_set: DocumentSet):
    """
    Export a document set with ShelveExporter.

    Arguments:
        document_set: DocumentSet to export.

    Returns:
        The exported document_set.
    """
    results = []
    for entity in document_set.entities:
        if len(entity.members) > 1:
            result = { 'representative': entity.representative, 'references': [] }
            for m in entity.members:
                member = {}
                member['representative'] =  entity.representative
                member['doc_id'] = str(m.document.doc_id)
                member['id'] = str(m.id)
                member['member'] = str(m)
                member['mention_type'] = m.annot_type
                member['coref_subtype'] = m.coref_subtype
                member['begin_char'] = m.begin_char
                member['end_char'] = m.end_char
                member['sentence_start_char'] = m.sentence.begin_char
                member['sentence_end_char'] = m.sentence.end_char
                result['references'].append(member)
            results.append(result)

    filepath = 'data/exported/results-{date:%Y-%m-%d_%H-%M-%S}.json'.format(date=datetime.datetime.now())
    with open(filepath, 'w') as jsonfile:
            json.dump(results, jsonfile)

    return document_set