# # TODO TIP: Using Dice coeff is OK for measuring segmentation quality
# # TODO TIP: Optimizing the Dice Loss usually helps segmentation a lot.
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
#
#
# class DiceBCELoss(nn.Module):
#     def __init__(self, weight=None, size_average=True):
#         super(DiceBCELoss, self).__init__()
#
#     def forward(self, inputs, targets, smooth=1):
#         # comment out if your model contains a sigmoid or equivalent activation layer
#         inputs = F.sigmoid(inputs)
#
#         # flatten label and prediction tensors
#         inputs = inputs.view(-1)
#         targets = targets.view(-1)
#
#         intersection = (inputs * targets).sum()
#         dice_loss = 1 - (2. * intersection + smooth) / (inputs.sum() + targets.sum() + smooth)
#         BCE = F.binary_cross_entropy(inputs, targets, reduction='mean')
#         Dice_BCE = BCE + dice_loss
#
#         return Dice_BCE
#
#
# class DiceLoss(nn.Module):
#     def __init__(self, weight=None, size_average=True):
#         super(DiceLoss, self).__init__()
#
#     def forward(self, inputs, targets, smooth=1):
#         # comment out if your model contains a sigmoid or equivalent activation layer
#         inputs = F.sigmoid(inputs)
#
#         # flatten label and prediction tensors
#         inputs = inputs.view(-1)
#         targets = targets.view(-1)
#
#         intersection = (inputs * targets).sum()
#         dice = (2. * intersection + smooth) / (inputs.sum() + targets.sum() + smooth)
#
#         return 1 - dice
#
#
# def dice_coeff(input, target):
#     raise NotImplementedError
#
#
# def dice_loss(
#         input: torch.Tensor,
#         target: torch.Tensor) -> torch.Tensor:
#     r"""Function that computes Sørensen-Dice Coefficient loss.
#
#     See :class:`~torchgeometry.losses.DiceLoss` for details.
#     """
#     return DiceLoss()(input, target)
