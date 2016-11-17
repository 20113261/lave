#!usr/env/python
#coding=UTF-8
from common.class_common import Hotel

class HotelDB():
    
    def __init__(self):
        self.hotel = Hotel()

    def hotelTupleList(self,ticket_list):

        result = []
        
        for edict in ticket_list:
            each_dict = eval(edict)
            self.hotel.hotel_name = each_dict['hotel_name']
            self.hotel.hotel_name_en = each_dict['hotel_name_en']
            self.hotel.source = each_dict['source']
            self.hotel.source_id = each_dict['source_id']
            self.hotel.brand_name = each_dict['brand_name']
            self.hotel.map_info = each_dict['map_info']
            self.hotel.address = each_dict['address']
            self.hotel.city = each_dict['city']
            self.hotel.country = each_dict['country']
            self.hotel.postal_code = each_dict['postal_code']
            self.hotel.star = each_dict['star']
            self.hotel.grade = each_dict['grade']
            self.hotel.has_wifi = each_dict['has_wifi']
            self.hotel.is_wifi_free = each_dict['is_wifi_free']
            self.hotel.has_parking = each_dict['has_parking']
            self.hotel.is_parking_free = each_dict['is_parking_free']
            self.hotel.service = each_dict['service']
            self.hotel.img_items = each_dict['img_items']
            self.hotel.description = each_dict['description']

            hotel_tuple = (self.hotel.hotel_name, self.hotel.hotel_name_en, self.hotel.source, \
                    self.hotel.source_id, self.hotel.brand_name, self.hotel.map_info, self.hotel.address,\
                    self.hotel.city, self.hotel.country, self.hotel.postal_code, self.hotel.star, \
                    self.hotel.grade, self.hotel.has_wifi, self.hotel.is_wifi_free, self.hotel.has_parking, \
                    self.hotel.is_parking_free, self.hotel.service, self.hotel.img_items, self.hotel.description)
            result.append(hotel_tuple)


        return result
