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

        # Fearfulness versus Calmness
        self._fearCalm = 5
        self._fearCalmThres = 5.5

        # Contendedness versus Jealousy
        self._contJeal = 5
        self._contJealThres = 5.5

    """
    This function is used to provide the name of one of the parameters, and an accompanied value.
    The parameter corresponding to the supplied name is then changed by the value. After this, a function is called
    to make sure the parameter value is limited to be between 0 and 10.
    """
    def ChangeParam(self, paramName, value):
        if paramName == "fun":
            self._funFrus += value
        elif paramName == "bored":
            self._boredExci += value
        elif paramName == "fear":
            self._fearCalm += value
        elif paramName == "contend":
            self._contJeal += value
        self.CapParam(paramName)

    """
    Function that takes a string that is then matched to one of the behavioural parameters.
    Subsequently, it is ensured that value is no higher than 10, and not lower than 0.
    """
    def CapParam(self, paramName):
        if paramName == "fun":
            if self._funFrus > 10:
                self._funFrus = 10
            elif self._funFrus < 0:
                self._funFrus = 0
        elif paramName == "bored":
            if self._boredExci > 10:
                self._boredExci = 10
            elif self._boredExci < 0:
                self._boredExci = 0
        elif paramName == "fear":
            if self._fearCalm > 10:
                self._fearCalm = 10
            elif self._fearCalm < 0:
                self._fearCalm = 0
        elif paramName == "content":
            if self._contJeal > 10:
                self._contJeal = 10
            elif self._contJeal < 0:
                self._contJeal = 0




