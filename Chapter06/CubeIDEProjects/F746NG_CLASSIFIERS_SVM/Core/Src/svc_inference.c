#include <math.h>
#include "svc_inference.h"


#define Malloc(type,n) (type *)malloc((n)*sizeof(type))


static float kernels[NUM_SV] = {0};
static void compute_kernels(float *x);
static void calculate_ovo_scores(float *kernels, float *ovo_confs);
static void calculate_ovr_scores(float *ovo_confs, float *ovr_confs);

static void compute_kernels(float *x)
{
    memset(kernels, 0, sizeof(kernels));
    for (int sv_idx = 0; sv_idx < NUM_SV; sv_idx++)
    {
        float kernel = 0.0;
        for (int feature_idx = 0; feature_idx < NUM_FEATURES; feature_idx++)
        {
            kernel += pow(x[feature_idx] - SV[sv_idx][feature_idx], 2);
        }
        kernels[sv_idx] = exp(-svm_gamma * kernel);
    }
}

static void calculate_ovo_scores(float *kernels, float *ovo_confs)
{
    int idx = 0;
    memcpy(ovo_confs, intercepts, sizeof(float) * NUM_INTERCEPTS);
    for (int m = 0; m < NUM_CLASSES - 1; m++)
    {
        for (int n = m + 1; n < NUM_CLASSES; n++)
        {
            for (int p = w_sum[m]; p < w_sum[m + 1]; p++)
                ovo_confs[idx] += kernels[p] * coeffs[n - 1][p];

            for (int p = w_sum[n]; p < w_sum[n + 1]; p++)
                ovo_confs[idx] += kernels[p] * coeffs[m][p];
            idx++;
        }
    }
}

static void calculate_ovr_scores(float ovo_confs[NUM_INTERCEPTS], float ovr_confs[NUM_CLASSES]){
    int votes[NUM_CLASSES] = {0};
    float sum_of_confs[NUM_CLASSES] = {0};

    int k = 0;
    for (int i = 0; i < NUM_CLASSES; i++){
        for(int j= i+1; j < NUM_CLASSES; j++){
            sum_of_confs[i] += ovo_confs[k];
            sum_of_confs[j] -= ovo_confs[k];
            votes[(ovo_confs[k] > 0) ? i : j] += 1;
            k += 1;
        }
    }
    
    for (int i = 0; i < NUM_CLASSES; i++)
        ovr_confs[i] = votes[i] + sum_of_confs[i] / (3 * (fabs(sum_of_confs[i]) + 1));
}

int findMax(float array[], int *max_idx) {
    float max_val = array[0];
    *max_idx = 0;//MODIFIED
    for (int i = 1; i < NUM_CLASSES; ++i) {
        if (array[i] > max_val) {
            *max_idx = i;
        }
    }
    
    return 0;
}

static void multiclass_probability(int k, float **r, float *p)
{
	int t,j;
	int iter = 0, max_iter=fmax(100,k);
	float **Q=Malloc(float *,k);
	float *Qp=Malloc(float,k);
	float pQp, eps=0.005/k;

	for (t=0;t<k;t++)
	{
		p[t]=1.0/k;  // Valid if k = 1
		Q[t]=Malloc(float,k);
		Q[t][t]=0;
		for (j=0;j<t;j++)
		{
			Q[t][t]+=r[j][t]*r[j][t];
			Q[t][j]=Q[j][t];
		}
		for (j=t+1;j<k;j++)
		{
			Q[t][t]+=r[j][t]*r[j][t];
			Q[t][j]=-r[j][t]*r[t][j];
		}
	}
	for (iter=0;iter<max_iter;iter++)
	{
		// stopping condition, recalculate QP,pQP for numerical accuracy
		pQp=0;
		for (t=0;t<k;t++)
		{
			Qp[t]=0;
			for (j=0;j<k;j++)
				Qp[t]+=Q[t][j]*p[j];
			pQp+=p[t]*Qp[t];
		}
		float max_error=0;
		for (t=0;t<k;t++)
		{
			float error=fabs(Qp[t]-pQp);
			if (error>max_error)
				max_error=error;
		}
		if (max_error<eps) break;

		for (t=0;t<k;t++)
		{
			float diff=(-Qp[t]+pQp)/Q[t][t];
			p[t]+=diff;
			pQp=(pQp+diff*(diff*Q[t][t]+2*Qp[t]))/(1+diff)/(1+diff);
			for (j=0;j<k;j++)
			{
				Qp[j]=(Qp[j]+diff*Q[t][j])/(1+diff);
				p[j]/=(1+diff);
			}
		}
	}
	//if (iter>=max_iter)
		//info("Exceeds max_iter in multiclass_prob\n");
	for(t=0;t<k;t++) free(Q[t]);
	free(Q);
	free(Qp);
}

static float sigmoid_predict(float decision_value, float A, float B)
{
	float fApB = -decision_value*A+B;
	// 1-p used later; avoid catastrophic cancellation
	if (fApB >= 0)
		return exp(-fApB)/(1.0+exp(-fApB));
	else
		return 1.0/(1+exp(fApB)) ;
}

