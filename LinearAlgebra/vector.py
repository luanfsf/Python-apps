from math import hypot, sqrt
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def addition(self, vetor):
        if ( len(self.coordinates) == len(vetor) ):
            self.coordinates = [x+y for x,y in zip(self.coordinates,vetor)]
        return

    def subtraction(self,vetor):
        if ( len(self.coordinates) == len(vetor) ):
            self.coordinates = [x-y for x,y in zip(self.coordinates,vetor)]
        return

    def scalarMultiplication(self,scalar):
        self.coordinates = [x*scalar for x in (self.coordinates)]
        return

    def magnitude(self):
        return sqrt(sum( [x**2 for x in self.coordinates] ))

    def normalization(self):
        return [x/self.magnitude() for x in self.coordinates]
