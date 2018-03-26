"""

This class takes care of all the internal behaviour.
The behavioural parameters are taken care of in this file,
as well as how they're changed.

"""

import ExternalBehaviour

class InternalBehaviour:

    """
    The __init__ function sets the base values of the behavioural parameters.
    These parameters are used in order to determine the various aspects of the robot's emotional state.
    The parameters should range from 0 to 10, and are accompanied by a separate threshold value that indicates
    when the 'switch' between the positive and negative end of the emotion should occur.
    """
    def __init__(self):
        # Fun versus Frustration
        self._funFrus = 5
        self._funFrusThres = 5.5

        # Boredom versus Excitement
        self._boredExci = 5
        self._boredExciThres = 5.5

<<<<<<< HEAD
        # Fearfulness versus Relaxedness


=======
        # Fearfulness versus Calmness
        self._fearCalm = 5
        self._fearCalmThres = 5.5

        # Contendedness versus Jealousy
        self._contJeal = 5
        self._contJealThres = 5.5
>>>>>>> 3a8f712acaba4ea7a3b2bc2d2d3865a6ac962dfc
