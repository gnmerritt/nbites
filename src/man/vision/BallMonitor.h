#ifndef BALL_MONITOR_H
#define BALL_MONITOR_H

#include "BulkMonitor.h"

class BallMonitor
{
public:

    BallMonitor();

    void update(float x, float y, float dist);
    void update(float x, float y, float velx, float vely);

    void Reset();
    void LogOutput();

private:
    BulkMonitor monitor;

};

#endif
