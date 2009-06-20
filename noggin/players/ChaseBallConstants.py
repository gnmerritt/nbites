# Component Switches
USE_LOC_CHASE = False

# Transitions' Constants
# Ball on and off frame thresholds
BALL_ON_THRESH = 2
BALL_OFF_THRESH = 20
# Value to stop spinning to ball and approach
BALL_APPROACH_BEARING_THRESH = 30
# Value to start spinning to ball
BALL_APPROACH_BEARING_OFF_THRESH = 40
# Should position for kick
BALL_POS_KICK_DIST_THRESH = 15.0
BALL_POS_KICK_BEARING_THRESH = 30

# States' constants
# turnToBall
FIND_BALL_SPIN_SPEED = 25.0
BALL_SPIN_SPEED = 25.0
BALL_SPIN_GAIN = 0.9
MIN_BALL_SPIN_SPEED = 5

# approachBall() values
APPROACH_X_GAIN = 0.15
APPROACH_SPIN_SPEED = 10
MIN_APPROACH_SPIN_SPEED = 10
APPROACH_SPIN_GAIN = 1.1
MAX_APPROACH_X_SPEED = 11.0
MIN_APPROACH_X_SPEED = -11.0

# positionForKick() values
BALL_KICK_LEFT_Y_L = 10
BALL_KICK_RIGHT_Y_R = -BALL_KICK_LEFT_Y_L
BALL_KICK_LEFT_Y_R = 6
BALL_KICK_LEFT_X_CLOSE = 2
BALL_KICK_LEFT_X_FAR = 14
POSITION_FOR_KICK_DIST_THRESH = 5
POSITION_FOR_KICK_BEARING_THRESH = 15


# Values for controlling the strafing
PFK_MAX_Y_SPEED = 6.0
PFK_MIN_Y_SPEED = -PFK_MAX_Y_SPEED
PFK_MAX_X_SPEED = 4.0
PFK_MIN_X_SPEED = 0.0
PFK_MIN_Y_MAGNITUDE = 1.5
PFK_Y_GAIN = 0.7

# Keep track of what gait we're using
FAST_GAIT = "fastGait"
NORMAL_GAIT = "normalGait"

# Obstacle avoidance stuff
AVOID_OBSTACLE_FRONT_DIST = 40.0 #cm
AVOID_OBSTACLE_SIDE_DIST = 30.0 #cm
AVOID_OBSTACLE_FRAMES_THRESH = 2
DONE_AVOIDING_FRAMES_THRESH = 25
DODGE_BACK_SPEED = -3.0 # cm/s
DODGE_RIGHT_SPEED = -6.0 # cm/s
DODGE_LEFT_SPEED = 6.0 # cm/s

ORBIT_BALL_STEP_FRAMES = 150

TURN_LEFT = 1
TURN_RIGHT = -1

CHASE_AFTER_KICK_FRAMES = 100
