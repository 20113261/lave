#!usr/env/python
#coding=UTF-8
from common.class_common import Car


class CarDB():

    def __init__(self):
        self.car = Car()

    def carTupleList(self,car_list):

        result = []
        for edict in car_list:
            each_dict = eval(edict)
            self.car.source = each_dict['source']
            self.car.company = each_dict['company']
            self.car.car_type = each_dict['car_type']
            self.car.car_desc = each_dict['car_desc']
            self.car.car_image = each_dict['car_image']
            self.car.price = each_dict['price']
            self.car.list_price = each_dict['list_price']
            self.car.rest =  each_dict['rest']
            self.car.currency = each_dict['currency']
            self.car.rent_city = each_dict['rent_city']
            self.car.rent_store = each_dict['rent_store']
            self.car.return_store = each_dict['return_store']
            self.car.rent_time = each_dict['rent_time']
            self.car.rent_area = each_dict['rent_area']
            self.car.return_area = each_dict['return_area']
            self.car.is_automatic = each_dict['is_automatic']
            self.car.baggages = each_dict['baggages']
            self.car.passengers = each_dict['passengers']
            self.car.pay_method = each_dict['pay_method']
            self.car.insurance = each_dict['insurance']
            self.car.fuel_strategy = each_dict['fuel_strategy']
            self.car.promotion = each_dict['promotion']
            self.car.license = each_dict['license']

            car_tuple = (self.car.source,self.car.company,self.car.car_type,self.car.car_desc,self.car.car_image, \
                    self.car.price,self.car.list_price,self.car.rest,self.car.currency,self.car.rent_city,self.car.rent_store, \
                    self.car.return_rule,self.car.rent_time,self.car.rent_area,self.car.return_area,self.car.is_automatic,\
                    self.car.baggages,self.car.passengers,self.car.pay_method,self.car.insurance,self.car.fuel_strategy,self.car.promotion, \
                    self.car.license)
            result.append(car_tuple)

        return result

