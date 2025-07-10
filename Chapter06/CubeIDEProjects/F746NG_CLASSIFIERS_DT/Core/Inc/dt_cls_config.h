#ifndef DT_CLS_CONFIG_H_INCLUDED
#define DT_CLS_CONFIG_H_INCLUDED
#define NUM_NODES 285
#define NUM_FEATURES 2
#define NUM_CLASSES 2
extern const int LEFT_CHILDREN[NUM_NODES];
extern const int RIGHT_CHILDREN[NUM_NODES];
extern const int SPLIT_FEATURE[NUM_NODES];
extern const float THRESHOLDS[NUM_NODES];
extern const int VALUES[NUM_NODES][NUM_CLASSES];
#endif
