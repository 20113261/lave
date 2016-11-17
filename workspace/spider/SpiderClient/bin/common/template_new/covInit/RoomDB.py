#!usr/env/python
#coding=UTF-8
from common.class_common import Room


class RoomDB():

    def __init__(self):
        self.room = Room()

    def roomTupleList(self,room_list):

        result = []
	print type(self.room)
        for edict in room_list:
            each_dict = eval(edict)
            self.room.hotel_name = each_dict['hotel_name']
            self.room.city = each_dict['city']
            self.room.source = each_dict['source']
            self.room.source_hotelid = each_dict['source_hotelid']
            self.room.source_roomid = each_dict['source_roomid']
            self.room.real_source = each_dict['real_source']
            self.room.room_type = each_dict['room_type']
            self.room.occupancy = each_dict['occupancy']
            self.room.bed_type = each_dict['bed_type']
            self.room.size = each_dict['size']
            self.room.floor = each_dict['floor']
            self.room.check_in = each_dict['check_in']
            self.room.check_out = each_dict['check_out']
            self.room.rest = each_dict['rest']
            self.room.tax = each_dict['tax']
            self.room.pay_method = each_dict['pay_method']
            self.room.is_extrabed = each_dict['is_extrabed']
            self.room.is_extrabed_free = each_dict['is_extrabed_free']
            self.room.has_breakfast = each_dict['has_breakfast']
            self.room.is_breakfast_free = each_dict['is_breakfast_free']
            self.room.is_cancel_free = each_dict['is_cancel_free']
            self.room.extrabed_rule = each_dict['extrabed_rule']
            self.room.return_rule = each_dict['return_rule']
            self.room.change_rule = each_dict['change_rule']
            self.room.room_desc = each_dict['room_desc']
            self.room.others_info = each_dict['others_info']
            self.room.currency = each_dict['currency']
            self.room.price = each_dict['price']
            self.room.guest_info = each_dict['guest_info']
            
            room_tuple = (self.room.hotel_name,self.room.city,self.room.source,self.room.source_hotelid,self.room.source_roomid, \
                    self.room.real_source,self.room.room_type,self.room.occupancy,self.room.bed_type,self.room.size,self.room.floor,\
		    self.room.check_in, self.room.check_out, self.room.rest, self.room.price, self.room.tax, self.room.currency, self.room.pay_method,self.room.is_extrabed, \
                    self.room.is_extrabed_free,self.room.has_breakfast,self.room.is_breakfast_free,self.room.is_cancel_free,self.room.extrabed_rule, \
                    self.room.return_rule,self.room.change_rule,self.room.room_desc,self.room.others_info,self.room.guest_info)
            result.append(room_tuple)
        
        return result
