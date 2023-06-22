import os
import shutil
import time
from datetime import datetime

# Đường dẫn thư mục cần backup
source_directory = "C:/Users/name/folder"

# Đường dẫn địa chỉ lưu
destination_directory = "C:/Users/name/backup"
max_backup_files = 7   # Số lượng file backup nhiều nhất

def backup_data():
    # Tạo tên thư mục sao lưu dựa trên ngày và giờ hiện tại
    now = datetime.now().strftime("%Hh%Mm %d-%b-%Y")
    backup_directory = os.path.join(destination_directory, f"backup_{now}")
    
    # Sao chép toàn bộ dữ liệu từ thư mục nguồn sang thư mục sao lưu
    shutil.copytree(source_directory, backup_directory)
    
    print(f"Đã sao lưu dữ liệu vào: {backup_directory}")

# Kiểm tra nếu thư mục sao lưu không tồn tại thì tạo mới và sao lưu dữ liệu đầu tiên
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)
    backup_data()

# Lưu danh sách các thư mục sao lưu hiện có
backup_directories = sorted(os.listdir(destination_directory), reverse=True)


# Lặp vô hạn để thực hiện sao lưu dữ liệu vào 0h hàng ngày
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    if current_time == "00:00:00" or current_time == "00:00:00":
        if len(backup_directories) >= max_backup_files:
            for directory in backup_directories[max_backup_files:]:
                shutil.rmtree(os.path.join(destination_directory, directory))
                print(f"Đã xóa thư mục: {directory}")
        
        backup_data()
        
        backup_directories = sorted(os.listdir(destination_directory), reverse=True)
        print(f"Đã sao lưu dữ liệu vào: {backup_directories}")
    
    time.sleep(1)
