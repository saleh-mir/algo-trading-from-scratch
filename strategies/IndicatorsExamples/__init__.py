from jesse.strategies import Strategy, cached
import jesse.indicators as ta
from jesse import utils


class IndicatorsExamples(Strategy):
    def should_long(self) -> bool:
        rsi = ta.rsi(self.candles)
        ema50 = ta.ema(self.candles, 50)

        if self.price > ema50 and rsi < 30:
            # do something
            return True

        return False

    def go_long(self):
        pass

    def should_short(self) -> bool:
        # For futures trading only
        return False

    def go_short(self):
        # For futures trading only
        pass

    def should_cancel_entry(self) -> bool:
        return True
