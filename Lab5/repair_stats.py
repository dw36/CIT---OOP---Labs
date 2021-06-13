class RepairStats:
    """ Statistics on a Mobile Device Repair Shop Inventory """

    def __init__(self, num_pending_repairs, num_completed_repairs, total_profit):
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


    def get_num_pending_repairs(self):
        """ Returns the number of pending repairs """
        return self._num_pending_repairs

    def get_num_completed_repairs(self):
        """ Returns the number cof completed repairs """
        return self._num_completed_repairs

    def get_total_profit(self):
        """ Returns the total profit for all the completed repairs """
        return self._total_profit
