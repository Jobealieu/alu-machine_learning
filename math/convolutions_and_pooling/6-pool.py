#!/usr/bin/env python3
"""Module that performs pooling on images"""
import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """Performs pooling on images

    Args:
        images: numpy.ndarray of shape (m, h, w, c) containing the images
        kernel_shape: tuple of (kh, kw) containing the pooling kernel shape
        stride: tuple of (sh, sw) with the stride for height and width
        mode: 'max' for max pooling or 'avg' for average pooling

    Returns:
        numpy.ndarray containing the pooled images
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride
    out_h = (h - kh) // sh + 1
    out_w = (w - kw) // sw + 1
    output = np.zeros((m, out_h, out_w, c))
    func = np.max if mode == 'max' else np.mean
    for i in range(out_h):
        for j in range(out_w):
            x = i * sh
            y = j * sw
            output[:, i, j, :] = func(
                images[:, x:x + kh, y:y + kw, :], axis=(1, 2))
    return output
