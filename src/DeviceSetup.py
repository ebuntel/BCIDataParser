
class DeviceSetup:
    """Data class holding various information on the device setup

    Attributes:
        name: Name of this DeviceSetup object
        update_rate_HZ: The frequency of fNIRS device
    """

    def __init__(self, update_rateHZ=0):
        self.update_rate_HZ = update_rateHZ
