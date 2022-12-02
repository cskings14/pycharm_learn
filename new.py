
def squared(a):
    return (a * a )


print(squared(4))

class oof:
    def __init__(self, oof):
        self.oof = oof


    def student_info(self, *args, **kwargs):
        print(args)  # positional arguments
        print(kwargs)  # keyword arguments

courses = ['Math', 'Art']
info = {'name': 'Jon', 'age': 22}

oof('h').student_info(*courses, **info)





