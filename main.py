import logging
from bitmex import BitmexClient
from binance import BinanceClient
from interface.root_component import Root



logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceClient("HFGVBvIanQrW4TjAupu5b1eIHDd3eY9a4vuhEjF9Elo0xOuxkKC7eTXPYapnG9fN", "uvlzwIsEDCttFlckaJKwwqLot9K5UkBoWDxHBWGz6aM6Wg5jm2DdcFu6cYHlRSH9" ,False, True )

    bitmex = BitmexClient("88d3mpUsWHSK8aQUR8iH9gjL", "kKvVwWgUyyvBO1iDAJRuzhpYrVCii3Br9zthRQ0HZb67lUru" , True)


    root = Root(binance, bitmex)
    root.mainloop()

