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
        # Fun versus frustration
        self._funFrus = 5
        self._funFrusThres = 5.5

        # Boredom versus excitement
        self._boredExci = 5
        self._boredExciThres = 5.5

        # Fearfulness versus Relaxedness
