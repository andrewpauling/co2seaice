#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:45:44 2020

@author: -
"""

import numpy as np
import xarray as xr


def area_weighted_sum(data):
    """
    Compute area weighted sum of some CMIP6 data.

    Parameters
    ----------
    data : xarray DataArray
        DataArray containing the data to average.
        Assumes lat dimension/coordinate is called
        'lat' and lon dimension/coordinate is called
        'lon'

    Returns
    -------
    dout : xarray DataArray
        DataArray containing area-weighted sum of
        data. Has lost domensions of lat and lon

    """
    
    lat = data.lat
    coslat = np.cos(np.deg2rad(lat))
    
    dout = (data*coslat).sum(('lat', 'lon'))
    
    return dout


def area_weighted_mean(data):
    """
    Compute area weighted mean of some CMIP6 data.

    Parameters
    ----------
    data : xarray DataArray
        DataArray containing the data to average.
        Assumes lat dimension/coordinate is called
        'lat' and lon dimension/coordinate is called
        'lon'

    Returns
    -------
    dout : xarray DataArray
        DataArray containing area-weighted sum of
        data. Has lost domensions of lat and lon

    """
    
    lat = data.lat
    coslat = np.cos(np.deg2rad(lat))
    
    if len(lat.dims) == 1:
        dout = (data*coslat).sum(('lat', 'lon'))/coslat.sum('lat')
    else:
        dout = (data*coslat).sum(('lat', 'lon'))/coslat.sum('lat', 'lon')
        
    return dout