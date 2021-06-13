from abstract_mobile_device import AbstractMobileDevice


class Tablet(AbstractMobileDevice):
    """ Model a Tablet Device """

    external_keyboard_LABEL = "external_keyboard"
    Tablet_TYPE = "Tablet"

    def __init__(self, serial_num, make, model, storage, problem, price, external_keyboard, date_received):
        """ Initialize the Tablet """
        super().__init__(serial_num, make, model, storage, problem, date_received)

        AbstractMobileDevice._validate_string_input(Tablet.external_keyboard_LABEL, external_keyboard)
        self._external_keyboard = external_keyboard


    def get_details(self):
        """Return the details  of the Tablet """
        detail = ""
        if self._is_completed:
            detail = f'{self._serial_num} {self._make} {self._model} with {str(self._storage)} GB of storage with a {self._problem} received on {self._date_received} with external_keyboard {self._external_keyboard} (Repaired on {self._date_repaired})'

            if self._external_keyboard:
                detail = f'{self._serial_num} {self._make} {self._model} with {str(self._storage)} GB of storage with a {self._problem} received on {self._date_received} with external_keyboard {self._external_keyboard} (Repaired on {self._date_repaired})'

            else:
                detail = f'{self._serial_num} {self._make} {self._model} with {str(self._storage)} GB of storage with a {self._problem} received on {self._date_received} without external_keyboard {self._external_keyboard} (Repaired on {self._date_repaired})'



        else:
            if self._external_keyboard:
                detail = f'{self._serial_num} {self._make} {self._model} with {str(self._storage)} GB of storage with a {self._problem} received on {self._date_received} with external_keyboard {self._external_keyboard} (Repaired on {self._date_repaired})'

            else:
                detail = f'{self._serial_num} {self._make} {self._model} with {str(self._storage)} GB of storage with a {self._problem} received on {self._date_received} without external_keyboard {self._external_keyboard} (Repaired on {self._date_repaired})'


        return detail


    def get_type(self):
        """Return the type of device """
        return Tablet.Tablet_TYPE


myTablet = Tablet("ser356832", "Apple", "iTablet 11", "512GB", "battary issue", "CAD2", True, "2021-05-02")
myTablet.set_price(60.5)
myTablet.complete_repair(50.5)
print(myTablet.get_details())

        

