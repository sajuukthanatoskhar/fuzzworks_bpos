import requests

fw_api_name_to_id = "https://www.fuzzwork.co.uk/api/typeid2.php?typename="
fw_api_blueprints = "https://www.fuzzwork.co.uk/blueprint/api/blueprint.php?typeid="

activities = {'manufacturing': '1',
              'ME' : '4',
              'TE' : '5',
              'Invention' : '8'}


def get_single_id(name: str) -> str:
    """
    Gets an ID of a single entry from the fuzzwork.co.uk website, amazing!
    :param name: Can be 'Sabre', 'Sabre Blueprint', 'Caldari Shuttle'
    :return:
    """
    if len(name.split(",")) >1:
        name = name[:-1*(len(name.split(",")[-1])+1)]
    return requests.get(fw_api_name_to_id + name).json()[0]['typeID']


def get_blueprint_details(id: str) -> dict:
    """
    Gets the blueprint details
    :param id:
    :return:
    """

    return requests.get(fw_api_blueprints + id).json()


def get_manufacturing_materials(bp_data_dump : dict) -> dict:
    """
    Gets the list of stuff needed for a blueprint to make
    :param bp_data_dump:
    :return:
    """
    if 'activityMaterials' not in bp_data_dump.keys():
        return {}

    return bp_data_dump['activityMaterials'][activities['manufacturing']]
