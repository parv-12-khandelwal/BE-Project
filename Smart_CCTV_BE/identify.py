import cv2
import os
import numpy as np
import tkinter as tk
import tkinter.font as font
import customtkinter as ctk

def collect_data(name, ids):
	count = 1
	
	cap = cv2.VideoCapture(0)

	filename = "haarcascade_frontalface_alt.xml"

	cascade = cv2.CascadeClassifier(filename)

	while True:
		_, frm = cap.read()

		gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)

		faces = cascade.detectMultiScale(gray, 1.4, 1)

		for x,y,w,h in faces:
			cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 2)
			roi = gray[y:y+h, x:x+w]

			cv2.imwrite(f"persons/{name}-{count}-{ids}.jpg", roi)
			count = count + 1
			cv2.putText(frm, f"{count}", (20,20), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 3)
			cv2.imshow("new", roi)


		cv2.imshow("identify", frm)

		if cv2.waitKey(1) == 27 or count > 300:
			cv2.destroyAllWindows()
			cap.release()
			train()
			break

def train():
	print("training part initiated !")

	recog = cv2.face.LBPHFaceRecognizer_create()

	dataset = 'persons'

	paths = [os.path.join(dataset, im) for im in os.listdir(dataset)]

	faces = []
	ids = []
	labels = []
	for path in paths:
		labels.append(path.split('/')[-1].split('-')[0])

		ids.append(int(path.split('/')[-1].split('-')[2].split('.')[0]))

		faces.append(cv2.imread(path, 0))

	recog.train(faces, np.array(ids))

	recog.save('model.yml')

	print('training part completed !')

	return

def identify():
	cap = cv2.VideoCapture(0)

	filename = "haarcascade_frontalface_default.xml"

	paths = [os.path.join("persons", im) for im in os.listdir("persons")]
	labelslist = {}
	for path in paths:
		labelslist[path.split('/')[-1].split('-')[2].split('.')[0]] = path.split('/')[-1].split('-')[0]

	print(labelslist)
	recog = cv2.face.LBPHFaceRecognizer_create()

	recog.read('model.yml')

	cascade = cv2.CascadeClassifier(filename)

	while True:
		_, frm = cap.read()

		gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)

		faces = cascade.detectMultiScale(gray, 1.3, 2)

		for x,y,w,h in faces:
			cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 2)
			roi = gray[y:y+h, x:x+w]

			label = recog.predict(roi)

			if label[1] < 100:
				cv2.putText(frm, f"{labelslist[str(label[0])]} + {int(label[1])}", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
			else:
				cv2.putText(frm, "unkown", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

		cv2.imshow("identify", frm)

		if cv2.waitKey(1) == 27:
			cv2.destroyAllWindows()
			cap.release()
			break

def maincall():


	root = tk.Tk()

	root.geometry("480x100")
	root.title("identify")

	label = tk.Label(root, text="Select below buttons ")
	label.grid(row=0, columnspan=2)
	label_font = font.Font(size=35, weight='bold',family='Helvetica')
	label['font'] = label_font

	btn_font = font.Font(size=25)

	button1 = tk.Button(root, text="Add Member ", command=collect_data, height=2, width=20)
	button1.grid(row=1, column=0, pady=(10,10), padx=(5,5))
	button1['font'] = btn_font

	button2 = tk.Button(root, text="Start with known ", command=identify, height=2, width=20)
	button2.grid(row=1, column=1,pady=(10,10), padx=(5,5))
	button2['font'] = btn_font
	root.mainloop()

	return

def maincall_2():

	global databox
	databox = False

	def showDatabox():
		def submit_member():
			name = inp_name.get()
			ids = inp_id.get()
			add_member_label.destroy()
			inp_name.destroy()
			inp_id.destroy()
			button_sub.destroy()
			root.wm_geometry("360x120")
			collect_data(name,ids)
			
		root.wm_geometry("360x260")
		add_member_label = ctk.CTkLabel(master=frame_1,text= "Add Member")
		inp_name = ctk.CTkEntry(master=frame_1, placeholder_text="Name")
		inp_id = ctk.CTkEntry(master=frame_1,  placeholder_text="ID")
		button_sub = ctk.CTkButton(master=frame_1, text="Submit", command=submit_member)
		add_member_label.grid(row=4)
		inp_name.grid(row = 4, columnspan=2, pady=10, padx= 10, sticky='nesw')
		inp_id.grid(row = 5, columnspan=2, pady=10, padx= 10, sticky='nesw')
		button_sub.grid(row = 6, pady=10, padx= 10)


	ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
	ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
	
	root = ctk.CTk()
	root.geometry("360x120")
	root.title("Identify")

	frame_1 = ctk.CTkFrame(master=root)
	frame_1.pack(fill = "both", expand = True)
	frame_1.grid(pady=20, padx=20)

	label = ctk.CTkLabel(master=frame_1, text="Select below buttons ")
	label.grid(row=0, columnspan=2)
	label_font = font.Font(size=35, weight='bold',family='Helvetica')
	label['font'] = label_font

	btn_font = font.Font(size=25)

	button1 = ctk.CTkButton(master=frame_1, text="Add Member ", command=showDatabox)
	button1.grid(row=1, column=0, pady=(10,10), padx=(10,10))
	button1['font'] = btn_font

	button2 = ctk.CTkButton(master=frame_1, text="Start with known ", command=identify)
	button2.grid(row=1, column=1,pady=(10,10), padx=(10,10))
	button2['font'] = btn_font
	root.mainloop()
