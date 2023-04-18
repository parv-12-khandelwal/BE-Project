import tkinter
import tkinter.messagebox
import customtkinter as ctk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from find_motion import find_motion
from identify import maincall_2 as maincall
from violence_detection import detect_violence
from count_people import cont
#import count_people
import os
from PIL import Image

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")
quit_image = ctk.CTkImage(Image.open(os.path.join(image_path, "exit.png")),size=(30,30))
in_out_image = ctk.CTkImage(Image.open(os.path.join(image_path, "incognito.png")),size=(30,30))
monitor_image = ctk.CTkImage(Image.open(os.path.join(image_path, "lamp.png")),size=(30,30))
main_image = ctk.CTkImage(Image.open(os.path.join(image_path, "main.png")),size=(30,30))
recording_image = ctk.CTkImage(Image.open(os.path.join(image_path, "rec.png")),size=(30,30))
identify_image = ctk.CTkImage(Image.open(os.path.join(image_path, "identify.png")),size=(30,30))
rectangle_image = ctk.CTkImage(Image.open(os.path.join(image_path, "rectangle-of-cutted-line-geometrical-shape.png")),size=(30,30))
noise_image = ctk.CTkImage(Image.open(os.path.join(image_path, "security-camera.png")),size=(30,30))
violence_image = ctk.CTkImage(Image.open(os.path.join(image_path, "violence.png")), size=(30,30))
logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "spy.png")),size=(100,100))
count_image = ctk.CTkImage(Image.open(os.path.join(image_path, "count_people.png")), size=(30,30))

app = ctk.CTk()
app.geometry("690x340")
app.title("Smart CCTV")


frame_1 = ctk.CTkFrame(master=app)
frame_1.pack(fill = "both", expand = True)
frame_1.grid(pady=20, padx=30)
frame_1.grid_rowconfigure(4, weight=1)

label_1 = ctk.CTkLabel(master=frame_1, text="Smart CCTV", image=logo_image, compound="left", font=ctk.CTkFont(size=30, weight="bold"))
label_1.grid(row =0, column=1, pady=10, padx=10)

btn_monitor = ctk.CTkButton(master=frame_1, text="Monitor", image=monitor_image, command=find_motion)
btn_monitor.grid(row=1,column = 0, pady=10, padx=10)

btn_identify = ctk.CTkButton(master=frame_1, text="Identify", image=identify_image, command=maincall)
btn_identify.grid(row=1,column = 1, pady=10, padx=10)

btn_rectangle = ctk.CTkButton(master=frame_1, text="Rectangle", image=rectangle_image, command=rect_noise)
btn_rectangle.grid(row=1,column = 2, pady=10, padx=10)

btn_noise = ctk.CTkButton(master=frame_1, text="Noise", image=noise_image, command=noise)
btn_noise.grid(row=2,column = 0, pady=10, padx=10)

btn_in_out = ctk.CTkButton(master=frame_1, text="In Out", image=in_out_image, command=in_out)
btn_in_out.grid(row=2,column = 1, pady=10, padx=10)

btn_record = ctk.CTkButton(master=frame_1, text="Record", image=recording_image, command=record)
btn_record.grid(row=2,column = 2,pady=10, padx=10)

btn_violence = ctk.CTkButton(master=frame_1, text="Violence Detection", image=violence_image, command=detect_violence)
btn_violence.grid(row=3,column = 0,pady=10, padx=10)

btn_violence = ctk.CTkButton(master=frame_1, text="Count People", image=count_image, command=cont)
btn_violence.grid(row=3,column = 1,pady=10, padx=10)

btn_quit = ctk.CTkButton(master=frame_1, text="Quit", image=quit_image, command=app.quit)
btn_quit.grid(row=3,column =2, pady=10, padx=10)

app.mainloop()