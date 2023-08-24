print("travel app")
#
# Желаемые гео-локации:

# Список мест, которые вы хотели бы посетить.

#################################################################

# Список билетов:

# Транспорт:

# Авиабилеты:
# Даты и направления полетов.

# Железнодорожные билеты:
# Даты и маршруты поездов.

# Билеты на водный транспорт:
# Детали маршрута и даты путешествия.


# Развлечения:

# Музеи:
# Список интересующих вас музеев.

# Театры:
# Информация о спектаклях и датах посещения.

# Спортивные мероприятия:
# Соревнования, матчи или события, которые вы хотите посетить.

# Музыкальные мероприятия:
# Концерты или фестивали, которые вас интересуют.

#################################################################
# Список вещей для поездки:

# Для себя:

# Личные вещи:
# Одежда, обувь, аксессуары.

# Техника:
# Смартфон, ноутбук, зарядные устройства.

# Туалетные принадлежности:
# Зубная паста, щетка, гигиенические средства и т.д.

# Медикаменты:
# Лекарства, аптечка.


# Для семьи (если есть):

# Детские вещи:
# Подгузники, детская одежда, игрушки.

# Семейные принадлежности:
# Общие предметы, которые могут понадобиться семье.

#################################################################
# Общий бюджет поездки:

# Разделение бюджета на следующие категории:

# Транспорт:
# Расходы на билеты.

# Развлечения:
# Затраты на посещение музеев, театров, спортивных и музыкальных мероприятий.

# Проживание:
# Затраты на отель или другие варианты размещения.

# Питание:
# Примерный бюджет на еду и напитки.

# Дополнительные расходы:
# Непредвиденные затраты и сouvenirs


import json

def create_trip(geo_locations, tickets, activities, packing_list, budget):
    trip = {
        "geo_locations": geo_locations,
        "tickets": tickets,
        "activities": activities,
        "packing_list": packing_list,
        "budget": budget
    }
    return trip

def save_trip_to_json(trip, filename):
    with open(filename, "w") as file:
        json.dump(trip, file, indent=4)

def load_trip_from_json(filename):
    with open(filename, "r") as file:
        trip = json.load(file)
    return trip

# Пример использования
desired_geo_locations = ["Paris", "Rome", "Barcelona"]
ticket_details = {
    "air_tickets": [{"date": "2023-09-01", "destination": "Paris"}, {"date": "2023-09-10", "destination": "Rome"}],
    "train_tickets": [{"date": "2023-09-02", "route": "Rome to Barcelona"}],
    "water_tickets": [{"date": "2023-09-05", "route": "Barcelona to Rome"}]
}
activities = {
    "museums": ["Louvre", "Vatican Museums"],
    "theatres": [{"show": "Romeo and Juliet", "date": "2023-09-03"}],
    "sports": ["Football match on 2023-09-07"],
    "music": ["Music festival on 2023-09-12"]
}
packing_list = {
    "personal": ["Clothes", "Shoes", "Accessories"],
    "electronics": ["Smartphone", "Laptop", "Chargers"],
    "toiletries": ["Toothpaste", "Toothbrush", "Hygiene products"],
    "medicines": ["Medications", "First aid kit"],
    "family": {
        "children": ["Diapers", "Kids' clothes", "Toys"],
        "family_items": ["Stroller", "Baby food"]
    }
}
budget_allocation = {
    "transportation": 1000,
    "activities": 500,
    "accommodation": 800,
    "food": 400,
    "extras": 200
}

trip = create_trip(desired_geo_locations, ticket_details, activities, packing_list, budget_allocation)

save_trip_to_json(trip, "trip_plan.json")
loaded_trip = load_trip_from_json("trip_plan.json")

print(loaded_trip)





