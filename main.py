from tkinter import *


def main_window():
    main = Tk()
    main.geometry("300x400")
    main.title("BMI Calculator")
    main.config(bg="white")
    return main

def create_frames(main):
    Label(main, text="BMI Calculator", font=("Arial", 16)).grid(row=0, column=0, pady=10)

    frame_1 = Frame(main, bg="white")
    frame_1.grid(row=1, column=0, padx=10, pady=10)

    frame_2 = Frame(main, bg="white")
    frame_2.grid(row=2, column=0, padx=10, pady=10)

    frame_bottom = Frame(main, bg="white")
    frame_bottom.grid(row=3, column=0, padx=10, pady=20)

    return frame_1, frame_2, frame_bottom

def create_widgets(frame_1, frame_2, frame_bottom):
    Label(frame_1, text="Height (cm):").grid(row=0, column=0, padx=5, pady=5)
    ent_height = Entry(frame_1, textvariable=height_var)
    ent_height.grid(row=1, column=0, ipadx=30, padx=10)

    Label(frame_2, text="Weight (kg):").grid(row=0, column=0, padx=5, pady=5)
    ent_weight = Entry(frame_2, textvariable=weight_var)
    ent_weight.grid(row=1, column=0, ipadx=30, padx=10)

    Button(frame_bottom, text="Calculate", command=find_bmi).grid(row=2, column=0, pady=10)

    global result_label
    result_label = Label(frame_bottom, text="", bg="white", font=("Arial", 12))
    result_label.grid(row=3, column=0, pady=10)


def find_bmi():
    height = float(height_var.get()) / 100
    weight = float(weight_var.get())
    bmi = weight / (height ** 2)
    result_label.config(text=f"BMI = {bmi:.2f}")

main = main_window()
height_var = StringVar()
weight_var = StringVar()
frame_1, frame_2, frame_bottom = create_frames(main)
create_widgets(frame_1, frame_2, frame_bottom)

main.mainloop()
