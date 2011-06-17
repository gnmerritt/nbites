#ifndef BALL_MONITOR_H
#definte BALL_MONITOR_H




#include "BulkMonitor.h"
#include "Ball.h"
#include "BallEKF.h"


class BallMonitor
{
public:

    BallMonitor();
    ~BallMonitor();

    double update(int sensor, double input);

    void Reset();
    void LogOutput();

private:
    BulkMonitor* monitor;


#endif
