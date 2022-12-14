from my_config import user_token, comm_token, offset, line

from vk_base import *

def found_person_info(offset):
    person_info = select(offset)
    list_person = []
    for i in person_info:
        list_person.append(i)
    return f'{list_person[0]} {list_person[1]}, ссылка - {list_person[3]}'

def person_id(offset):
    person_info = select(offset)
    list_person = []
    for i in person_info:
        list_person.append(i)
    return str(list_person[2])

for i in range(0,5):
    offset = i
    print(found_person_info(offset))
    print(person_id(offset))
    # insert_data_units_seen(person_id(offset))