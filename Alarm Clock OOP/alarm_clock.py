class AlarmClock:
    def __init__(self):
        self.current_time = ''
        self.alarm_on_off = ''
        self.alarm_time = ''

    def set_current_time (self):
        self.current_time = input('Please set the current time. ')
        print(f'The clock is currently set to {self.current_time}')

    def alarm_switch (self):
        self.alarm_on_off = input('Please type out whether to turn the alarm on or off. ')
        if (self.alarm_on_off.lower() == 'on'):
            print('The alarm is on.')
        else:
            print('The alarm is off.')
            
    def set_alarm_time (self):
        self.alarm_time = input('Please set the time for the alarm. ')
        print(f'The alarm is set for {self.alarm_time}')
