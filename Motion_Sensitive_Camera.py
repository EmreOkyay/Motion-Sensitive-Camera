                                            ## MOTION SENSITIVE CAMERA ##
import cv2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import numpy as np
import sys
from PyQt5 import QtCore, uic
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import GUI
import Email_GUI
from functools import partial

email_user = ''
email_password = ''
email_reciever = ''

class Camera(QtWidgets.QMainWindow):
    def __init__(self):
        m = 0
        super(Camera, self).__init__()
        Load_GUI = loadUi('GUI.ui', self)
        capture = cv2.VideoCapture(0)
        self.show()

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.MP4', fourcc, 20, (640, 480), True)

        # History, Threshold, DetectShadows
        # History: Every 300 frames, the pixels on the screen become the new background
        fgbg = cv2.createBackgroundSubtractorMOG2(300, 200, True)

        # Keeps track of what frame we're on
        frameCount = 0

        while (1):

            # Return Value and the current frame
            ret, frame = capture.read()

            self.lcdNumber.display(m)  # Updates the value of lcd
            GUI.Ui_MainWindow.Motion_False(self)

            #  Check if a current frame actually exist
            if not ret:
                break
            self.GUI_Video(frame)
            frameCount += 1
            # Resize the frame since the video (demo.mov) is too big
            resizedFrame = cv2.resize(frame, (0, 0), fx=0.50,fy=0.50)  # source, desired size for the image, fx, fy 1/2 times the x and y

            # Get the foreground mask
            fgmask = fgbg.apply(resizedFrame)

            # Counts all the non zero pixels within the mask (0 = black, 1 = white)
            count = np.count_nonzero(fgmask)

            print('Frame: %d, Pixel Count: %d' % (frameCount, count))

            # Determine how many pixels do you want to detect to be considered "movement"
            if (frameCount > 1 and count > 800):  # Lower the count is higher the sensitivity is
                m += 1
                GUI.Ui_MainWindow.Motion_True(self)  # If motion is detected, sets the label2 text as "Motion Detected"
                out.write(frame)
                if m == 60:
                    img = frame
                    cv2.imwrite("img.jpg", img)
                    self.sentMail()
                    m = 0

            cv2.imshow('Mask', fgmask)

            Load_GUI.pushButton.clicked.connect(GUI.Ui_MainWindow.on_Click)

            if GUI.A == 0: # If button is clicked, make A = 0, therefore execute close function
                Load_GUI.pushButton.clicked.connect(Camera.Close(self, capture, out))


            if cv2.waitKey(33) == 27: # 27 for esc key
                capture.release()
                out.release()
                cv2.destroyAllWindows()
                break
        sys.exit(0)

    def Close(self, capture, out):
        capture.release()
        out.release()
        cv2.destroyAllWindows()
        sys.exit(0)


    def GUI_Video(self, img):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:  # (width, height, channels)
            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.label.setPixmap(QPixmap.fromImage(img))
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def Email(self):
        global email_user, email_password, email_reciever
        email_user = self.lineEdit.text()
        email_password = self.lineEdit_2.text()
        email_reciever = self.lineEdit_3.text()


    def Exit(load, self):
        global email_user, email_password, email_reciever
        # Pop ups in case of empty email sections
        if email_user == '' and email_password != '' and email_reciever != '':
            Email_GUI.Ui_MainWindow.pop_up_1(self)
        elif email_password == '' and email_user != '' and email_reciever != '':
            Email_GUI.Ui_MainWindow.pop_up_2(self)
        elif email_reciever == '' and email_user != '' and email_password != '':
            Email_GUI.Ui_MainWindow.pop_up_3(self)
        elif email_user == '' and email_password == '' and email_reciever != '':
            Email_GUI.Ui_MainWindow.pop_up_4(self)
        elif email_user == '' and email_reciever == '' and email_password != '':
            Email_GUI.Ui_MainWindow.pop_up_5(self)
        elif email_password == '' and email_reciever == '' and email_user != '':
            Email_GUI.Ui_MainWindow.pop_up_6(self)
        elif email_user == '' and email_password == '' and email_reciever == '':
            Email_GUI.Ui_MainWindow.pop_up_7(self)
        elif email_user != '' and email_password != '' and email_reciever != '':
            load.close()


    appi = QtWidgets.QApplication(sys.argv)
    load = uic.loadUi("Email_GUI.ui")
    load.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password) # Hides the password
    load.pushButton.clicked.connect(partial(Email, load))
    load.pushButton_2.clicked.connect(partial(Exit, load))
    load.show()
    appi.exec_()

    def sentMail(self):

        subject = 'Python Test'

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_reciever
        msg['Subject'] = subject

        body = '''        MOTION DETECTED! MOTION DETECTED!
        MOTION DETECTED! MOTION DETECTED!
        MOTION DETECTED! MOTION DETECTED!'''
        msg.attach(MIMEText(body, 'plain'))

        filename = 'img.jpg'
        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)

        server.sendmail(email_user, email_reciever, text)
        server.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Camera()
    app.exec_()

