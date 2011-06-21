#include "BallMonitor.h"
#include <string>

static const int NUM_MONITORS = 7;

// names of different sensors (for variance monitoring)
const std::string sensorNames[] = {
    "ballX", "ballY", "ballDist", "ekfX", "ekfY", "velX", "velY"
};


BallMonitor::BallMonitor()
    : monitor(BulkMonitor(NUM_MONITORS,"BallMonitor", sensorNames[]))
{

}

void Reset()
{
    monitor.Reset();
}

void LogOutput()
{
    monitor.LogOutput();
}

double update(float x, float y, float dist)
{
    int i = 0;
    monitor.update(i, x);
    monitor.update(++i, y);
    monitor.update(++i, dist);
}

double update(float x, float y, float velx, float vely)
{
    int i = 3;
    monitor.update(i, x);
    monitor.update(++i, y);
    monitor.update(++i, velx);
    monitor.update(++i, vely)

}

