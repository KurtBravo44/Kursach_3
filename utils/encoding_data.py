def encoding_data(data):

    spited_data = data.split()
    if len(spited_data) == 2 and "Счет" not in data:
        data_1 = spited_data[0]
        data_2 = spited_data[1]
        coreved = data_1 + " " + data_2[:6] + "******" + data_2[12:]
        return coreved

    elif 'Счет' in data:
        data_1 = spited_data[0]
        data_2 = spited_data[1]
        covered = data_1 + " " + "**" + data_2[16:]
        return covered

    else:
        data_1 = spited_data[0]
        data_2 = spited_data[1]
        data_3 = spited_data[2]
        covered = data_1 + " " + data_2 + " " + data_3[0:6] + "******" + data_3[12:]
        return covered



