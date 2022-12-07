import tkinter
import tkinter.messagebox
import customtkinter
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from find_motion import find_motion
from identify import maincall
import os
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")
quit_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "exit.png")),size=(30,30))
in_out_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "incognito.png")),size=(30,30))
monitor_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "lamp.png")),size=(30,30))
main_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "main.png")),size=(30,30))
recording_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "rec.png")),size=(30,30))
identify_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "identify.png")),size=(30,30))
rectangle_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "rectangle-of-cutted-line-geometrical-shape.png")),size=(30,30))
noise_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "security-camera.png")),size=(30,30))
logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "spy.png")),size=(100,100))

app = customtkinter.CTk()
app.geometry("690x340")
app.title("Smart CCTV")

def button_callback():
    print("Button click")





frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(fill = "both", expand = True)
frame_1.grid(pady=20, padx=40)
frame_1.grid_rowconfigure(4, weight=1)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Smart CCTV", image=logo_image, compound="left", font=customtkinter.CTkFont(size=30, weight="bold"))
label_1.grid(row =0, column=1, pady=10, padx=10)

btn_monitor = customtkinter.CTkButton(master=frame_1, text="Monitor", image=monitor_image, command=find_motion)
btn_monitor.grid(row=1,column = 0, pady=10, padx=10)

btn_identify = customtkinter.CTkButton(master=frame_1, text="Identify", image=identify_image, command=maincall)
btn_identify.grid(row=1,column = 1, pady=10, padx=10)

btn_rectangle = customtkinter.CTkButton(master=frame_1, text="Rectangle", image=rectangle_image, command=rect_noise)
btn_rectangle.grid(row=1,column = 2, pady=10, padx=10)

btn_noise = customtkinter.CTkButton(master=frame_1, text="Noise", image=noise_image, command=noise)
btn_noise.grid(row=2,column = 0, pady=10, padx=10)

btn_in_out = customtkinter.CTkButton(master=frame_1, text="In Out", image=in_out_image, command=in_out)
btn_in_out.grid(row=2,column = 1, pady=10, padx=10)

btn_record = customtkinter.CTkButton(master=frame_1, text="Record", image=recording_image, command=record)
btn_record.grid(row=2,column = 2,pady=10, padx=10)

btn_quit = customtkinter.CTkButton(master=frame_1, text="Quit", image=quit_image, command=app.quit)
btn_quit.grid(row=3,column = 1, pady=10, padx=10)

app.mainloop()