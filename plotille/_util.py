# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# The MIT License

# Copyright (c) 2017 Tammo Ippen, tammo.ippen@posteo.de

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from math import floor


def roundeven(x):
    '''Round to next even integer number in case of `X.5`

    In Python3 this is the same as `round(x, 0)`, but since Python2 rounds up
    in that case and I want consistent behaviour, here is the roundeven function.

    Parameters:
        x: float  The number to round.

    Returns:
        int: floor(x)       if x - floor(x) < 0.5
             ceil(x)        if x - floor(x) > 0.5
             next even of x if x - floor(x) == 0.5
    '''
    x_r = round(x)
    if abs(x_r - x) == 0.5:
        return int(2.0 * round(x / 2))
    return x_r


def hist(X, bins):  # noqa: N803
    '''Create histogram similar to `numpy.hist()`

    Parameters:
        X: List[float]  The items to count over.
        bins: int       The number of bins to put X entries in.

    Returns:
        (counts, bins):
            counts: List[int]  The counts for all bins.
            bins: List[float]  The range for each bin: bin `i` is in [bins[i], bins[i+1])
    '''
    assert bins > 0
    xmin = min(X) if len(X) > 0 else 0
    xmax = max(X) if len(X) > 0 else 1
    xwidth = abs((xmax - xmin) / bins)

    y = [0] * bins
    for x in X:
        x_idx = min(bins - 1, int(floor((x - xmin) / xwidth)))
        y[x_idx] += 1

    return y, [i * xwidth + xmin for i in range(bins + 1)]
