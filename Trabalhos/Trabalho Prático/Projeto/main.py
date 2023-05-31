import logging
from logging import Filter


def disable_logging():
    class IQFilter(Filter):
        def filter(self, record):
            return False if "Unhandleable IQ request" in record.msg else True

    logging.basicConfig(level=logging.ERROR, format='%(asctime)s [%(levelname)s] %(message)s')
    handler = logging.StreamHandler()
    handler.setLevel(logging.ERROR)
    handler.addFilter(IQFilter())
    logger = logging.getLogger('spade')
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)

disable_logging()

from Tower.tower import TowerAgent
from Airplane.airplane import AirplaneAgent
from GareManager.gareManager import GareManagerAgent
from Admin.admin import AdminAgent
from messages import AirplaneData
from config import config
import time
import random


if __name__ == "__main__":

    try:

        gares_free = [random.randint(0, 1) == 0 for _ in range(config.num_gares)]
        occupied_gares = [i for i in range(config.num_gares) if not gares_free[i]]

        gareManager = GareManagerAgent(occupied_gares, f"gare_manager@{config.host}", config.password)
        f = gareManager.start()
        f.wait()

        tower = TowerAgent(f"tower@{config.host}", config.password)
        f = tower.start()
        f.wait()

        futures = []

        # Initial airport state
        for g, free in enumerate(gares_free):
            plane = AirplaneAgent(gareManager.gares[g] if not free else None, f"plane{g}@{config.host}", config.password)
            f = plane.start()
            f.wait()
            futures.append(f)
            if not free:
                tower.add_plane(AirplaneData(plane))


        admin = AdminAgent(f"admin@{config.host}", config.password)
        f = admin.start()
        f.wait()

        g = config.num_gares
        while True:
            time.sleep(config.arrival_interval)
            # New plane arrived
            plane = AirplaneAgent(None, f"plane{g}@{config.host}", config.password)
            f = plane.start()
            futures.append(f)
            g += 1

            # Update weather
            if config.weather_state != -1:
                if random.randint(0, 1) == 0:
                    if config.weather_state == 3:
                        config.weather_state = -1
                    config.weather_state += 1

    except KeyboardInterrupt:
        print("Stopping...")