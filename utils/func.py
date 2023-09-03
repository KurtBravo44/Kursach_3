from utils import encoding_data

def sort_file(file, option):
    '''Функция сортирует файл по заданному значению в обратном порядке'''
    sort_file = sorted(file, key=lambda x: x.get(option, ""), reverse=True)
    return sort_file


def output_of_operations(file, i):
    '''Функция принимает 2 аргумента:
    1 - файл для чтения
    2 - позиция, итерируемого файла
    Функция итерируется по списку словарей, находя в ней нужные ключи и их значения,
    после чего образует форму операции, соответствующей заданным параметрам'''
    operation_date = (file[i]['date'])
    type_operation = (file[i]['description'])
    operation_to = (file[i]['to'])
    operation_currency = (file[i]['operationAmount']['currency']['name'])
    operation_sum = (file[i]['operationAmount']['amount'])

    coding_number_to = encoding_data.encoding_data(operation_to)


    if 'from' in file[i]:

        operation_from = file[i]['from']

        coding_number_from = encoding_data.encoding_data(operation_from)

        return (f'{operation_date[:10].replace("-", ".")} {type_operation}\n'
                f'{coding_number_from} --> {coding_number_to}\n'
                f'{operation_sum} {operation_currency}')
    else:
        return (f'{operation_date[:10].replace("-", ".")} {type_operation}\n'
                f'{coding_number_to}\n'
                f'{operation_sum} {operation_currency}')






