class AbstractMobileDevice:
    """ AbstractMobileDevice class """

    MAKE_LABEL = "Make"
    MODEL_LABEL = "Model"
    STORAGE_LABEL = "Storage"
    PROBLEM_LABEL = "Problem"
    DATE_RECEIVED_LABEL = "Date Received"
    SERIAL_NUM_LABEL = "Serial Number"


    def __init__(self, make, model, storage, problem, date_received, serial_num):
        """ Constructor - Initializes the main attributes of a AbstractMobileDevice """

        AbstractMobileDevice._validate_string_input(AbstractMobileDevice.MAKE_LABEL, make)
        self._make = make

        AbstractMobileDevice._validate_string_input(AbstractMobileDevice.MODEL_LABEL, model)
        self._model = model

        AbstractMobileDevice._validate_string_input(AbstractMobileDevice.STORAGE_LABEL, storage)
        self._storage = storage

        AbstractMobileDevice._validate_string_input(AbstractMobileDevice.PROBLEM_LABEL, problem)
        self._problem = problem

        AbstractMobileDevice._validate_string_input(AbstractMobileDevice.DATE_RECEIVED_LABEL, date_received)
        self._date_received = date_received

        AbstractMobileDevice._validate_string_input(AbstractMobileDevice.SERIAL_NUM_LABEL, serial_num)
        self._serial_num = serial_num

        self._is_completed = False
        self._price = 0
        self._date_repaired = None
        self._cost = 0

    def get_price(self):
        """ return repair price for the mobile device """

        return self._price


    def set_price(self, repair_price:float):
        """ set repair price for the mobile device """
        AbstractMobileDevice._validate_string_input('Reair price', repair_price)
        if type(repair_price) is not float:
            raise ValueError("Repair price must be a float.")

        self._price = repair_price


    def complete_repair(self, cost:float):
        """ set repair completion date for the mobile device """

        AbstractMobileDevice._validate_string_input('Cost', cost)
        self._is_completed = True
        self._cost = cost


    def get_details(self):
        """ return mobile device details """

        raise NotImplementedError("Child class must implement method")
        # if self._is_completed:
        #     return self._make + ' ' + self._model + ' with ' + self._storage + ' of storage with ' + self._problem + ' received on ' + str(self._date_received) + ' (Repaired on ' + str(self._date_repaired) + ' for $' + str(self._price) + ')'

        # return self._make + ' ' + self._model + ' with ' + self._storage + ' of storage with ' + self._problem + ' received on ' + str(self._date_received) + ' (Repair price would be $' + str(self._price) + ')'


    def get_type(self):
        """ get the type of the device"""

        raise NotImplementedError("Child class must implement method")

    def get_serial_num(self):
        """ return serial number fo the mobile device"""

        return self._serial_num

    
    def is_complete(self):
        """ return true mobile device has been repaired"""

        return self._is_completed


    def calc_profit(self):
        """  return the profit of the fixing the mobile device"""
        return self._price - self._cost


    @classmethod
    def _validate_string_input(cls, display_name, str_value):
        """ Private helper to validate string values """

        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")




