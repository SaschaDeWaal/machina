# Machina

A robot game



### Emotion system

Each robot has one parameter called `arousal` (1 - 10). All behaviors state should take this variable in count.



**To keep in mind:**

1. ****We should create a DriverState, which will be the parent of all states that needs movement. The drive style of the robot should match the `arousal` level



### Todo:

- [ ] Add sound
- [ ] Emotion system / refactor
- [ ] Program should automatic start when the pi is turned on
- [ ] DriverState base can be created (turnDegrees(degrees), driveTowards(relative position)) 
- [ ] Object detection should work with the behavior program (subprocess)

### Behavior's todo:

- [ ] ReturnToBaseState: turn around on the spot (or wandering behaviour) until own base is seen.
    Drive towards that point until the robot is close to snow.
    At that point, check left and right to see whether there's a clear way.
     If so, turn that way. If not, randomly go left or right for some time, then turn back the other way to face the base.  Rinse and repeat. Go to Remove Snow
- [ ] RemoveSnowState: Turn around until snow is seen;
  IMPORTANT to take into account the angle at which the base center was seen, and the amount of degrees turned since it started looking for snow
   If base is out of sight, start moving toward the snow to push it for X seconds. After that, drive backward towards the base for either X seconds, or X-Y seconds (randomize the amount of Y?) Rinse and Repeat Go to SeekBaseState after either not finding snow or after some amount of time spent removing snow
  SeekBaseState: turn around on the spot (or wandering behaviour) until the base of a different team is seen. Move towards that base until it is within some distance. Move to the AttackBaseState
- [ ] AttackBaseState: turn around till it sees snow
  IMPORTANT to take into account the angle X at which the base center was seen, and the amount of degrees turned since it started looking for snow Take into account the angle Y at which snow is seen.
  Turn around Z degrees further from the snow in the same direction
  Drive for a small time to end up behind the snow.
  Turn back Y+Z degrees to align the robot's facing with the base.
  Push snow into the base for some seconds or until the gyroscope picks up deacceleration
  Drive back for the same amount of seconds, and either go in ReturnToBaseState or repeat AttackBase State.
- [ ] BeingPetState: A player can grab the robot and start petting it. This state should always be enable to start. So we should a event in the base state that checkts if it is grabbed. This will make the robot more arousal. When putting down, the robot makes a small dance/animation 
- [ ] BeingShakedState: A player can shake the robot. This will make the robot less efficient.  After putting down, the robot should drive drunk around (wonder around)
- [ ] BatteryLowState: When the battery is almost empty, the robot should show this to the user until it is connected to the charger. 
- [ ] BeingChargedState: A indle state while the robot is charged. When fully charged, the robot should give a signal.
- [ ] AngryState: When the efficient score is too low, its should wonder around and hit other robots. 