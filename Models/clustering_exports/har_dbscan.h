#ifndef HAR_DBSCAN_H_INCLUDED
#define HAR_DBSCAN_H_INCLUDED
#define NUM_CORE_POINTS 16084
#define NUM_FEATURES 10
#define NUM_CLUSTERS 80
#define EPS 8
extern const float CORE_POINTS[NUM_CORE_POINTS][NUM_FEATURES];
extern const int labels[NUM_CORE_POINTS];
#endif