/*model->probA[k] -2.49386353f , model->probB[k]) 0.52703167f*/
float probA[NUM_INTERCEPTS] = {-2.3549002752201886, -4.179415379701203, -1.7161062347859755};
float probB[NUM_INTERCEPTS] = {0.42584277918889, 0.6427246699062157, -0.046707285548392166};
float svm_predict_probability(float *dec_values, float *prob_estimates)
{
	int i;
			int nr_class = NUM_CLASSES;
			//float *dec_values = Malloc(float, nr_class*(nr_class-1)/2);
			//PREFIX(predict_values)(model, x, dec_values, blas_functions);

			float min_prob=1e-7;
			float **pairwise_prob=Malloc(float *,nr_class);
			for(i=0;i<nr_class;i++)
				pairwise_prob[i]=Malloc(float,nr_class);
			int k=0;
			for(i=0;i<nr_class;i++)
				for(int j=i+1;j<nr_class;j++)
				{
	                            pairwise_prob[i][j]=fmin(fmax(sigmoid_predict(dec_values[k],probA[k],probB[k]),min_prob),1-min_prob);
					pairwise_prob[j][i]=1-pairwise_prob[i][j];
					k++;
				}
	                multiclass_probability(nr_class,pairwise_prob,prob_estimates);

			int prob_max_idx = 0;
			for(i=1;i<nr_class;i++)
				if(prob_estimates[i] > prob_estimates[prob_max_idx])
					prob_max_idx = i;
			for(i=0;i<nr_class;i++)
				free(pairwise_prob[i]);
			free(pairwise_prob);
			return prob_max_idx;
}
float k_function(const float * x, const float *y)
{
	double sum = 0;
	int dim = fmin(NUM_FEATURES, NUM_FEATURES), i;
	double* m_array = (double*)malloc(sizeof(double)*dim);
	for (i = 0; i < dim; i++)
	{
		m_array[i] = x[i] - y[i];
	}
	for (i = 0; i < dim; ++i)
	{
		sum += m_array[i] * m_array[i];
	}
	//sum = blas_functions->dot(dim, m_array, 1, m_array, 1);
	free(m_array);
	for (; i < NUM_FEATURES; i++)
		sum += x[i] * x[i];
	for (; i < NUM_FEATURES; i++)
		sum += y[i] * y[i];

	return exp(-svm_gamma*sum);
}

double predict_values(float *x, float* dec_values)
{
	int i;
	int nr_class = NUM_CLASSES;
	int l = NUM_SV;
	double *kvalue = Malloc(double,l);
	for(i=0;i<l;i++)
                kvalue[i] = k_function(x, SV[i]);

	int a;
	float nSV[NUM_CLASSES];
	for (a = 0; a < NUM_CLASSES; ++a)
	{
		nSV[a] = w_sum[a+1] - w_sum[a];
	}

	int *start = Malloc(int,nr_class);
	start[0] = 0;
	for(i=1;i<nr_class;i++)
		start[i] = start[i-1]+nSV[i-1];

	int *vote = Malloc(int,nr_class);
	for(i=0;i<nr_class;i++)
		vote[i] = 0;

	int p=0;
	for(i=0;i<nr_class;i++)
		for(int j=i+1;j<nr_class;j++)
		{
			double sum = 0;
			int si = start[i];
			int sj = start[j];
			int ci = nSV[i];
			int cj = nSV[j];

			int k;
			const float *coef1 = coeffs[j-1];
			const float *coef2 = coeffs[i];
			for(k=0;k<ci;k++)
				sum += coef1[si+k] * kvalue[si+k];
			for(k=0;k<cj;k++)
				sum += coef2[sj+k] * kvalue[sj+k];
			//sum -= model->rho[p];
			//sum += intercepts[p];
			dec_values[p] = sum;

			if(dec_values[p] > 0)
				++vote[i];
			else
				++vote[j];
			p++;
		}

	int vote_max_idx = 0;
	for(i=1;i<nr_class;i++)
		if(vote[i] > vote[vote_max_idx])
			vote_max_idx = i;
	free(start);
	free(vote);
	free(kvalue);
	return vote_max_idx;

}

int svc_predict(float* input, float* output)
{
    compute_kernels(input);
    float ovo_scores[NUM_INTERCEPTS];
    float ovr_scores[NUM_CLASSES];
    float dec_values[NUM_INTERCEPTS];
    //int max_idx;
    //int ovo_err = calculate_ovo_scores(kernels, ovo_scores);
    calculate_ovo_scores(kernels, ovo_scores);
    //int ovr_err = calculate_ovr_scores(ovo_scores, ovr_scores);
    calculate_ovr_scores(ovo_scores, ovr_scores);
    //predict_values(input, dec_values);
    if (NUM_CLASSES == 2)
    {
    	svm_predict_probability(ovo_scores, output);
	}
    else if (NUM_CLASSES > 2)
    {
    	svm_predict_probability(ovo_scores, output);
	}
    else
    {
    	return -1;
	}
    //memcpy(output, ovo_scores, sizeof(float) * NUM_CLASSES);
    //findMax(ovr_scores, &max_idx);
    //strcpy(output_label, LABELS[max_idx]);
    return 0;
}
