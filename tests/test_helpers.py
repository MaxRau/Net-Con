from libs.helpers import get_running_config
from ncclient import manager
import mock
import lxml
import pytest

#@mock.patch('manager.connect')
def test_get_running_config():
    #manager.connect.return_value = ''
    config = get_running_config('138.120.48.30', '830', 'admin', 'Alcatel', {'name':'junos'})
    assert isinstance(config, lxml.etree._Element)
