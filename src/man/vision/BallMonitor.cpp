#include "BallMonitor.h"
#include <string>


static const int NUM_MONITORS = 7;

// names of different sensors (for variance monitoring)
const std::string sensorNames[NUM_MONITORS] = {
    "ballX", "ballY", "ballDist", "ekfX", "ekfY", "velX", "velY"
};


BallMonitor::BallMonitor()
    : monitor(NUM_MONITORS,"BallMonitor", sensorNames)
{

}

void BallMonitor::Reset()
{
    monitor.Reset();
}

void BallMonitor::LogOutput()
{
    monitor.LogOutput();
}

void BallMonitor::update(float x, float y, float dist)
{
    int i = 0;
    monitor.update(i, x);
    monitor.update(++i, y);
    monitor.update(++i, dist);
}

void BallMonitor::update(float x, float y, float velx, float vely)
{
    int i = 3; // see above
    monitor.update(i, x);
    monitor.update(++i, y);
    monitor.update(++i, velx);
    monitor.update(++i, vely);

}

