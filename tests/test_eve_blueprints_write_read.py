from fuzzworks_bpos import eve_blueprint_read_write as bp_lib
from fuzzworks_bpos import fuzzworks as fw

test_blueprint_name = "Condor"
test_blueprint_id = '684'

BOM = {"Tritanium": 32000, "Pyerite": 6000,  # tested bp
       "Mexallon": 2500, "Isogen": 500}

bp_details = ['requestedid', 'blueprintSkills', 'blueprintDetails', 'activityMaterials', 'decryptors']


def test_get_blueprint_details():
    """Tests that we get the blueprint details from Fuzzworks"""
    # tested_bp = bp_lib.blueprint(name=test_blueprint_name)
    tested_bp_deets = fw.get_blueprint_details(test_blueprint_id)

    for section in bp_details:
        if section not in tested_bp_deets.keys():
            assert False
    assert True


def test_get_materials_for_blueprint():
    """
    Tests that the materials for a blueprint
    :return:
    """
    tested_bp = bp_lib.blueprint(name=test_blueprint_name)
    mat: bp_lib.blueprint_mats_manufacturing
    for mat in tested_bp.materials_req:
        # for tested_material in BOM.fromkeys():
        if mat.name not in list(BOM.keys()):
            assert False
        if mat.quantity != BOM[mat.name]:
            assert False

    assert True


def test_make_bp_with_no_name():
    """
    Make a blueprint with no name and with an id, tests integrated code
    :return:
    """
    if bp_lib.blueprint(id=test_blueprint_id).name != 'Condor Blueprint':
        assert False
    assert True


def test_make_bp_with_no_id():
    """
    Make a blueprint with a name and no id, tests integrated code
    :return:
    """
    if bp_lib.blueprint(name=test_blueprint_name).id != '684':
        assert False
    assert True
