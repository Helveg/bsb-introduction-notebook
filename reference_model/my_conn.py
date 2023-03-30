from bsb.connectivity import ConnectionStrategy
from bsb import config
from bsb.config import types

@config.node
class MyConnection(ConnectionStrategy):
    preference = config.attr(type=types.list(type=types.float(min=0, max=1)), required=True)
    
    def connect(self, pre, post):
        pass