from tkinter import *

if __name__ == '__main__':


    root = Tk()
    root.title("Калькулятор пластиковых окон")
    root.geometry("1100x500")

    window1_i = PhotoImage(file="window_open_tilt_1_r.gif")
    window2_i = PhotoImage(file="window_open_tilt_2_r.gif")
    window3_i = PhotoImage(file="window_open_tilt_3_r.gif")
    window4_i = PhotoImage(file="window_open_tilt_4_r.gif")
    deaf_window_i = PhotoImage(file="window_deaf_r.gif")
    window2_d_i = PhotoImage(file="window_d_tilt_2_r.gif")
    window3_d_i = PhotoImage(file="window_d_tilt_3_r.gif")

    choose_frame = Frame(root)
    choose_frame.pack(anchor="nw", side="top")

    choose_window_lb = Label(choose_frame, text="Шаг 1. Выберите какое у вас окно:")
    choose_window_lb.pack(anchor="nw", )

    deaf_window_btn = Button(choose_frame, image=deaf_window_i)
    deaf_window_btn.pack(anchor="nw", side="left")

    window1_btn = Button(choose_frame, image=window1_i)
    window1_btn.pack(anchor="nw", side="left")

    window2_btn = Button(choose_frame, image=window2_i)
    window2_btn.pack(anchor="nw", side="left")

    window3_btn = Button(choose_frame, image=window3_i)
    window3_btn.pack(anchor="nw", side="left")

    window4_btn = Button(choose_frame, image=window4_i)
    window4_btn.pack(anchor="nw", side="left")

    window2_d_btn = Button(choose_frame, image=window2_d_i)
    window2_d_btn.pack(anchor="nw", side="left")

    window3_d_btn = Button(choose_frame, image=window3_d_i)
    window3_d_btn.pack(anchor="nw")

    Label(root).pack()

    input_frame = Frame(root)
    input_frame.pack(anchor="nw", padx=10, pady=10)

    choose_window_lb2 = Label(input_frame, text="Шаг 2. Введите параметры вашего окна:")
    choose_window_lb2.grid(row=0, column=0, columnspan=2, sticky="w")

    width_window_lb = Label(input_frame, text="Ширина окна:")
    width_window_lb.grid(row=1, column=0, sticky="w")

    width_window_tb = Text(input_frame, width=10, height=1, wrap='word')
    width_window_tb.grid(row=1, column=1, sticky="w")

    m_lb = Label(input_frame, text="мм")
    m_lb.grid(row=1, column=2, sticky="w")

    height_window_lb = Label(input_frame, text="Высота окна:")
    height_window_lb.grid(row=2, column=0, sticky="w")

    height_window_tb = Text(input_frame, width=10, height=1, wrap='word')
    height_window_tb.grid(row=2, column=1, sticky="w")

    mm_lb = Label(input_frame, text="мм")
    mm_lb.grid(row=2, column=2, sticky="w")

    width_door_lb = Label(input_frame, text="Ширина двери:")
    width_door_lb.grid(row=3, column=0, sticky="w")

    width_door_tb = Text(input_frame, width=10, height=1, wrap='word')
    width_door_tb.grid(row=3, column=1, sticky="w")

    m_lb = Label(input_frame, text="мм")
    m_lb.grid(row=3, column=2, sticky="w")

    height_door_lb = Label(input_frame, text="Высота двери:")
    height_door_lb.grid(row=4, column=0, sticky="w")

    height_door_tb = Text(input_frame, width=10, height=1, wrap='word')
    height_door_tb.grid(row=4, column=1, sticky="w")

    mm_lb = Label(input_frame, text="мм")
    mm_lb.grid(row=4, column=2, sticky="w")

    root.mainloop()