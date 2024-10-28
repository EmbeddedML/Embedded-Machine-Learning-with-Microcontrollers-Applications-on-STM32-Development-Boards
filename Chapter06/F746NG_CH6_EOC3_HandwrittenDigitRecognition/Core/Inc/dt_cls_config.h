#ifndef HDR_DT_CONFIG_H_INCLUDED
#define HDR_DT_CONFIG_H_INCLUDED
#define NUM_NODES 1415
#define NUM_FEATURES 7
#define NUM_CLASSES 10
extern const int LEFT_CHILDREN[NUM_NODES];
extern const int RIGHT_CHILDREN[NUM_NODES];
extern const int SPLIT_FEATURE[NUM_NODES];
extern const float THRESHOLDS[NUM_NODES];
extern const int VALUES[NUM_NODES][NUM_CLASSES];
#endif
