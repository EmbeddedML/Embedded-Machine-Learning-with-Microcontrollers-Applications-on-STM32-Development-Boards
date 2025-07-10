/*
 * lib_bayes.c
 *
 *  Created on: Oct 6, 2023
 *     Authors: Berkan Höke, Eren Atmaca
 */

#include "bayes_cls_inference.h"


int8_t bayes_cls_predict(arm_matrix_instance_f32 *input, arm_matrix_instance_f32 *output)
{
	// Returns probabilities of the classes using Bayes Classifier

	int8_t status = ARM_MATH_SUCCESS;

	float32_t __input_T[NUM_FEATURES * 1];
	float32_t __zero_mean[NUM_FEATURES * 1];
	float32_t __zero_mean_T[NUM_FEATURES * 1];
	float32_t __prod;
	float32_t __xt_invCov[NUM_FEATURES * 1];
	arm_matrix_instance_f32 mu, invCov;
	arm_matrix_instance_f32 input_T = {.numRows = 1, .numCols = NUM_FEATURES, .pData = __input_T};
	arm_matrix_instance_f32 zero_mean = {.numRows = NUM_FEATURES, .numCols = 1, .pData = __zero_mean};
	arm_matrix_instance_f32 zero_mean_T = {.numRows = 1, .numCols = NUM_FEATURES, .pData = __zero_mean_T};
	arm_matrix_instance_f32 xt_invCov = {.numRows = 1, .numCols = NUM_FEATURES, .pData = __xt_invCov};
#if (CASE == 3)
	float32_t __mu_T[NUM_FEATURES * 1];
	float32_t __xt_invCov_x;
	float32_t __invCov_mu[NUM_FEATURES * 1];
	float32_t __invCov_mu_T[NUM_FEATURES * 1];
	float32_t __invCov_mu_x;
	float32_t __mu_invCov_mu;
	arm_matrix_instance_f32 mu_T = {.numRows = 1, .numCols = NUM_FEATURES, .pData = __mu_T};
	arm_matrix_instance_f32 xt_invCov_x = {.numRows = 1, .numCols = 1, .pData = &__xt_invCov_x};
	arm_matrix_instance_f32 invCov_mu = {.numRows = NUM_FEATURES, .numCols = 1, .pData = __invCov_mu};
	arm_matrix_instance_f32 invCov_mu_T = {.numRows = 1, .numCols = NUM_FEATURES, .pData = __invCov_mu_T};
	arm_matrix_instance_f32 invCov_mu_x = {.numRows = 1, .numCols = 1, .pData = &__invCov_mu_x};
	arm_matrix_instance_f32 mu_invCov_mu = {.numRows = 1, .numCols = 1, .pData = &__mu_invCov_mu};
#endif
	arm_matrix_instance_f32 prod = {.numRows = 1, .numCols = 1, .pData = &__prod};

	status = arm_mat_trans_f32(input, &input_T);

	float discr[NUM_CLASSES] = {0};
	for (int cls = 0; cls < NUM_CLASSES; cls++)
	{
		mu.pData = &MEANS[cls][0];
		mu.numRows = NUM_FEATURES;
		mu.numCols = 1;
		float prior = logf(CLASS_PRIORS[cls]);


#if (CASE == 1)
		status += arm_mat_sub_f32(input, &mu, &zero_mean);
		status += arm_mat_trans_f32(&zero_mean, &zero_mean_T);
		status += arm_mat_mult_f32(&zero_mean_T, &zero_mean, &prod);
		discr[cls] = prior - prod.pData[0] / (2 * sigma_sq);
#elif (CASE == 2)
		status += arm_mat_sub_f32(input, &mu, &zero_mean);
		status += arm_mat_trans_f32(&zero_mean, &zero_mean_T);
		invCov.pData = &INV_COV[0][0];
		invCov.numRows = NUM_FEATURES;
		invCov.numCols = NUM_FEATURES;
		status += arm_mat_mult_f32(&zero_mean_T, &invCov, &xt_invCov);
		status += arm_mat_mult_f32(&xt_invCov, &zero_mean, &prod);
		discr[cls] = prior - prod.pData[0] * 0.5;
#elif (CASE == 3)
		invCov.pData = &INV_COVS[cls];
		invCov.numRows = NUM_FEATURES;
		invCov.numCols = NUM_FEATURES;

		status += arm_mat_mult_f32(&input_T, &invCov, &xt_invCov);
		status += arm_mat_mult_f32(&xt_invCov, input, &xt_invCov_x);

		xt_invCov_x.pData[0] = xt_invCov_x.pData[0] * (-0.5f);

		status += arm_mat_mult_f32(&invCov, &mu, &invCov_mu);
		status += arm_mat_trans_f32(&invCov_mu, &invCov_mu_T);
		status += arm_mat_mult_f32(&invCov_mu_T, input, &invCov_mu_x);
		status += arm_mat_trans_f32(&mu, &mu_T);
		status += arm_mat_mult_f32(&mu_T, &invCov_mu, &mu_invCov_mu);

		// mu_invCov_mu.pData[0] = mu_invCov_mu.pData[0] * (-0.5f);

		float log_det = logf(DETS[cls]) * (-0.5f);

		discr[cls] = xt_invCov_x.pData[0] + invCov_mu_x.pData[0] - 0.5f * mu_invCov_mu.pData[0] + log_det + prior;
#endif
	}
	memcpy(output->pData, discr, sizeof(float32_t) * NUM_CLASSES);
	output->numCols = NUM_CLASSES;
	output->numRows = 1;
	return status;
}
