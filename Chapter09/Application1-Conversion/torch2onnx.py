import torch.onnx
import torchvision

dummy_input = torch.randn(1, 3, 224, 224)
pretrained = "MobileNet_V3_Small_Weights.IMAGENET1K_V1"
model = torchvision.models.mobilenet_v3_small(weights = pretrained)
torch.onnx.export(model, dummy_input, "mobilenetv3small.onnx")
