class RepairStats:
    """ Statistics on a Mobile Device Repair Shop Inventory """

    def __init__(self, num_pending_repairs, num_completed_repairs, total_profit, num_phones, num_tablets):
        """ Initialize the data values """

        if num_pending_repairs is None or type(num_pending_repairs) != int:
            raise ValueError("Invalid pending repairs value")
        self._num_pending_repairs = num_pending_repairs

        if num_completed_repairs is None or type(num_completed_repairs) != int:
            raise ValueError("Invalid completed repairs value")
        self._num_completed_repairs = num_completed_repairs

        if total_profit is None or type(total_profit) != float:
            raise ValueError("Invalid repairs profit")
        self._total_profit = total_profit

        if num_phones is None or type(num_phones) != int:
            raise ValueError("Invalid Phone number value")
        self._num_phones = num_phones

        if num_tablets is None or type (num_tablets) != int:
            raise ValueError("Invalid Tablet number value")
        self._num_tablets = num_tablets


    def get_num_pending_repairs(self):
        """ Returns the number of pending repairs """
        return self._num_pending_repairs

    def get_num_completed_repairs(self):
        """ Returns the number of completed repairs """
        return self._num_completed_repairs

    def get_total_profit(self):
        """ Returns the total profit for all the completed repairs """
        return self._total_profit

    def get_num_phones(self):
        """Returns the number of phones"""
        return self._num_phones

    def get_num_tablets(self):
        """Return the number of Tablets"""
        return self._num_tablets