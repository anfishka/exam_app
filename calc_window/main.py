from tkinter import *

if __name__ == '__main__':


    root = Tk()
    root.title("Калькулятор пластиковых окон")
    root.geometry("1150x700")

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
    choose_window_lb.pack(anchor="nw")

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

    # min_width_window = 500
    # max_width_window = 1600

    width_window_tb = Text(input_frame, width=10, height=1, wrap='word')
    width_window_tb.grid(row=1, column=1, sticky="w")

    m_lb = Label(input_frame, text="мм")
    m_lb.grid(row=1, column=2, sticky="w")

    height_window_lb = Label(input_frame, text="Высота окна:")
    height_window_lb.grid(row=2, column=0, sticky="w")

    # min_height_window = 500
    # max_height_window = 1800

    height_window_tb = Text(input_frame, width=10, height=1, wrap='word')
    height_window_tb.grid(row=2, column=1, sticky="w")

    mm_lb = Label(input_frame, text="мм")
    mm_lb.grid(row=2, column=2, sticky="w")

    width_door_lb = Label(input_frame, text="Ширина двери:")
    width_door_lb.grid(row=3, column=0, sticky="w")

    # min_width_door = 500
    # max_width_door = 1000

    width_door_tb = Text(input_frame, width=10, height=1, wrap='word')
    width_door_tb.grid(row=3, column=1, sticky="w")

    m_lb = Label(input_frame, text="мм")
    m_lb.grid(row=3, column=2, sticky="w")

    height_door_lb = Label(input_frame, text="Высота двери:")
    height_door_lb.grid(row=4, column=0, sticky="w")

    # min_height_door = 1350
    # max_height_door = 2350

    height_door_tb = Text(input_frame, width=10, height=1, wrap='word')
    height_door_tb.grid(row=4, column=1, sticky="w")

    mm_lb = Label(input_frame, text="мм")
    mm_lb.grid(row=4, column=2, sticky="w")


    def windowsill_click():
        if windowsill_cb_v.get() == 1:
            label.config(text="Чекбокс выбран")
        else:
            label.config(text="Чекбокс не выбран")


    def window_tide_click():
        if window_tide_cb_v.get() == 1:
            label.config(text="Чекбокс выбран")
        else:
            label.config(text="Чекбокс не выбран")


    def window_slopes_click():
        if window_slopes_cb_v.get() == 1:
            label.config(text="Чекбокс выбран")
        else:
            label.config(text="Чекбокс не выбран")


    def window_mosquito_net_click():
        if window_mosquito_net_cb_v.get() == 1:
            label.config(text="Чекбокс выбран")
        else:
            label.config(text="Чекбокс не выбран")


    def window_montage_demontage_click():
        if window_montage_demontage_cb_v.get() == 1:
            label.config(text="Чекбокс выбран")
        else:
            label.config(text="Чекбокс не выбран")


    windowsill_cb_v = IntVar()
    window_tide_cb_v = IntVar()
    window_slopes_cb_v = IntVar()
    window_mosquito_net_cb_v = IntVar()
    window_montage_demontage_cb_v = IntVar()

    Label(root).pack()

    options_frame = Frame(root)
    options_frame.pack(anchor="nw")

    height_door_lb = Label(options_frame, text="Шаг 3: Выберите дополнительные опции:")
    height_door_lb.grid(row=0, column=0, columnspan=6, sticky="w")

    windowsill_cb = Checkbutton(options_frame, text="Подоконник", variable=windowsill_cb_v, command=windowsill_click)
    windowsill_cb.grid(row=1, column=0, sticky="w")

    window_tide_cb = Checkbutton(options_frame, text="Отлив", variable=window_tide_cb_v, command=window_tide_click)
    window_tide_cb.grid(row=1, column=1, sticky="w")

    window_slopes_cb = Checkbutton(options_frame, text="Откосы", variable=window_slopes_cb_v,
                                   command=window_slopes_click)
    window_slopes_cb.grid(row=1, column=2, sticky="w")

    window_mosquito_net_cb = Checkbutton(options_frame, text="Москитная сетка", variable=window_mosquito_net_cb_v,
                                         command=window_mosquito_net_click)
    window_mosquito_net_cb.grid(row=1, column=3, sticky="w")

    window_montage_demontage_cb = Checkbutton(options_frame, text="Монтаж / Демонтаж",
                                              variable=window_montage_demontage_cb_v,
                                              command=window_montage_demontage_click)
    window_montage_demontage_cb.grid(row=1, column=4, sticky="w")

    label = Label(root, text="")
    label.pack()


    def show_selected_prof():
        show_window_profile = window_profile.get()
        label.config(text=f"Выбрано: {show_window_profile}")


    window_profile = StringVar()
    window_profile.set("Rehau")

    choose_prof_frame = Frame(root)
    choose_prof_frame.pack(anchor="nw")

    choose_prof = Label(choose_prof_frame, text="Шаг 4: Выберите тип профиля:")
    choose_prof.grid(row=0, column=0, columnspan=6, sticky="w")

    rehau_r_btn = Radiobutton(choose_prof_frame, text="Rehau", variable=window_profile, value="Rehau")
    rehau_r_btn.grid(row=1, column=0, sticky="w")

    salamander_r_btn = Radiobutton(choose_prof_frame, text="Salamander", variable=window_profile, value="Salamander")
    salamander_r_btn.grid(row=1, column=1, sticky="w")

    wds_r_btn = Radiobutton(choose_prof_frame, text="WDS", variable=window_profile, value="WDS")
    wds_r_btn.grid(row=1, column=2, sticky="w")

    show_window_profile = Button(text="Показать выбранное", command=show_selected_prof)
    show_window_profile.pack()

    lab = Label(root, text="Выбрано: ")
    lab.pack()


    def show_selected_glazing():
        show_window_glazing = glazing.get()
        label.config(text=f"Выбрано: {show_window_glazing}")


    glazing = StringVar()
    glazing.set("Однокамерный")

    glazing_frame = Frame(root)
    glazing_frame.pack(anchor="nw")

    glazing_lb = Label(glazing_frame, text="Шаг 5: Выберите стеклопакет")
    glazing_lb.grid(row=0, column=0, columnspan=6, sticky="w")

    glazing_r_btn = Radiobutton(glazing_frame, text="Однокамерный", variable=glazing, value="Однокамерный")
    glazing_r_btn.grid(row=1, column=0, sticky="w")

    double_glazing_r_btn = Radiobutton(glazing_frame, text="Двухкамерный", variable=glazing, value="Двухкамерный")
    double_glazing_r_btn.grid(row=1, column=1, sticky="w")

    energy_saving_btn = Radiobutton(glazing_frame, text="Энергосберегающий", variable=glazing,
                                    value="Энергосберегающий")
    energy_saving_btn.grid(row=1, column=2, sticky="w")

    sun_protection_r_btn = Radiobutton(glazing_frame, text="Солнцезащитный", variable=glazing, value="Солнцезащитный")
    sun_protection_r_btn.grid(row=1, column=3, sticky="w")

    show_window_glazing = Button(text="Показать выбранное", command=show_selected_glazing)
    show_window_glazing.pack()


    def show_window_system_rehau():
        show_window_system = window_system_rehau.get()
        label.config(text=f"Выбрано: {show_window_system}")


    window_system_rehau = StringVar()
    window_system_rehau.set("Ecosol-60")

    # FOR REHAU
    window_system_frame_rehau = Frame(root)
    window_system_frame_rehau.pack(anchor="nw")

    window_system_rehau_lb = Label(window_system_frame_rehau, text="Шаг 5: Выберите систему")
    window_system_rehau_lb.grid(row=0, column=0, columnspan=6, sticky="w")

    ecosol_60_rehau_r_btn = Radiobutton(window_system_frame_rehau, text="Ecosol-60", variable=window_system_rehau,
                                        value="Ecosol-60")
    ecosol_60_rehau_r_btn.grid(row=1, column=0, sticky="w")

    ecosol_70_rehau_r_btn = Radiobutton(window_system_frame_rehau, text="Ecosol-70", variable=window_system_rehau,
                                        value="Ecosol-70")
    ecosol_70_rehau_r_btn.grid(row=1, column=1, sticky="w")

    brilliant_design_rehau_r_btn = Radiobutton(window_system_frame_rehau, text="Brilliant Design",
                                               variable=window_system_rehau, value="Brilliant Design")
    brilliant_design_rehau_r_btn.grid(row=1, column=2, sticky="w")

    synego_rehau_r_btn = Radiobutton(window_system_frame_rehau, text="Synego", variable=window_system_rehau,
                                     value="Synego")
    synego_rehau_r_btn.grid(row=1, column=3, sticky="w")

    geneo_rehau_r_btn = Radiobutton(window_system_frame_rehau, text="Geneo", variable=window_system_rehau,
                                    value="Geneo")
    geneo_rehau_r_btn.grid(row=1, column=3, sticky="w")

    show_window_system_rehau_btn = Button(text="Показать выбранное", command=show_window_system_rehau)
    show_window_system_rehau_btn.pack()


    def show_window_system_salamander():
        show_window_system = window_system_salamander.get()
        label.config(text=f"Выбрано: {show_window_system}")


    window_system_salamander = StringVar()
    window_system_salamander.set("Bluevolution 82")

    # FOR SALAMANDER
    window_system_frame_salamander = Frame(root)
    window_system_frame_salamander.pack(anchor="nw")

    window_system_salamander_lb = Label(window_system_frame_salamander, text="Шаг 5: Выберите систему")
    window_system_salamander_lb.grid(row=0, column=0, columnspan=6, sticky="w")

    ecosol_60_salamander_r_btn = Radiobutton(window_system_frame_salamander, text="Bluevolution 82",
                                             variable=window_system_salamander, value="Bluevolution 82")
    ecosol_60_salamander_r_btn.grid(row=1, column=0, sticky="w")

    ecosol_70_salamander_r_btn = Radiobutton(window_system_frame_salamander, text="Steamline",
                                             variable=window_system_salamander, value="Steamline")
    ecosol_70_salamander_r_btn.grid(row=1, column=1, sticky="w")

    brilliant_design_salamander_r_btn = Radiobutton(window_system_frame_salamander, text="BluEvolution 92",
                                                    variable=window_system_salamander, value="BluEvolution 92")
    brilliant_design_salamander_r_btn.grid(row=1, column=2, sticky="w")

    show_window_system_salamander_btn = Button(text="Показать выбранное", command=show_window_system_salamander)
    show_window_system_salamander_btn.pack()


    def show_window_system_wds():
        show_window_system_wds = window_system_wds.get()
        label.config(text=f"Выбрано: {show_window_system_wds}")


    window_system_wds = StringVar()
    window_system_wds.set("5 Siries")

    # FOR WDS
    window_system_frame_wds = Frame(root)
    window_system_frame_wds.pack(anchor="nw")

    window_system_wds_lb = Label(window_system_frame_wds, text="Шаг 5: Выберите систему")
    window_system_wds_lb.grid(row=0, column=0, columnspan=6, sticky="w")

    ecosol_60_wds_r_btn = Radiobutton(window_system_frame_wds, text="5 Siries", variable=window_system_wds,
                                      value="5 Siries")
    ecosol_60_wds_r_btn.grid(row=1, column=0, sticky="w")

    ecosol_70_wds_r_btn = Radiobutton(window_system_frame_wds, text="6 Siries", variable=window_system_wds,
                                      value="6 Siries")
    ecosol_70_wds_r_btn.grid(row=1, column=1, sticky="w")

    brilliant_design_wds_r_btn = Radiobutton(window_system_frame_wds, text="WDS 300", variable=window_system_wds,
                                             value="WDS 300")
    brilliant_design_wds_r_btn.grid(row=1, column=2, sticky="w")

    show_window_system_wds_btn = Button(text="Показать выбранное", command=show_window_system_wds)
    show_window_system_wds_btn.pack()

    price_lb2 = Label(text="Цена:", width=20, height=1, background="yellow")
    price_lb2.pack()

    reset_pararms_btn = Button(text="Сбросить параметры", width=20, height=1)
    reset_pararms_btn.pack()

    root.mainloop()
