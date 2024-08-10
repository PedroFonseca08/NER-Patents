def convert_annotations_to_strings(text, annotations, match_length):
    entities = annotations["entities"]
    result = []

    for start, end, label in entities:
        entity_number = []
        start = start-match_length
        end = end-match_length
        entity_text = text[start:end]

        while entity_text and (entity_text[0] == ' ' or entity_text[0] == '.'):
            entity_text = entity_text[1:]
            start +=1

        while entity_text and (entity_text[-1] == ' ' or entity_text[-1] == '.'):
            entity_text = entity_text[:-1]
            end -=1
        entity_number.append(start)
        entity_number.append(end)

        result.append([entity_text, label, entity_number])

    return result