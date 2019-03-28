from tkinter import *
from PIL import Image, ImageDraw,ImageTk
import face_recognition
import cv2

# Load the jpg file into a numpy array
ca=cv2.VideoCapture(0)


def ai():
        ret, img = ca.read()
        img=cv2.flip(img,1)
        cv2.imwrite('./data/233.jpg', img)

        image = face_recognition.load_image_file("./data/233.jpg")
        # Find all facial features in all the faces in the image
        face_landmarks_list = face_recognition.face_landmarks(image)

        print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

        # Create a PIL imagedraw object so we can draw on the picture
        pil_image = Image.fromarray(image)
        d = ImageDraw.Draw(pil_image)

        for face_landmarks in face_landmarks_list:
            for facial_feature in face_landmarks.keys():
                d.line(face_landmarks[facial_feature], width=5)
        cv2.waitKey(1)
        imgtk = ImageTk.PhotoImage(image=pil_image)
        panel.imgtk = imgtk
        panel.config(image=imgtk)
        root.after(1, ai)
def take_snapshot():

    print(233)
    cv2.imwrite('./data/2.jpg',img)
root = Tk()
root.title("opencv + tkinter")
#root.protocol('WM_DELETE_WINDOW', detector)

panel = Label(root)  # initialize image panel
panel.pack(padx=10, pady=10)
root.config(cursor="arrow")
btn = Button(root, text="点赞!", command=take_snapshot)
btn.pack(fill="both", expand=True, padx=10, pady=10)

ai()
root.mainloop()
# 当一切都完成后，关闭摄像头并释放所占资源
ca.release()
cv2.destroyAllWindows()