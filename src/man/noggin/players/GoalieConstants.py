from .. import NogginConstants as NogCon

BALL_SAVE_LIMIT_TIME = 2.5
MOVE_TO_SAVE_DIST_THRESH = 200.
CENTER_SAVE_THRESH = 15
ORTHO_GOTO_THRESH = Constants.CENTER_FIELD_X * 0.5
STRAFE_ONLY = True
STRAFE_SPEED = 0.3
STRAFE_STEPS = 3
MAX_FRAMES_OFF_CENTER = 360
MAX_STEPS_OFF_CENTER = 50
BUFFER = 50
STRAFE_THRESH_ONE = 10
STRAFE_THRESH_TWO = 15
STRAFE_THRESH_THREE = 25
STRAFE_THRESH_FOUR = 35
STRAFE_THRESH_FIVE = 45
STRAFE_THRESH_SIX = 55
STRAFE_THESH_SEVEN = 65

AGGRESSIVENESS_OFFSET_X = 100
AGGRESSIVENESS_OFFSET_Y = 15
SAVE_OFFSET_X = 50
GOALBOX_Y_REDUCTION = 20
END_CLEAR_BUFFER = 10



# Distance at which we use active localization
ACTIVE_LOC_THRESH = 150.

# Difference to goto a different point
SHOULD_POSITION_DIFF = 5.0

CHASE_FROM_SQUAT_DIST = 55.0
CHASE_FROM_SQUAT_BEARING = 70.0
CHASE_FROM_SQUAT_VEL = 4.0

START_CHASE_BUFFER = 3
STOP_CHASE_BUFFER = 3


#Dani

#Buffer for size of the goalie box so that the
#Goalie will clear a ball in his box
BOX_BUFFER = 15
CHASE_RIGHT_X_LIMIT = NogCon.MY_GOABOX_RIGHT_X + 70
CHASE_LEFT__X_LIMIT = NogCon.MY_GOALBOX_LEFT_X - 7
CHASE_UPPER_Y_LIMIT = NogCon.FIELD_HEIGHT + 10
CHASE_LOWER_Y_LIMIT = 0 - 10

CLOSE_BEHIND_GOALIE = -10
