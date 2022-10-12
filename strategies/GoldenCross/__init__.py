from jesse.strategies import Strategy, cached
import jesse.indicators as ta
from jesse import utils


class GoldenCross(Strategy):
    @property
    def ema20(self):
        return ta.ema(self.candles, 20)
    
    @property
    def ema50(self):
        return ta.ema(self.candles, 50)
    
    @property
    def trend(self):
        # uptrend
        if self.ema20 > self.ema50:
            return 1
        else: # downtrend
            return -1

    def should_long(self) -> bool:
        return self.trend == 1

    def go_long(self):
        entry_price = self.price
        qty = utils.size_to_qty(self.balance*0.5, entry_price)
        self.buy = qty, entry_price # MARKET order
    
    def update_position(self) -> None:
        if self.reduced_count == 1:
            self.stop_loss = self.position.qty, self.price - self.current_range
        elif self.trend == -1:
            # close the position using a MARKET order
            self.liquidate()

    @property
    def current_range(self):
        return self.high - self.low

    def on_open_position(self, order) -> None:
        self.stop_loss = self.position.qty, self.price - self.current_range*2
        self.take_profit = self.position.qty/2, self.price + self.current_range*2

    def should_cancel_entry(self) -> bool:
        return True
    
    # # # # # # # # # # # # 
    # Filters
    # # # # # # # # # # # # 

    def filters(self) -> list:
        return [
            self.rsi_filter
        ]
    
    def rsi_filter(self):
        rsi = ta.rsi(self.candles)
        return rsi < 65
    