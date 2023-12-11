import os
import numpy as np
# environment = 'empty'
environment = 'obstacles'

folder_path = f'data/{environment}'
sensors_extension = 'sensorValues.npy'
motors_extension = 'motorValues.npy'


def Create_Dict(file_extension):
    data_dict = {}
    files = [f for f in os.listdir(folder_path) if f.endswith(file_extension)]
    for file_name in files:
        key = file_name.replace(file_extension, '')
        file_path = os.path.join(folder_path, file_name)
        values = np.load(file_path)
        data_dict[key] = values
    print(data_dict)
    return data_dict

def Dict_To_File(new_file_name, data_dict, num_values_to_write=100):
    output_file_path = new_file_name
    with open(output_file_path, 'w') as output_file:
        for key, values in data_dict.items():
            # Write only the first num_values_to_write values
            values_to_write = values[:num_values_to_write]
            values_str = ', '.join(map(str, values_to_write))
            output_file.write(f"{key}: {values_str}\n")


sensors_dict = Create_Dict(sensors_extension)
Dict_To_File(f'{environment}_sensors_dict.txt',sensors_dict)


motors_dict = Create_Dict(motors_extension)
Dict_To_File(f'{environment}_motors_dict.txt',motors_dict)


