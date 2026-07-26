from machine import Pin
import time


class HX711:
    def __init__(self, dout, pd_sck, gain=128):
        self.dout = dout
        self.pd_sck = pd_sck

        self.dout.init(Pin.IN)
        self.pd_sck.init(Pin.OUT)
        self.pd_sck.value(0)

        self.offset = 0

        if gain == 128:
            self.gain = 1
        elif gain == 64:
            self.gain = 3
        elif gain == 32:
            self.gain = 2
        else:
            self.gain = 1

    def is_ready(self):
        return self.dout.value() == 0

    def _read_raw(self):
        timeout = time.ticks_ms()

        while not self.is_ready():
            if time.ticks_diff(time.ticks_ms(), timeout) > 1000:
                raise OSError("HX711 timeout")

        value = 0

        for _ in range(24):
            self.pd_sck.value(1)
            value = (value << 1) | self.dout.value()
            self.pd_sck.value(0)

        for _ in range(self.gain):
            self.pd_sck.value(1)
            self.pd_sck.value(0)

        if value & 0x800000:
            value |= ~0xFFFFFF

        return value

    def read(self):
        return self._read_raw() - self.offset

    def tare(self, samples=10):
        total = 0
        for _ in range(samples):
            total += self._read_raw()
            time.sleep_ms(10)
        self.offset = total // samples

    def set_offset(self, offset):
        self.offset = offset

    def get_offset(self):
        return self.offset