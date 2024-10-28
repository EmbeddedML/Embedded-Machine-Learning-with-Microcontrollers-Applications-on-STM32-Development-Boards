#ifndef SVM_MOMENTS_CONFIG_H_INCLUDED
#define SVM_MOMENTS_CONFIG_H_INCLUDED
#define NUM_CLASSES 10
#define NUM_INTERCEPTS 45
#define NUM_FEATURES 7
#define NUM_SV 50770
enum KernelType{
	LINEAR,
	POLY,
	RBF
};
extern const float coeffs[NUM_CLASSES - 1][NUM_SV];
extern const float SV[NUM_SV][NUM_FEATURES];
extern const float intercepts[NUM_INTERCEPTS];
extern const float w_sum[NUM_CLASSES + 1];
extern const float svm_gamma;
extern const float coef0;
extern const int degree;
extern const enum KernelType type;
#endif