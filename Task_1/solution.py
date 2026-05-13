class AirConditioning:
    '''
    The class of a household air conditioner.

    Manages the status (on/off) and the temperature.
    Temperature range: from 0 to 43 degrees Celsius.
    When switching on, the temperature is set to 18°C.
    '''

    def __init__(self) -> None:
        '''
        Initialization of the air conditioner.

        By default, the air conditioner is turned off and 
        the temperature is not set.
        '''
        self.__status = False
        self.__temperature = None

    def __str__(self) -> str:
        '''
        A string representation of the condition of the air conditioner.

        :return: Description of the current state.
        '''
        if not self.__status:
            return 'Кондиционер выключен.'
        else:
            return 'Кондиционер включен. '\
                   f'Температурный режим: {self.__temperature} градусов.'

    @property
    def status(self) -> bool:
        '''
        Get the status of the air conditioner.

        :return: True if enabled, otherwise False.
        '''
        return self.__status

    @status.setter
    def status(self, value: bool) -> None:
        '''
        Setting the status is prohibited directly.

        Use the switch_on() and switch_off() methods.
        '''
        pass

    @property
    def temperature(self) -> int | None:
        '''
        Get the current temperature.

        :return: Temperature in degrees or None 
        if the air conditioner is turned off.
        '''
        return self.__temperature

    @temperature.setter
    def temperature(self, value: int) -> None:
        '''
        Setting the temperature is prohibited directly.

        Use temperature control methods.
        '''
        pass

    def switch_on(self) -> None:
        '''
        Turn on the air conditioner.

        Sets the default temperature to 18°C if the device is currently off.
        '''
        if not self.__status:
            self.__status = True
            self.__temperature = 18

    def switch_off(self) -> None:
        '''
        Turn off the air conditioner.

        The temperature is reset to None if the device is currently on.
        '''
        if self.__status:
            self.__status = False
            self.__temperature = None

    def reset(self) -> None:
        '''
        Reset the air conditioner settings.

        Sets the temperature to 18°C if the air conditioner is turned on.
        '''
        if self.__status:
            self.__temperature = 18

    def get_temperature(self) -> int | None:
        '''
        Get the current temperature.

        :return: Current temperature or None if the device is off.
        '''
        return self.__temperature

    def raise_temperature(self) -> None:
        '''
        Raise the temperature by 1 degree.

        Only works if the air conditioner is on and 
        the temperature is below 43°C.
        '''
        if self.__status:
            if self.__temperature < 43:
                self.__temperature += 1

    def lower_temperature(self) -> None:
        '''
        Lower the temperature by 1 degree.

        Only works if the air conditioner is on and 
        the temperature is above 0°C.
        '''
        if self.__status:
            if self.__temperature > 0:
                self.__temperature -= 1