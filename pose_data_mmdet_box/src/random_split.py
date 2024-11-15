import os
import random
import shutil

# 폴더 경로 설정
folder_path = 'cropped_img_four_parts'

# 파일 리스트 가져오기
file_list = os.listdir(folder_path)

# 파일 리스트 섞기
random.shuffle(file_list)

# 총 파일 수 계산
total_files = len(file_list)
train_size = int(total_files * 0.7)
valid_size = int(total_files * 0.15)
test_size = total_files - train_size - valid_size  # 남은 파일은 테스트 세트로

# 데이터셋 분할
train_files = file_list[:train_size]
valid_files = file_list[train_size:train_size + valid_size]
test_files = file_list[train_size + valid_size:]

# 각 분할별 파일 이름 리스트 출력
print("Train files:", train_files)
print("Validation files:", valid_files)
print("Test files:", test_files)

# 저장할 디렉토리 경로 설정
train_dir = 'train'
valid_dir = 'val'
test_dir = 'test'

# 디렉토리가 없으면 생성
os.makedirs(train_dir, exist_ok=True)
os.makedirs(valid_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# 파일 이동
for file_name in train_files:
    src = os.path.join(folder_path, file_name)
    dst = os.path.join(train_dir, file_name)
    shutil.move(src, dst)

for file_name in valid_files:
    src = os.path.join(folder_path, file_name)
    dst = os.path.join(valid_dir, file_name)
    shutil.move(src, dst)

for file_name in test_files:
    src = os.path.join(folder_path, file_name)
    dst = os.path.join(test_dir, file_name)
    shutil.move(src, dst)
