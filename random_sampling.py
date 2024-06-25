import os
import random
import shutil

def sampling_data(dir_list_path, destination_dir, sample_length):
    dir_list = os.listdir(dir_list_path)

    total_data_length = 0
    for dir in dir_list:
        data_path = os.path.join(dir_list_path, dir)
        total_data_length += len(os.listdir(data_path))
    
    dir_length = {}
    for dir in dir_list:
        data_path = os.path.join(dir_list_path, dir)
        dir_length['{}'.format(dir)] = len(os.listdir(data_path))
    
    sample_length = sample_length
    sample_data_length = {key: int((value / total_data_length) * sample_length)
                          for key, value in dir_length.items()}
    
    destination_dir = destination_dir
    for dir, cnt in sample_data_length.items():
        data_path = os.path.join(dir_list_path, dir)
        file_list = os.listdir(data_path)
        sample_file_list = random.sample(file_list, cnt)

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        
        for file_name in sample_file_list:
            source_file_path =  os.path.join(data_path, file_name)
            destination_file_path = os.path.join(destination_dir, file_name)

            if os.path.exists(source_file_path) and os.path.isfile(source_file_path):
                shutil.copy2(source_file_path, destination_file_path)
            else:
                print(f'File not found: {file_name}')