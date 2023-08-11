import os
import pandas as pd
import time 


folder_path = './output'  # 삭제하려는 폴더의 경로

# 폴더 안에 있는 모든 파일을 순회하며 삭제
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
            print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")


# 입력 폴더 경로와 출력 폴더 경로
input_folder = './'  # 입력 폴더의 경로를 정확히 지정해주세요.
output_folder = './output'


f = open('2DID_sorting.txt',"r") 
data = f.read().splitlines()
print(data)



# 출력 폴더가 없다면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 입력 폴더 내의 모든 CSV 파일에 대해 처리
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.CSV'):
        print(f"현재 처리 중인 파일: {filename}")
        input_csv_path = os.path.join(input_folder, filename)
        output_csv_path = os.path.join(output_folder, filename)
        
        # CSV 파일을 DataFrame으로 로드
        df = pd.read_csv(input_csv_path,skiprows=1,index_col=0) ### skiprows csv 시작하는 행을 삭제
        
        print(df)
        
        selected_row = df.loc[data, :]  # 선택할 행의 인덱스를 정확히 지정해주세요.
        
               
        selected_row.to_csv(output_csv_path)
        print(f"2 행의 데이터와 일치하는 셀의 열만 남긴 새로운 CSV 파일이 생성되었습니다: {output_csv_path}")
         

        
 
        
        

