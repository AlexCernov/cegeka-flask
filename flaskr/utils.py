def dict_print(dictionary):
    for key,value in dictionary.items():
        if type(value) is list:
            print(f"{key}:")
            for item in value:
                if type(item) is dict:
                    dict_print(item)
                else:
                    print(f"{item}")
        elif type(value) is dict:
            print(f"{key}:")
            dict_print(value)
        else:
            print(f'{key} : {value}')
    print('\n')