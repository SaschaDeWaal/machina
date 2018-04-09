import numpy

"""

This class takes care of all the internal behaviour.
The behavioural parameters are taken care of in this file,
as well as how they're changed.

"""

class InternalBehaviour:

    """
    The __init__ function sets the base values of the behavioural parameters.
    These parameters are used in order to determine the various aspects of the robot's emotional state.
    The parameters should range from 0 to 10, and are accompanied by a separate threshold value that indicates
    when the 'switch' between the positive and negative end of the emotion should occur.

    It also sets values for the 'wishes' parameters. These are to be multiplied by sensor output in order to determine
    the effect that certain interactions by the users have on the robot. Wishes can be positive and negative, to allow
    a like or dislike for some particular action. They're supposed to have a value between -2 and 2 to indicate for
    both a high and mild (dis)like.
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


        # Wish parameters. Can be added/removed/changed as necessary.
        self._touchPreference = 0 # how robot reacts to being touched
        self.touchBorder = 0.5    # amount of touch needed for robot to start disliking it.
        self._lightPreference = 0 # how much the robot likes to be in bright places

        self._isBeingPetted = False     # Whether robot is being petted, depends on light sensor input
        self._isInDarkness = False      # Whether robot currently is in a dark area
        self._isLifted = False          # whether robot is being lifted by someone
        self._isHit = False             # Whether robot is receiving an uppercut, noted by a sudden acceleration
                                        # and speed increase in the gyroscope
        self._hasCollided = False       # Whether robot has collided with something, noted by a sudden acceleration
                                        # and speed decrease in the gyroscope
        self._gyroscope = [0,0,0,0,0,0] # 6 numbers; 3 for acceleration in x,y,z direction, and gyroscope for balance



    """
    Function that take in the sensor output from light detector and changes the appropriate values depending on lightPreference
    """
    def LightEffect(self, lightInput):
        self._fearCalm += lightInput * self._lightPreference

    """
    Function that take in the sensor output from light detector,
    """
    def TouchEffect(self):
        if self._isBeingPetted:
            self._funFrus += self._touchPreference

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




