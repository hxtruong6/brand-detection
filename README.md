# Nhận diện thương hiệu nước uống tại Việt Nam
## 1. Giới thiệu
Chương trình gồm 2 chức năng chính, trên 5 loại thương hiệu nước uống tại Việt Nam (Aquafina, Coca cola, Vĩnh Hảo, Dasani và Lavie):   
- upload ảnh và detect logo của các thương hiệu nước uống.
- upload video và kiểm tra tần suất xuất hiện và độ bao phủ trung bình trên frame ảnh của loại nhãn hàng (thời gian thực thi tương đối chậm nếu video quá dài vì không có hỗ trợ GPU).

Video demo của từng chức năng:https://www.youtube.com/watch?v=4fUWmV3Ccmg&feature=youtu.be
## 2. Hướng dẫn thực thi chương trình
Thực hiện lần lượt các bước sau:
### B1: Download mã nguồn chương trình
```
git clone https://github.com/hxtruong/brand-detection.git
```
```
ROOT = {đường dẫn đến repo đã clone về}
```

### B2: Khởi động server
Download file weight cho mô hình yolo và đặt ở trong thư mục ROOT/server: https://drive.google.com/open?id=1ctJCv7yHS-MxhtDTRJ3twJv5zA-ymQtk   
#### Cài đặt các thư viện cần thiết
- Tạo và khởi động môi trường ảo
```
pip3 install virtualenv
virtualenv ~/venv
source ~/venv/bin/activate
```
- Cài đặt Flask
```
pip install Flask
```
- Cài đặt Open CV
```
pip install opencv-python
```
#### Khởi động server
```
cd ROOT/server
python app.py
```

### B3: Khởi động UI
Mở 1 terminal mới
#### Cài đặt yarn
```
sudo apt-get install npm
sudo npm install -g yarn
```

#### Khởi động UI
```
cd ROOT/web
yarn
yarn dev
```

### B4: Trải nghiệm chương trình
Mở trình duyệt web và nhập: localhost:3000


