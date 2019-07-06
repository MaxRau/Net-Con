from libs.helpers import get_running_config
from libs.simulator import run_simulator
from lxml import etree

config = get_running_config('138.120.48.30', '830', 'admin', 'Alcatel', {'name':'junos'})
assert isinstance(config, etree._Element)
print(etree.tostring(config))
#server = run_simulator('8300', config)
#assert isinstance(server, simulator)
#server.close()
