from netcon.helpers import get_running_config
from netcon.simulator import run_simulator
import lxml

config = get_running_config('127.0.0.1', 'admin', 'admin', {'name':'junos'})
assert isinstance(config, lxml.etree)

server = run_simulator('8080', config)
assert isinstance(server, simulator)
server.close()
