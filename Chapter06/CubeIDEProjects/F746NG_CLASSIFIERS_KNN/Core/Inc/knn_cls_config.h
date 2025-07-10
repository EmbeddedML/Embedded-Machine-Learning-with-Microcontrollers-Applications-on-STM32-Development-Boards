#ifndef KNN_CLS_CONFIG_H_INCLUDED
#define KNN_CLS_CONFIG_H_INCLUDED
#define NUM_CLASSES 2
#define NUM_NEIGHBORS 5
#define NUM_FEATURES 2
#define NUM_SAMPLES 1600
extern char* LABELS[NUM_CLASSES];
extern const float DATA[NUM_SAMPLES][NUM_FEATURES];
extern const int DATA_LABELS[NUM_SAMPLES];
#endif