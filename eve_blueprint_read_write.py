import fuzzworks
from typing import Union


class blueprint:
    def __init__(self, id: Union[int, str] = None, name: str = None):
        """
        Just a blueprint for eve online, catered aroudn manufacturing
        :param id: is the id number of the blueprint
        """
        if not id and name:
            self.name = name
            self.id = fuzzworks.get_single_id(name)
        elif id and not name:
            self.id = str(id)
            self.name = self.get_name()

        self.materials_req = self.get_mat_reqs()

    def get_mat_reqs(self) -> list:
        """

        :return: list of materials
        """
        materials_list: [blueprint_mats_manufacturing] = []
        mat_list = fuzzworks.get_manufacturing_materials(
            fuzzworks.get_blueprint_details(self.id))
        for required_material in mat_list:
            materials_list.append(required_material)

        return materials_list

    def get_name(self) -> str:
        name = str
        return name


class blueprint_mats_manufacturing:
    def __init__(self, dict_info):
        """

        :param dict_info:
            name is the name of the item required
            bp_id is the blueprint id
            maketype is the id of the finished material
        """
        self.name = dict_info['name']
        self.bp_id = dict_info['typeid']
        self.item_id = dict_info['maketype']
        self.quantity = dict_info['quantity']
