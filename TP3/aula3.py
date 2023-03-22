from buyerAgent import BuyerAgent
from sellerAgent import SellerAgent
import time

if __name__ == "__main__":
    pwd = "Openfire_password1"
    seller = SellerAgent("seller@192.168.56.1", pwd)
    future = seller.start()
    future.wait()
    buyer = BuyerAgent("buyer@192.168.56.1", pwd)
    buyer.start()


    while seller.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            seller.stop()
            buyer.stop()
            break
    print("Agents finished")