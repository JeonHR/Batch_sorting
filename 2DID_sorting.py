import os
import pandas as pd



folder_path = './output'  # Python 실행 전 삭제하는 폴더 경로


# 폴더 안에 있는 모든 파일을 순회하며 삭제
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename) ## File Path
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
    os.makedirs(output_folder) ## 폴더 자동생성

# 입력 폴더 내의 모든 CSV 파일에 대해 처리
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.csv'): ###모든 확장자를 소문자로 만드는 방법
        print(f"현재 처리 중인 파일: {filename}")
        input_csv_path = os.path.join(input_folder, filename)
        output_csv_path = os.path.join(output_folder, filename)
        
        # CSV 파일을 DataFrame으로 로드
        df = pd.read_csv(input_csv_path,skiprows=1,index_col=0) ### skiprows csv 시작하는 행을 삭제
        ## 첫열에 생성되는 값 삭제해주는 과정을 진행
        
        print(df)
        
        try:
            # data 리스트에 포함된 값과 일치하는 행만 선택하여 새로운 DataFrame 생성
            # 이게 일치하는 행만 확인되게 만드는 핵심
            selected_rows = df[df.index.isin(data)]
            
            # 선택된 행이 비어있지 않은 경우에만 CSV 파일로 저장
            # 일치하지 않는 것만 형성되는 것 좋은 생각임.
            if not selected_rows.empty:
                selected_rows.to_csv(output_csv_path)
                print(f"2 행의 데이터와 일치하는 셀의 열만 남긴 새로운 CSV 파일이 생성되었습니다: {output_csv_path}")
            else:
                print("일치하는 값이 없어 CSV 파일을 생성하지 않았습니다.")

        except KeyError as e:
            print(e)



        
 
        
        

