import os
import pandas as pd

def process_conversation(file_path):
    if os.path.isfile(file_path) and file_path.endswith('.txt'):
        with open(file_path, 'r', encoding = 'utf-8') as file:
            lines = file.readlines()
        
        lines = [line.split(': ', 1)[-1].strip() for line in lines]
        result = '\\n '.join(lines)

        return result
    else:
        return f'File not found: {file_path}'

def process_dataframe(data_dir, output_path):
    columns = ['idx', 'class', 'conversation']
    data = pd.DataFrame(columns = columns)
    
    for i, file_name in enumerate(os.listdir(data_dir)):
        # 텍스트 파일 경로
        file_path = os.path.join(data_dir, file_name)

        sample = {
            'idx': i,
            'class': '일반 대화',
            'conversation': process_conversation(file_path)
        }
        data.loc[len(data)] = sample
        
    data.to_csv(output_path, index = False, encoding = 'utf-8')