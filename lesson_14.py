def close(*args, **kwargs):
    print(args)
    print('Door closed')


class WoodDoor:
    # Class attributes
    material = 'Wood'

    def __init__(self, width, height=180):
        # instance attributes
        self.width = width
        self.height = height

        self.color = None
        self.master = None

        self.area = width * height

    @staticmethod
    def open():
        print('Door opened')

    @classmethod
    def paint(cls):
        print(f'{cls} Paint door')

    def __str__(self):
        close(1, 2, 3, 4)
        return f'{self.__class__.__name__}, ' \
               f'width={self.width}, height={self.height} {self.material}'

    def __repr__(self):
        return f'{self.__class__.__name__}, ' \
               f'width={self.width}, height={self.height}'


class CarEngine:

    MIN_CYLINDERS = 4
    MAX_CYLINDERS = 8
    MIN_CAPACITY = 1400
    MAX_CAPACITY = 5200

    def __init__(
            self,
            capacity,
            cylinders,
            idle_rpms=700,
            max_rpms=8000
    ):
        self.capacity = capacity
        self.cylinders = cylinders
        self.idle_rpms = idle_rpms
        self.max_rpms = max_rpms

        self.rpms = self.idle_rpms

    def start(self):
        print(f'Idle rpms {self.idle_rpms}')
        print('Engine starts')

    def stop(self):
        print('Engine stops')

    def accelerate(self):
        self.rpms *= 2
        if self.rpms > self.max_rpms:
            print('Engine over heated')
        print(f'RPMS {self.rpms}')

        return self.rpms


class GasEngine(CarEngine):
    FUEL = 'Gas'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sparks = self.cylinders


class DieselEngine(CarEngine):
    FUEL = 'Diesel'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pump_injector = self.cylinders

    def accelerate(self):
        result = super().accelerate()
        self.rpms /= 1.2
        print(f'RPMS {self.rpms}')
        return result


def main():
    engine = CarEngine(2000, 4)
     # engine.FUEL
    engine = GasEngine(2000, 4, max_rpms=7000)
    engine.start()
    engine.accelerate()
    engine.accelerate()
    engine.accelerate()

    diesel = DieselEngine(3000, 6, max_rpms=5000)
    diesel.start()
    diesel.accelerate()
    diesel.accelerate()

    door_1 = WoodDoor(80)

    door_2 = WoodDoor(80, 200)

    print(door_1.material)
    door_2.material = 'Iron'
    print(door_2.material)
    print(type(door_1))
    # print(type('Hello'))
    door_1.open()

    print(door_1.width)
    print(door_2.open())

    print(door_1.area)
    print(door_1.master)
    print(door_1.material)

    print(door_1)
    print(door_2)
    door_1.width = 80
    door_1.height = 180
    print(door_1.width, door_1.height)
    print(door_1.width * door_1.height)
    print(WoodDoor.open())
    print(door_1.open())


if __name__ == '__main__':
    main()
