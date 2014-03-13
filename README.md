Các scripts trong Ubuntu hữu ích  
=======

#1 Hướng dẫn thay đổi repos cho Ubuntu Server 12.04

- Bước 1: Sử dụng wget tải file sau về
         wget https://raw.github.com/tothanhcong/scripts/master/Source/tai-source-list.sh
- Bước 2: chạy lệnh chmod để phân quyền cho file tai-source-list.sh
         chmod -R 777 tai-source-list.sh
- Bước 3: Thực thi file "tai-source-list.sh"
         ./tai-source-list.sh
- Bước 4: Thực hiện lệnh apt-get update để cập nhật lại repos và sử dụng cài các gói bình thường
         apt-get update


