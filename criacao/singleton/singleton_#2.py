def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)

        return instances


@singleton
class AppSettings:
    def __init__(self):
        self.tema = 'Dark'
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()
    as2 = AppSettings()
