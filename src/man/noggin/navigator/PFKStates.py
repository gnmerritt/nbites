from man.noggin.util import MyMath
from . import WalkHelper as walker
from . import NavHelper as helper
from . import NavConstants as constants
from . import BrunswickSpeeds as speeds
from math import fabs

# Values for controlling the speeds
PFK_LEFT_SPIN_SPEED = speeds.LEFT_SPIN_WHILE_X_MAX_SPEED
PFK_RIGHT_SPIN_SPEED = speeds.RIGHT_SPIN_WHILE_X_MAX_SPEED
PFK_LEFT_SPEED = speeds.OMNI_LEFT_MAX_SPEED
PFK_RIGHT_SPEED = speeds.OMNI_RIGHT_MAX_SPEED
PFK_FWD_SPEED = speeds.OMNI_FWD_MAX_SPEED
PFK_REV_SPEED = speeds.OMNI_REV_MAX_SPEED
PFK_MIN_Y_MAGNITUDE = speeds.MIN_OMNI_Y_MAGNITUDE
PFK_MIN_X_MAGNITUDE = speeds.MIN_OMNI_X_MAGNITUDE
PFK_MIN_SPIN_MAGNITUDE = speeds.MIN_SPIN_WHILE_X_MAGNITUDE

# Buffering values, insure that we eventually kick the ball
PFK_CLOSE_ENOUGH_X = 2.7
PFK_CLOSE_ENOUGH_Y = 2.7
PFK_CLOSE_ENOUGH_THETA = 11



def positionForKick(nav):
    """
    This state is called by player through Navigator::kickPosition(kick)
    It will position the robot at the ball using self.kick to determine the x,y
    offset and the final heading.

    This state will aggresively omni-walk, so it's probably best if we don't call
    it until we're near the ball.
    """
    ball = nav.brain.ball

    # we've either just started, or are close to our last destination
    # tell the robot where to go!
    if nav.firstFrame():
        nav.destX = ball.relX - nav.kick.x_offset - 3
        nav.destY = ball.relY - nav.kick.y_offset

        # @TODO check if rotating the other way is quicker?
        # wait for heading to actually be there
        #nav.destTheta = nav.brain.my.h

        nav.destTheta = 0 # temporary!

        nav.newDestination = True

        print 'Set new PFK destination of ({0},{1},{2})' \
              .format(nav.destX, nav.destY, nav.destTheta)

        return nav.goNow('destWalking')

