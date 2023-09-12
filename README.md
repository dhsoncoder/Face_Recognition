# Face_Recognition
A basic program that uses OpenCV to detect and recognize human faces

Ý tưởng:
- Nhận diện gương mặt thông qua 2 giai đoạn
- Giai đoạn 1: Phát hiện khuôn mặt. Tức là phải sử dụng một thuật toán để nhận dạng ra khuôn mặt đang nằm ở vị trí nào trên màn hình, từ đó khoanh vùng để bước tới khâu tiếp theo là nhận diện gương mặt.
Em lựa chọn thuật toán Viola-Jones, chính xác hơn thì là một biến thể của nó, đó là Haar Cascade vì nó dễ sử dụng và có sẵn các hàm hỗ trợ trong OpenCV.
- Giai đoạn 2: Nhận dạng gương mặt. Nguyên lý hoạt động của việc nhận dạng gương mặt trong chương trình này là mã hóa hình ảnh và biểu diễn nó dưới dạng vector số học, sau đó so sánh với danh sách vector các gương mặt đã được mã hóa từ trước(gọi là dataset). Nếu như kết quả trả về nằm trong phạm vi sai số cho phép thì tên của người nhận dạng sẽ được hiện lên và ngược lại sẽ thông báo không nhận dạng được.

Thuận lợi:
- OpenCV có sẵn các thư viện và gói hỗ trợ trong việc nhận dạng khuôn mặt
- Nguồn tài liệu lớn trên Internet

Khó khăn:
- Các module như dlib, face_recognition khá khó để cài đặt do không tương thích với một số phiên bản python
- Dữ liệu đầu vào không đủ nhiều
- Biểu cảm khuôn mặt thay đổi
- Điều kiện môi trường, chất lượng ánh sáng, chất lượng camera
- Sự xuất hiện hoặc thiếu thành phần khuôn mặt như kính, mũ, râu,...
- Cấu hình máy không đáp ứng đủ để chạy tốt chương trình
