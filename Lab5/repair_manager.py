from mobile_device import MobileDevice
from repair_stats import RepairStats

class RepairManager:


    def __init__(self, store_name):

        self._store_name = store_name
        self._devices = []
        self._repairs = []


    def add_device(self, MobileDevice):
        """ Adds a device """
        if MobileDevice is None:
            raise ValueError("Mobile device must be defined.")

        for i in self._devices:
            if i._serial_num == MobileDevice._serial_num:
                return

        self._devices.append(MobileDevice)


    def remove_device(self, serial_num):
        """ Removes an device """
        MobileDevice._validate_string_input(MobileDevice.SERIAL_NUM_LABEL, serial_num)

        for i in self._devices:
            if i.get_serial_num() == serial_num:
                self._devices.remove(i)
                return


    def get_device(self, serial_num):
        """ Gets an device given the serial number """
        MobileDevice._validate_string_input(MobileDevice.SERIAL_NUM_LABEL, serial_num)

        for i in self._devices:
            if i.get_serial_num() == serial_num:
                return i

        return None


    def device_exists(self, serial_num):
        """ Checks if an device exists """
        MobileDevice._validate_string_input(MobileDevice.SEERIAL_NUM_LABEL, serial_num)

        for i in self._devices:
            if i.get_serial_num() == serial_num:
                return True

        return False


    def get_store_name(self):
        """ Returns the name of store """

        return self._store_name


    def get_repair_stats(self):
        """ Returns details of the inventory of mobile devices in for repair """
        completed_count = 0
        pending_count = len(self._devices)
        profit_sum = 0.0

        for device in self._devices:
            if device.is_complete():
                completed_count = completed_count + 1
            profit_sum = profit_sum + device.calc_profit()

        pending_count = pending_count - completed_count
        stats = RepairStats(pending_count, completed_count, profit_sum)

        return stats


    @classmethod
    def _validate_string_input(cls, display_name, str_value):
        """ Private helper to validate string values """
        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")
