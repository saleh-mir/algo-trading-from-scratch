from jesse.strategies import Strategy, cached
import jesse.indicators as ta
from jesse import utils

class ExampleStrategy(Strategy):
    def before(self) -> None:
        self.log('before exetuing other methods')

    def after(self) -> None:
        self.log('after executing other methods')

    def should_long(self) -> bool:
        return True

    def go_long(self) -> None:
        # current price: 21000
        self.buy = 1, 21_000 # MARKET order

    def should_cancel_entry(self) -> bool:
        return True
    
    def update_position(self) -> None:
        # # add to the current position
        # # current BTC price: 21_000
        # self.buy = 1, 21_000

        # # reduce the current position
        # # current BTC price: 21_000
        # self.take_profit = 0.5, 21_000

        # close the position
        # current BTC price: 21_000
        self.take_profit = 1, 21_000 # MARKET order

        

    