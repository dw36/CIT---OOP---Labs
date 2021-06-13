from abstract_mobile_device import AbstractMobileDevice


class Phone(AbstractMobileDevice):
    """ Model a Phone Device """

    CARRIER_LABEL = "Carrier"
    PHONE_TYPE = "phone"

    def __init__(self, serial_num, make, model, storage, problem, price, carrier, date_received):
        """ Initialize the Phone """
        super().__init__(make, model, storage, problem, date_received, serial_num)

        AbstractMobileDevice._validate_string_input(Phone.CARRIER_LABEL, carrier)
        self._carrier = carrier


    def get_details(self):
        """Return the details  of the Phone """
        detail = ""
        if self._is_completed:
            detail = f'{self._make} {self._model} with {str(self._storage)} GB of storage with a "{self._problem}"'
            f' received on {self._date_received} with carrier {self._carrier} (Repaired on {self._date_repaired})'
            
            





        else:
            detail = f'{self._make} {self._model} with {str(self._storage)} GB of storage with a "{self._problem}"'\
            f' received on {self._date_received} with carrier {self._carrier}.'

        return detail


    def get_type(self):
        """Return the type of device """
        return Phone.PHONE_TYPE


myPhone = Phone("ser356832", "Apple", "iPhone 11", "512GB", "battary issue", "CAD2", "Free", "2021-05-02")
myPhone.set_price(60.5)
myPhone.complete_repair(50.5)
print(myPhone.get_details())

        

