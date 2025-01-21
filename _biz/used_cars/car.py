import json

from _biz.used_cars.utils import get_dict_val_path

class Car:
    def __init__(self, item):
        self.year = get_dict_val_path(item, "year", "1900")
        self.trim = get_dict_val_path(item, "trim", "__trim__")
        self.link = get_dict_val_path(item, "vdpUrl", "__link__")
        self.dealer = get_dict_val_path(item, "dealerBadgingExperience", "__dealer__")
        self.dealer_city = get_dict_val_path(item, "dealer.city", "__city__")
        self.dealer_name = get_dict_val_path(item, "dealer.name", "__dealer_name__")
        self.price = get_dict_val_path(item, "currentPrice", 1000000)
        self.miles = get_dict_val_path(item, "mileage", 1000000)
        self.sub_trim = get_dict_val_path(item, "subTrim", "__sub_trim__")
        self.first_seen = get_dict_val_path(item, "firstSeen", "__firstSeen__")
        self.badge = get_dict_val_path(item, "badge", "__badge__")
        self.vin = get_dict_val_path(item, "vin", "__vin__")
        priceHistory = get_dict_val_path(item, "priceHistory", [])
        self.price_history = [x for x in priceHistory if "listPrice" in x]
        if self.sub_trim == "Unspecified":
            self.sub_trim = ""
        img_larges = get_dict_val_path(item, "images.large", [])
        self.image = ""
        if len(img_larges) > 0:
            self.image = img_larges[0]


