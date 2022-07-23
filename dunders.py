class MyInt(int):

    def __add__(self, other):
        return int(str(self) + str(other))


my_int = MyInt(10)

my_int2 = MyInt(20)

new = my_int + my_int2

# print(new)
#
# print(type(new))


class Clock:

    _SECONDS_IN_DAY = 24 * 60 * 60

    def __init__(self, seconds: int):
        self._seconds = seconds % self._SECONDS_IN_DAY

    def get_time_format(self):
        seconds = self._seconds % 60
        minutes = (self._seconds // 60) % 60
        hours = (self._seconds // 3600) % 24
        return '{hours}:{minutes}:{seconds}'.format(
            hours=self.get_format(hours),
            minutes=self.get_format(minutes),
            seconds=self.get_format(seconds))

    @staticmethod
    def get_format(value):
        return str(value) if value > 9 else '0' + str(value)

    def __format__(self, format_spec):
        return str(format_spec) if format_spec > 9 else '0' + str(format_spec)

    def __iadd__(self, other):
        self._seconds += other._seconds
        return self

    def __isub__(self, other):
        self._seconds -= other._seconds
        return self

    def __eq__(self, other):
        return self._seconds == other._seconds

    def __ne__(self, other):
        return not self.__eq__(other)

    def __int__(self):
        ...


clock1 = Clock(300)
print(clock1.get_time_format())

clock2 = Clock(200)

clock1 += clock2

print(clock1.get_time_format())

print(clock2.get_time_format())
clock2 -= clock1

print(clock2.get_time_format())

print(clock1 == clock2)
print(clock1 != clock2)
int(clock1)

