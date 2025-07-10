#ifndef DT_REG_CONFIG_H_INCLUDED
#define DT_REG_CONFIG_H_INCLUDED
#define NUM_FEATURES 1
#define NUM_NODES 399
extern const int LEFT_CHILDREN[NUM_NODES];
extern const int RIGHT_CHILDREN[NUM_NODES];
extern const int SPLIT_FEATURE[NUM_NODES];
extern const float THRESHOLDS[NUM_NODES];
extern const float VALUES[NUM_NODES];
#endif