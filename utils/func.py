import encoding_data

def sort_file(file):
    sort_file = sorted(file, key=lambda x: x.get('date', ""), reverse=True)
    return sort_file


def output_of_operations(file, i):

    # print(sort_json_file[i])
    operation_date = (file[i]['date'])
    type_operation = (file[i]['description'])
    operation_to = (file[i]['to'])
    operation_currency = (file[i]['operationAmount']['currency']['name'])
    operation_sum = (file[i]['operationAmount']['amount'])

    coding_number_to = encoding_data.encoding_data(operation_to)

    if 'from' in file[i]:

        operation_from = file[i]['from']

        coding_number_from = encoding_data.encoding_data(operation_from)

        print(f'{operation_date[:10].replace("-", ".")} {type_operation}\n'
                f'{coding_number_from} --> {coding_number_to}\n'
                f'{operation_sum} {operation_currency}')
    else:
        print(f'{operation_date[:10].replace("-", ".")} {type_operation}\n'
                f'{coding_number_to}\n'
                f'{operation_sum} {operation_currency}')

