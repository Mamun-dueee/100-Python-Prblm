class S:
    nInstances = 0
    def __init__(self):
        S.nInstances += 1

    @staticmethod
    def howManyInstances():
        print('Number of instances created: ', S.nInstances)
