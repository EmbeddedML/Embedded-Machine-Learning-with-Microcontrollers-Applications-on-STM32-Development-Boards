/*
 * lib_model.cpp
 *
 *  Created on: Oct 14, 2023
 *      Author: Eren Atmaca
 */
#include "lib_model.h"

using namespace tflite;
static void AllOpsResolver(void);

static tflite::MicroMutableOpResolver<88> micro_op_resolver;
static tflite::MicroInterpreter* interpreter;
static const tflite::Model* model = nullptr;

/*
 * @brief Initializes the TFLite model and library
 * @param tfliteModel 	TFLite Model
 * @param inputTensor 	Pointer to input TfLiteTensor structure
 * @param buffer 		Pointer to buffer
 * @param bufferSize 	Size of buffer
 * @retval 0 if successfully initialized
 */
int8_t LIB_MODEL_Init(const void *tfliteModel, TfLiteTensor **inputTensor, uint8_t *buffer, uint32_t bufferSize)
{
	model = tflite::GetModel(tfliteModel);
	if (model->version() != TFLITE_SCHEMA_VERSION)
	{
		MicroPrintf(
		  "Model provided is schema version %d not equal "
		  "to supported version %d.",
		  model->version(), TFLITE_SCHEMA_VERSION);
		return ERROR;
	}

	AllOpsResolver();

	static tflite::MicroInterpreter static_interpreter(model, micro_op_resolver, buffer, bufferSize);
	interpreter = &static_interpreter;

	// Allocate memory from the tensor_arena for the model's tensors.
	TfLiteStatus allocate_status = interpreter->AllocateTensors();
	if (allocate_status != kTfLiteOk)
	{
		MicroPrintf("AllocateTensors() failed");
		return ERROR;
	}

	// Get information about the memory area to use for the model's input.
	*inputTensor = interpreter->input(0);
	return OK;
}

/*
 * @brief Runs inference
 * @param output Pointer to output TfLiteTensor structure
 * @retval 0 if successfull inference
 */
int8_t LIB_MODEL_Run(TfLiteTensor **output)
{
	if (kTfLiteOk != interpreter->Invoke())
	{
		MicroPrintf("Invoke failed.");
		return ERROR;
	}
	*output = interpreter->output(0);
	return OK;
}

/*
 * @brief Initializes all operations
 * @param None
 * @retval None
 */
static void AllOpsResolver(void)
{
	// Please keep this list of Builtin Operators in alphabetical order.
	micro_op_resolver.AddAbs();
	micro_op_resolver.AddAdd();
	micro_op_resolver.AddAddN();
	micro_op_resolver.AddArgMax();
	micro_op_resolver.AddArgMin();
	micro_op_resolver.AddAssignVariable();
	micro_op_resolver.AddAveragePool2D();
	micro_op_resolver.AddBatchToSpaceNd();
	micro_op_resolver.AddCallOnce();
	micro_op_resolver.AddCast();
	micro_op_resolver.AddCeil();
	micro_op_resolver.AddCircularBuffer();
	micro_op_resolver.AddConcatenation();
	micro_op_resolver.AddConv2D();
	micro_op_resolver.AddCos();
	micro_op_resolver.AddCumSum();
	micro_op_resolver.AddDepthToSpace();
	micro_op_resolver.AddDepthwiseConv2D();
	micro_op_resolver.AddDequantize();
	micro_op_resolver.AddDetectionPostprocess();
	micro_op_resolver.AddElu();
	micro_op_resolver.AddEqual();
	micro_op_resolver.AddEthosU();
	micro_op_resolver.AddExp();
	micro_op_resolver.AddExpandDims();
	micro_op_resolver.AddFill();
	micro_op_resolver.AddFloor();
	micro_op_resolver.AddFloorDiv();
	micro_op_resolver.AddFloorMod();
	micro_op_resolver.AddFullyConnected();
	micro_op_resolver.AddGather();
	micro_op_resolver.AddGatherNd();
	micro_op_resolver.AddGreater();
	micro_op_resolver.AddGreaterEqual();
	micro_op_resolver.AddHardSwish();
	micro_op_resolver.AddIf();
	micro_op_resolver.AddL2Normalization();
	micro_op_resolver.AddL2Pool2D();
	micro_op_resolver.AddLeakyRelu();
	micro_op_resolver.AddLess();
	micro_op_resolver.AddLessEqual();
	micro_op_resolver.AddLog();
	micro_op_resolver.AddLogicalAnd();
	micro_op_resolver.AddLogicalNot();
	micro_op_resolver.AddLogicalOr();
	micro_op_resolver.AddLogistic();
	micro_op_resolver.AddMaxPool2D();
	micro_op_resolver.AddMaximum();
	micro_op_resolver.AddMean();
	micro_op_resolver.AddMinimum();
	micro_op_resolver.AddMirrorPad();
	micro_op_resolver.AddMul();
	micro_op_resolver.AddNeg();
	micro_op_resolver.AddNotEqual();
	micro_op_resolver.AddPack();
	micro_op_resolver.AddPad();
	micro_op_resolver.AddPadV2();
	micro_op_resolver.AddPrelu();
	micro_op_resolver.AddQuantize();
	micro_op_resolver.AddReadVariable();
	micro_op_resolver.AddReduceMax();
	micro_op_resolver.AddRelu();
	micro_op_resolver.AddRelu6();
	micro_op_resolver.AddReshape();
	micro_op_resolver.AddResizeBilinear();
	micro_op_resolver.AddResizeNearestNeighbor();
	micro_op_resolver.AddRound();
	micro_op_resolver.AddRsqrt();
	micro_op_resolver.AddShape();
	micro_op_resolver.AddSin();
	micro_op_resolver.AddSlice();
	micro_op_resolver.AddSoftmax();
	micro_op_resolver.AddSpaceToBatchNd();
	micro_op_resolver.AddSpaceToDepth();
	micro_op_resolver.AddSplit();
	micro_op_resolver.AddSplitV();
	micro_op_resolver.AddSqrt();
	micro_op_resolver.AddSquare();
	micro_op_resolver.AddSqueeze();
	micro_op_resolver.AddStridedSlice();
	micro_op_resolver.AddSub();
	micro_op_resolver.AddSvdf();
	micro_op_resolver.AddTanh();
	micro_op_resolver.AddTranspose();
	micro_op_resolver.AddTransposeConv();
	micro_op_resolver.AddUnpack();
	micro_op_resolver.AddVarHandle();
	micro_op_resolver.AddZerosLike();
}
