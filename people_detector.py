import cv2
test_path = r'D:\CODING\OPENCV\test_people.mp4'
cap = cv2.VideoCapture(test_path)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codecc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(filename='output_people.mp4',fourcc=codecc,fps=30,frameSize=(frame_width,frame_height))
full_cody = cv2.CascadeClassifier(r'D:\CODING\OPENCV\haarcascade_fullbody.xml')
while True:
    ret , frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frames = full_cody.detectMultiScale(gray,1.1,5)
    total_frames = len(frames)
    for (x,y,w,h) in frames:
        cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=3)
    cv2.putText(frame,f"total no of persons: {total_frames}",org =(20,40),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1.0,color=(0,0,255),thickness=2)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('r'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()


