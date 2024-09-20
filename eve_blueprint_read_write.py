from . import fuzzworks
from typing import Union

class blueprint_mats_manufacturing:
    def __init__(self, dict_info):
        """
        Is the blueprint material for manufacturing
        Could be used for other things like invention/TE/ME
        #todo could just change documentation to fit invention/TE/ME
        :param dict_info:
            name is the name of the item required
            bp_id is the blueprint id
            maketype is the id of the finished material
        """
        self.name = dict_info['name']
        self.bp_id = dict_info['typeid']
        self.item_id = dict_info['maketype']
        self.quantity = dict_info['quantity']


class blueprint:
    def __init__(self, id: Union[int, str] = None, name: str = None):
        """
        Just a blueprint for eve online, catered aroudn manufacturing
        :param name: is the name of the blueprint, optional
        :param id: is the id number of the blueprint

        """
        if not id and name:
            if not name.endswith('blueprint') or not name.endswith('Blueprint'):
                name += " Blueprint"
            self.name = name
            self.id = fuzzworks.get_single_id(self.name)
        elif id and not name:
            self.id = str(id)
            self.name = self.get_name()
        elif not id and not name:
            raise ValueError("No Name or id inputted")

        self.materials_req = self.get_mat_reqs()

    def get_mat_reqs(self) -> list:
        """
        Gets the material requirements for a blueprint
        :return: list of materials
        """
        materials_list: [blueprint_mats_manufacturing] = []
        mat_list = fuzzworks.get_manufacturing_materials(
            fuzzworks.get_blueprint_details(self.id))
        for required_material in mat_list:
            materials_list.append(blueprint_mats_manufacturing(required_material))
        return materials_list

    def get_name(self) -> str:
        name = fuzzworks.get_blueprint_details(self.id)['blueprintDetails']['productTypeName'] + " Blueprint"
        return name
