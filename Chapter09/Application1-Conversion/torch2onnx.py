import os
import torch.onnx
import torchvision
from Models.paths import ONNX_DIR

dummy_input = torch.randn(1, 3, 224, 224)
pretrained = "MobileNet_V3_Small_Weights.IMAGENET1K_V1"
model = torchvision.models.mobilenet_v3_small(weights = pretrained)
torch.onnx.export(model, dummy_input, os.path.join(ONNX_DIR, "mobilenetv3small.onnx"))
