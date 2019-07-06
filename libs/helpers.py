from ncclient import manager
from lxml import etree

def get_running_config(ip, port, uname, pw, device_params):
    session = manager.connect(host=ip, port=port, username=uname, password=pw, device_params=device_params, hostkey_verify=False)
    config = session.get_config(source='running').data_xml
    config_tree = etree.fromstring(config.encode('UTF-8'))
    return config_tree