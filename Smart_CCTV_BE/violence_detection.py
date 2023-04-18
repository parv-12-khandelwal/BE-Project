from keras.models import load_model
from collections import deque
import matplotlib.pyplot as plt
import numpy as np
import cv2
import datetime

#WORKING PROJECT
import numpy as np
import argparse
import pickle
import cv2
import os
from keras.models import load_model
from collections import deque

import smtplib, os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart



def detect_violence(limit=None):
        #fig=plt.figure(figsize=(16, 30))
        if not os.path.exists('output'):
            os.mkdir('output')

        print("Loading model ...")
        model = load_model('ViolenceDetectionModels/modelnew.h5', compile=False)
        Q = deque(maxlen=128)
        vs = cv2.VideoCapture(0)
        writer = None
        (W, H) = (None, None)
        count = 0     
        while True:
            # read the next frame from the file
            (grabbed, frame) = vs.read()

            # if the frame was not grabbed, then we have reached the end
            # of the stream
            if not grabbed:
                break
            
            # if the frame dimensions are empty, grab them
            if W is None or H is None:
                (H, W) = frame.shape[:2]

            # clone the output frame, then convert it from BGR to RGB
            # ordering, resize the frame to a fixed 128x128, and then
            # perform mean subtraction

            
            output = frame.copy()
           
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (128, 128)).astype("float32")
            frame = frame.reshape(128, 128, 3) / 255

            # make predictions on the frame and then update the predictions
            # queue
            preds = model.predict(np.expand_dims(frame, axis=0))[0]
#             print("preds",preds)
            Q.append(preds)

            # perform prediction averaging over the current history of
            # previous predictions
            results = np.array(Q).mean(axis=0)
            i = (preds > 0.50)[0]
            label = i

            text_color = (0, 255, 0) # default : green

            if label: # Violence prob
                text_color = (0, 0, 255) # red
                send_mail()

            else:
                text_color = (0, 255, 0)

            text = "Violence: {}".format(label)
            FONT = cv2.FONT_HERSHEY_SIMPLEX 

            cv2.putText(output, text, (35, 50), FONT,1.25, text_color, 3) 

            # check if the video writer is None
            if writer is None:
                # initialize our video writer
                fourcc = cv2.VideoWriter_fourcc(*"MJPG")
                writer = cv2.VideoWriter(f"violence_results/v_nv_res_{datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S')}.avi", fourcc, 30,(W, H), True)

            # write the output frame to disk
            writer.write(output)

            # show the output image
            cv2.imshow("Output",output)
            key = cv2.waitKey(1) & 0xFF

            # if the `q` key was pressed, break from the loop
            if key == 27:
                break
        # release the file pointersq
        print("[INFO] cleaning up...")
        writer.release()
        vs.release()
        cv2.destroyAllWindows()

        
def send_mail():
	fromaddr = "smcctv1234@gmail.com"
	toaddr = "s4samyak@gmail.com"
	password = 'bhuspjpqnvnnxhdh'

	msg = MIMEMultipart()
	msg['Subject'] = 'Violence Detected'
	msg['From'] = fromaddr
	msg['To'] = toaddr
	text = MIMEText("Alert!! Violence is detected")
	msg.attach(text)
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(fromaddr, password)
	s.sendmail(fromaddr, toaddr, msg.as_string())
	print("Mail sent successfully.")
	s.quit()