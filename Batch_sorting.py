import os
import pandas as pd

current_directory = os.getcwd()

# 입력 폴더 경로와 출력 폴더 경로
input_folder = './'  # 입력 폴더의 경로를 정확히 지정해주세요.
output_folder = './output'
selected_row_index = 1
selected_row_data = ['SerialNumber' , 'Site', 'TestResult', 'hbin#', 'hbin', 'sbin#', 'sbin', 'startTime', 'stopTime' , 'testTime(s)', 'DeviceName', 'HandlerID', 'TesterID', 'TestPGM', 'LotID', '6_ERROR_MESSAGE', '7_ERROR_MESSAGE']  # 여러 데이터 값 리스트


# 출력 폴더가 없다면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 입력 폴더 내의 모든 CSV 파일에 대해 처리
for filename in os.listdir(input_folder):
    if filename.endswith('.CSV'):
        print(f"현재 처리 중인 파일: {filename}")
        input_csv_path = os.path.join(input_folder, filename)
        output_csv_path = os.path.join(output_folder, filename)
        
        # CSV 파일을 DataFrame으로 로드
        df = pd.read_csv(input_csv_path)
        
        # 선택된 행을 가져오기
        selected_row = df.iloc[selected_row_index]  # 선택할 행의 인덱스를 정확히 지정해주세요.
        
        print (selected_row_index)
        
        # 선택된 행의 데이터와 일치하는 셀의 열만 선택하여 새로운 DataFrame 생성
        matching_columns = [col for col, cell_data in selected_row.items() if cell_data in selected_row_data]
        new_df = df[matching_columns]
        
        # 새로운 CSV 파일로 저장
        new_df.to_csv(output_csv_path, index=False)
        
        print(f"특정 행의 데이터와 일치하는 셀의 열만 남긴 새로운 CSV 파일이 생성되었습니다: {output_csv_path}")
