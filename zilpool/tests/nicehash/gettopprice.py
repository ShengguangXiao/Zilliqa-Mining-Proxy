from zilpool.nicehash import *
from zilpool.common import utils

pubApi = public_api("https://api2.nicehash.com", True)

# Get all algorithms
algorithms = pubApi.get_algorithms()
logging.info(algorithms)

config = utils.merge_config('./pool.conf')

privApi = private_api(config.nicehash, algorithms)

top_price = privApi.get_top_price()
print(top_price)