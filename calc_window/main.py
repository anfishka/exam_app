from tkinter import *

if __name__ == '__main__':


    root = Tk()
    root.title("Калькулятор пластиковых окон")
    root.geometry("1000x400")

    selected_window_type = ""
    selected_profile = ""
    selected_system = ""
    selected_glazing = ""
    selected_options = []

    windowsill_cb_v = IntVar()
    window_tide_cb_v = IntVar()
    window_slopes_cb_v = IntVar()
    window_mosquito_net_cb_v = IntVar()
    window_montage_demontage_cb_v = IntVar()

    MIN_WIDTH_WINDOW = 500
    MAX_WIDTH_WINDOW = 1600

    MIN_HEIGHT_WINDOW = 500
    MAX_HEIGHT_WINDOW = 1800

    MIN_WIDTH_DOOR = 500
    MAX_WIDTH_DOOR = 1000

    MIN_HEIGHT_DOOR = 1350
    MAX_HEIGHT_DOOR = 2350

    PRICE_REHAU = 2.80
    PRICE_WDS = 1.80
    PRICE_SALAMANDER = 1.40

    INITIAL_PRICE_REHAU = 800
    INITIAL_PRICE_SALAMANDER = 600
    INITIAL_PRICE_WDS = 720

    GLAZING_COSTS = {
        "Однокамерный":200,
        "Двухкамерный":400,
        "Энергосберегающий": 600,
        "Солнцезащитный": 800
    }
    OPTION_COSTS = {
        "Подоконник": 120,
        "Отлив": 140,
        "Откосы": 400,
        "Москитная сетка": 250,
        "Монтаж / Демонтаж": 260
    }

    SYSTEM_COSTS = {
        "5 Siries": 1.80,
        "6 Siries": 1.92,
        "WDS 300": 2.15,
        "Bluevolution 82": 1.40,
        "Steamline": 1.65,
        "BluEvolution 92": 1.86,
        "Ecosol-60": 2.80,
        "Ecosol-70": 2.96,
        "Brilliant Design": 3.12,
        "Synego": 3.23,
        "Geneo": 3.31
    }

    OPTIONS = {
        "Подоконник": windowsill_cb_v,
        "Отлив": window_tide_cb_v,
        "Откосы": window_slopes_cb_v,
        "Москитная сетка": window_mosquito_net_cb_v,
        "Монтаж / Демонтаж": window_montage_demontage_cb_v
    }

    window1_i = PhotoImage(file="window_open_tilt_1.gif")
    window2_i = PhotoImage(file="window_open_tilt_2_r.gif")
    window3_i = PhotoImage(file="window_open_tilt_3_r.gif")
    window4_i = PhotoImage(file="window_open_tilt_4_r.gif")
    deaf_window_i = PhotoImage(file="window_deaf_r.gif")
    window2_d_i = PhotoImage(file="window_d_tilt_2_r.gif")
    window3_d_i = PhotoImage(file="window_d_tilt_3_r.gif")

    ######################################################################

    def validate_input(value):
        if not value.isdigit():
            return False
        num = int(value)
        return MIN_WIDTH_WINDOW <= num <= MAX_WIDTH_WINDOW


    def validate_height(value):
        if not value.isdigit():
            return False
        num = int(value)
        return MIN_HEIGHT_WINDOW <= num <= MAX_HEIGHT_WINDOW


    def validate_door_width(value):
        if not value.isdigit():
            return False
        num = int(value)
        return MIN_WIDTH_DOOR <= num <= MAX_WIDTH_DOOR


    def validate_door_height(value):
        if not value.isdigit():
            return False
        num = int(value)
        return MIN_HEIGHT_DOOR <= num <= MAX_HEIGHT_DOOR


    def input_frame_ok_clicked():
        width_value = width_window_tb.get("1.0", "end-1c")
        height_value = height_window_tb.get("1.0", "end-1c")
        door_width_value = width_door_tb.get("1.0", "end-1c")
        door_height_value = height_door_tb.get("1.0", "end-1c")

        if not validate_input(width_value) or not validate_height(height_value) or \
                not validate_door_width(door_width_value) or not validate_door_height(door_height_value):
            error_label.config(text="Пожалуйста, введите корректные значения. \nМинимальная ширина окна: 500 мм. Максимальная ширина окна: 1600 мм. \nМинимальная высота окна: 500 мм. Максимальная высота окна: 1800 мм. \nМинимальная ширина двери: 500 мм. Максимальная ширина двери: 1000 мм.\nМинимальная высота двери: 1350мм. Максимальная высота двери: 2350 мм.")


            return

        show_choose_prof_frame()

    def show_input_frame():

        choose_frame.pack_forget()
        input_frame.pack(anchor="nw", padx=10, pady=10)


    def show_choose_prof_frame():
        input_frame.pack_forget()
        choose_prof_frame.pack(anchor="nw")


    def show_window_system_brand():
        choose_prof_frame.pack_forget()
        selected_profile = window_profile.get()
        if selected_profile == "WDS":
            window_system_frame_wds.pack(anchor="nw")
        elif selected_profile == "Rehau":
            window_system_frame_rehau.pack(anchor="nw")
        elif selected_profile == "Salamander":
            window_system_frame_salamander.pack(anchor="nw")


    def show_glazing_frame():
        window_system_frame_wds.pack_forget()
        window_system_frame_salamander.pack_forget()
        window_system_frame_rehau.pack_forget()
        glazing_frame.pack(anchor="nw")


    def show_options_frame():
        glazing_frame.pack_forget()
        options_frame.pack(anchor="nw")


    def show_price_frame():
        options_frame.pack_forget()
        price_frame.pack(anchor="nw")

        selected_profile = window_profile.get()
        if selected_profile == "WDS":
            selected_system = window_system_wds.get()
        elif selected_profile == "Rehau":
            selected_system = window_system_rehau.get()
        elif selected_profile == "Salamander":
            selected_system = window_system_salamander.get()

        selected_glazing = glazing.get()

        total_price = calculate_price()

        price_frame_lb.config(
            text=f"Выбрано:\n\nТип профиля:  {selected_profile} \nТип системы:  {selected_system} \nCтеклопакет:  {selected_glazing} \nОбщая стоимость: {total_price} грн"
        )


    def extract_int(txt):
        text = txt.get("1.0", END).strip()
        if text.isdigit():
            return int(text)
        else:
            return 0


    def calculate_price():
        width_mm = extract_int(width_window_tb)
        height_mm = extract_int(height_window_tb)
        door_width_mm = extract_int(width_door_tb)
        door_height_mm = extract_int(height_door_tb)

        profile = window_profile.get()
        glazing_type = glazing.get()
        system = ""


        if profile == "Rehau":
            initial_price = INITIAL_PRICE_REHAU
            mm_price = PRICE_REHAU
            system = window_system_rehau.get()
        elif profile == "Salamander":
            initial_price = INITIAL_PRICE_SALAMANDER
            mm_price = PRICE_SALAMANDER
            system = window_system_salamander.get()
        elif profile == "WDS":
            initial_price = INITIAL_PRICE_WDS
            mm_price = PRICE_WDS
            system = window_system_wds.get()

        total_width_price = initial_price + (width_mm - 500) * mm_price
        total_glazing_cost = GLAZING_COSTS.get(glazing_type, 0)
        total_option_cost = 0
        for opt, var in OPTIONS.items():
            if var.get():
                total_option_cost += OPTION_COSTS[opt]
        total_system_cost = SYSTEM_COSTS.get(system, 0) * (width_mm + height_mm + door_width_mm + door_height_mm) / 4

        total_price = total_width_price + total_glazing_cost + total_option_cost + total_system_cost

        total_price = round(total_price, 2)

        return total_price


    #################################################################################
    # Step 1: Choose Window
    choose_frame = Frame(root)
    choose_frame.pack(anchor="nw", side="top")

    choose_window_lb = Label(choose_frame, text="Шаг 1. Выберите какое у вас окно:")
    choose_window_lb.grid(row=0, column=0, sticky="w")

    deaf_window_btn = Button(choose_frame, image=deaf_window_i, command=show_input_frame)
    deaf_window_btn.grid(row=1, column=0, sticky="w")

    window1_btn = Button(choose_frame, image=window1_i, command=show_input_frame)
    window1_btn.grid(row=1, column=1,  sticky="w")

    window2_btn = Button(choose_frame, image=window2_i, command=show_input_frame)
    window2_btn.grid(row=1, column=2, sticky="w")

    window3_btn = Button(choose_frame, image=window3_i, command=show_input_frame)
    window3_btn.grid(row=1, column=3, sticky="w")

    window4_btn = Button(choose_frame, image=window4_i, command=show_input_frame)
    window4_btn.grid(row=2, column=0, sticky="w")

    window2_d_btn = Button(choose_frame, image=window2_d_i, command=show_input_frame)
    window2_d_btn.grid(row=2, column=1, sticky="w")

    window3_d_btn = Button(choose_frame, image=window3_d_i, command=show_input_frame)
    window3_d_btn.grid(row=2, column=2, sticky="w")

    ########################################################################
    # Step 2: Input Parameters

    input_frame = Frame(root)

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

    input_frame_ok = Button(input_frame, text="OK", command=input_frame_ok_clicked)
    input_frame_ok.grid(row=4, column=3, sticky="w")

    error_label = Label(input_frame, text="", fg="red")
    error_label.grid(row=5, columnspan=4, sticky="w")

    windowsill_cb_v = IntVar()
    window_tide_cb_v = IntVar()
    window_slopes_cb_v = IntVar()
    window_mosquito_net_cb_v = IntVar()
    window_montage_demontage_cb_v = IntVar()

    ####################################################################################
    # Step 6: Options

    options_frame = Frame(root)

    height_door_lb = Label(options_frame, text="Шаг 3: Выберите дополнительные опции:")
    height_door_lb.grid(row=0, column=0, columnspan=6, sticky="w")

    windowsill_cb = Checkbutton(options_frame, text="Подоконник", variable=windowsill_cb_v)
    windowsill_cb.grid(row=1, column=0, sticky="w")

    window_tide_cb = Checkbutton(options_frame, text="Отлив", variable=window_tide_cb_v)
    window_tide_cb.grid(row=1, column=1, sticky="w")

    window_slopes_cb = Checkbutton(options_frame, text="Откосы", variable=window_slopes_cb_v)
    window_slopes_cb.grid(row=1, column=2, sticky="w")

    window_mosquito_net_cb = Checkbutton(options_frame, text="Москитная сетка", variable=window_mosquito_net_cb_v)
    window_mosquito_net_cb.grid(row=1, column=3, sticky="w")

    window_montage_demontage_cb = Checkbutton(options_frame, text="Монтаж / Демонтаж",
                                              variable=window_montage_demontage_cb_v)
    window_montage_demontage_cb.grid(row=1, column=4, sticky="w")

    input_frame_ok = Button(options_frame, text="OK", command=show_price_frame)
    input_frame_ok.grid(row=4, column=3, sticky="w")

    window_profile = StringVar()
    window_profile.set("Rehau")
    #
    ##################################################################################
    # # Step 3: Choose Profile

    choose_prof_frame = Frame(root)

    choose_prof = Label(choose_prof_frame, text="Шаг 4: Выберите тип профиля:")
    choose_prof.grid(row=0, column=0, columnspan=6, sticky="w")

    rehau_r_btn = Radiobutton(choose_prof_frame, text="Rehau", variable=window_profile, value="Rehau")
    rehau_r_btn.grid(row=1, column=0, sticky="w")

    salamander_r_btn = Radiobutton(choose_prof_frame, text="Salamander", variable=window_profile, value="Salamander")
    salamander_r_btn.grid(row=1, column=1, sticky="w")

    wds_r_btn = Radiobutton(choose_prof_frame, text="WDS", variable=window_profile, value="WDS")
    wds_r_btn.grid(row=1, column=2, sticky="w")

    choose_prof_frame_ok = Button(choose_prof_frame, text="ОК", command=show_window_system_brand)
    choose_prof_frame_ok.grid(row=1, column=3, sticky="w")

    ###############################################################################################
    glazing = StringVar()
    glazing.set("Однокамерный")

    # Step 5: Choose Glazing

    glazing_frame = Frame(root)

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

    glazing_frame_ok = Button(glazing_frame, text="ОК", command=show_options_frame)
    glazing_frame_ok.grid(row=1, column=4, sticky="w")

    ##############################################################################################
    # Step 4: Choose System

    window_system_rehau = StringVar()
    window_system_rehau.set("Ecosol-60")

    # FOR REHAU
    window_system_frame_rehau = Frame(root)

    window_system_rehau_lb = Label(window_system_frame_rehau, text="Шаг 5: Выберите систему")
    window_system_rehau_lb.grid(row=0, column=0, columnspan=6, sticky="w")

    ecosol_60_rehau_r_btn = Radiobutton(window_system_frame_rehau, text="Ecosol-60", variable=window_system_rehau, value="Ecosol-60")
    ecosol_60_rehau_r_btn.grid(row=1, column=0, sticky="w")

    ecosol_70_rehau_r_btn = Radiobutton(window_system_frame_rehau, text="Ecosol-70", variable=window_system_rehau,value="Ecosol-70")
    ecosol_70_rehau_r_btn.grid(row=1, column=1, sticky="w")

    brilliant_design_rehau_r_btn = Radiobutton(window_system_frame_rehau, text="Brilliant Design",variable=window_system_rehau, value="Brilliant Design")
    brilliant_design_rehau_r_btn.grid(row=1, column=2, sticky="w")

    synego_rehau_r_btn = Radiobutton(window_system_frame_rehau, text="Synego", variable=window_system_rehau,value="Synego")
    synego_rehau_r_btn.grid(row=1, column=3, sticky="w")

    geneo_rehau_r_btn = Radiobutton(window_system_frame_rehau, text="Geneo", variable=window_system_rehau,value="Geneo")
    geneo_rehau_r_btn.grid(row=1, column=3, sticky="w")

    window_system_frame_rehau_ok = Button(window_system_frame_rehau, text="OK", command=show_glazing_frame)
    window_system_frame_rehau_ok.grid(row=1, column=4, sticky="w")

    window_system_salamander = StringVar()
    window_system_salamander.set("Steamline")

    # FOR SALAMANDER
    window_system_frame_salamander = Frame(root)

    window_system_salamander_lb = Label(window_system_frame_salamander, text="Шаг 5: Выберите систему")
    window_system_salamander_lb.grid(row=0, column=0, columnspan=6, sticky="w")

    bluevolution_82_salamander_r_btn = Radiobutton(window_system_frame_salamander, text="Bluevolution 82", variable=window_system_salamander, value="Bluevolution 82")
    bluevolution_82_salamander_r_btn.grid(row=1, column=0, sticky="w")

    steamline_r_salamander_btn = Radiobutton(window_system_frame_salamander, text="Steamline",variable=window_system_salamander, value="Steamline")
    steamline_r_salamander_btn.grid(row=1, column=1, sticky="w")

    bluevolution_92_salamander_r_btn = Radiobutton(window_system_frame_salamander, text="BluEvolution 92",variable=window_system_salamander, value="BluEvolution 92")
    bluevolution_92_salamander_r_btn.grid(row=1, column=2, sticky="w")

    window_system_frame_salamander_ok = Button(window_system_frame_salamander, text="OK", command=show_glazing_frame)
    window_system_frame_salamander_ok.grid(row=1, column=3, sticky="w")

    window_system_wds = StringVar()
    window_system_wds.set("5 Siries")

    # FOR WDS
    window_system_frame_wds = Frame(root)

    window_system_wds_lb = Label(window_system_frame_wds, text="Шаг 5: Выберите систему")
    window_system_wds_lb.grid(row=0, column=0, columnspan=6, sticky="w")

    siries_5_wds_r_btn = Radiobutton(window_system_frame_wds, text="5 Siries", variable=window_system_wds, value="5 Siries")
    siries_5_wds_r_btn.grid(row=1, column=0, sticky="w")

    siries_6_wds_r_btn = Radiobutton(window_system_frame_wds, text="6 Siries", variable=window_system_wds, value="6 Siries")
    siries_6_wds_r_btn.grid(row=1, column=1, sticky="w")

    wds300_wds_r_btn = Radiobutton(window_system_frame_wds, text="WDS 300", variable=window_system_wds, value="WDS 300")
    wds300_wds_r_btn.grid(row=1, column=2, sticky="w")

    window_system_frame_wds_ok = Button(window_system_frame_wds, text="OK", command=show_glazing_frame)
    window_system_frame_wds_ok.grid(row=1, column=3, sticky="w")

    ##############################################################################################
    # # Step 7: Calculate Price



    price_frame = Frame(root)

    price_frame_lb = Label(price_frame, text=f"Общая стоимость: {calculate_price()} грн.",  background="blue", fg="#fff", font=("Helvetica", 16))
    price_frame_lb.pack()

    root.mainloop()

