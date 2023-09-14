
import cv2
import face_recognition
import os
import numpy as np

images = [] # Danh sách hình ảnh khuôn mặt
labels = [] # Danh sách các nhãn tương ứng

# Load ảnh từ kho dataset
path="dataset"
myList = os.listdir(path)
print(myList)

# Lọc tên file lấy nhãn
for i in myList:
    print(i)
    curImg = cv2.imread(f"{path}/{i}")
    images.append(curImg)
    labels.append(os.path.splitext(i)[0])
print(len(images))
print(labels)
# Mã hóa hình ảnh
def encode(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
encodedList = encode(images)

# So sánh mặt
def recognize_face(encodedList, encodeFace):
    name = "Unknown"
    faceDis = face_recognition.face_distance(encodedList, encodeFace)
    print(faceDis)
    matched = np.argmin(faceDis)
    if faceDis[matched] < 0.5: # giá trị tăng giảm tùy thuộc
        name = labels[matched]
    
    return name


# Khởi tạo camera
camera = cv2.VideoCapture(0)  # 0 là thiết bị mặc định (camera webcam)

while True:
    temp, frame = camera.read()
    frame = cv2.flip(frame, 1)
    fr = cv2.resize(frame,(0,0),None,fx=0.5,fy=0.5)
    fr = cv2.cvtColor(fr,cv2.COLOR_BGR2RGB)
    
    facecurrentFrame = face_recognition.face_locations(fr)
    encodecurrentFrame = face_recognition.face_encodings(fr)
    
    for encodeFace, faceLoc in zip(encodecurrentFrame, facecurrentFrame):
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1 * 2, x2 * 2, y2 * 2, x1 * 2
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 2)
        
        if encodecurrentFrame:  # Kiểm tra nếu có khuôn mặt được mã hóa
           
            cv2.putText(frame, recognize_face(encodedList,encodeFace), (x2, y2), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    cv2.imshow("Face Reg", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Giải phóng tài nguyên
camera.release()
cv2.destroyAllWindows()
