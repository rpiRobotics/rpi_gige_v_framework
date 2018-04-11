# Copyright (c) 2017, Rensselaer Polytechnic Institute, Wason Technology LLC
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Rensselaer Polytechnic Institute, or Wason 
#       Technology LLC, nor the names of its contributors may be used to 
#       endorse or promote products derived from this software without 
#       specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from __future__ import absolute_import
from . import gevapi
from . import gevoslib
import cv2
import ctypes
from collections import namedtuple
import socket
import struct
import numbers
import atexit
import time
import numpy

#https://stackoverflow.com/questions/5619685/conversion-from-ip-string-to-integer-and-backward-in-python
def _ip2int(addr):                                                               
    return struct.unpack("!I", socket.inet_aton(addr))[0] 
def _int2ip(addr):                                                               
    return socket.inet_ntoa(struct.pack("!I", addr))  

class timeval(ctypes.Structure):
    _fields_ = [("tv_sec", ctypes.c_long), ("tv_usec", ctypes.c_long)]
        

GevCameraInfo=namedtuple('GevCameraInfo', ('fIPv6','ipAddr','ipAddrLow','ipAddrHigh', \
  'macLow', 'macHigh','host', 'mode','capabilites','manufacturer','model', \
  'serial','version','username'))

GevNetworkInterface=namedtuple('GevNetworkInterface', ('fIpv6','ipAddr',\
    'ipAddrLow','ipAddrHigh','ifIndex'))

class GigE_V_VideoCapture(object):
    def __init__(self, device=None):
        self._camera=None
        
        self._height=2056
        self._width=2464
        self._depth=3
        
        if (device is not None):
            self.open(device)
        

    @staticmethod
    def get_camera_list():
        list1=(gevapi.GEV_CAMERA_INFO*10)()
        camera_count=(ctypes.c_int*1)()
        res=gevapi.GevGetCameraList(list1, 10, camera_count)
        if (res != 0):
            raise Exception("GigE GevApi Error: " + str(res))

        list2=[]
        for i in range(0,camera_count[0]):
            c=list1[i]
            h=c.host
            device_host=GevNetworkInterface(h.fIPv6 != 0, _int2ip(h.ipAddr), \
              h.ipAddrLow, h.ipAddrHigh, h.ifIndex)
            device_info=GevCameraInfo(c.fIPv6 != 0, _int2ip(c.ipAddr), c.ipAddrLow,\
              c.ipAddrHigh, c.macLow, c.macHigh, device_host, \
              c.mode, c.capabilities, c.manufacturer, c.model, \
              c.serial, c.version, c.username)
            list2.append(device_info)
        return list2


    def open(self, device=0):
        
        if (isinstance(device,numbers.Number)):
            list1=(gevapi.GEV_CAMERA_INFO*10)()
            camera_count=(ctypes.c_int*1)()
            res=gevapi.GevGetCameraList(list1, 10, camera_count)
            if (res != 0):
                raise Exception("GigE GevGetCameraList Error: " + str(res))
            if (not device < camera_count[0]):
                raise Exception('GigE Error: Invalid camera index')
            
            camera=gevapi.GEV_CAMERA_HANDLE(0)
            
            res=gevapi.GevOpenCamera(ctypes.pointer(list1[device]), gevapi.GevExclusiveMode, ctypes.pointer(camera))
            if (res != 0):
                raise Exception("GigE GevOpenCamera Error: " + str(res))
            
            self._camera=camera
            
        
        elif (isinstance(device,basestring)):
            
            ip_int=_ip2int(device)
            
            camera=gevapi.GEV_CAMERA_HANDLE(0)
            
            res=gevapi.GevOpenCameraByAddress(ip_int, gevapi.GevExclusiveMode, ctypes.pointer(camera))
            if (res != 0):
                raise Exception("GigE GevOpenCamera Error: " + str(res))
            
            self._camera=camera
            
        else:
            raise TypeError("GigE_V_VideoCapture.Open expects an integer or string ip address")
        
        width=ctypes.c_uint32()
        height=ctypes.c_uint32()
        x_offset=ctypes.c_uint32()
        y_offset=ctypes.c_uint32()
        format_=ctypes.c_uint32()        
        
        res=gevapi.GevGetImageParameters(self._camera, ctypes.byref(width), ctypes.byref(height), \
            ctypes.byref(x_offset), ctypes.byref(y_offset), ctypes.byref(format_))
        if (res != 0):
            gevapi.GevCloseCamera(self._camera)
            self._camera=None
            raise Exception("GigE GevGetImageParameters Error: " + str(res))
        
        if (format_.value != gevapi.fmtMono8 and format_.value != gevapi.fMtBayerRG8):
            gevapi.GevCloseCamera(self._camera)
            self._camera=None
            raise Exception("GigE_V_VideoCapture unknown device image format")
        
        self._height=height.value
        self._width=width.value
        self._depth=gevapi.GevGetPixelDepthInBits(format_)
        
        c=self._height * self._width * self._depth
        
        self._numpy_bufs=[numpy.ndarray(c, dtype=numpy.uint8) for i in range(3)]
        self._numpy_bufs_ctypes=[numpy.ctypeslib.as_ctypes(array) for array in self._numpy_bufs]
                
        self._bufs=(ctypes.POINTER(ctypes.c_uint8)*3)(*self._numpy_bufs_ctypes)

        res=gevapi.GevInitImageTransfer(self._camera, gevapi.SynchronousNextEmpty, 3, self._bufs)
        if (res != 0):
            raise Exception("GigE GevInitImageTransfer Error: " + str(res))
        
    def release(self):
        if (self._camera is not None):
            gevapi.GevCloseCamera(self._camera)            
            self._camera=None
            

    def read(self):
        
        if (self._camera is None):        
            return False, None
        
        res=gevapi.GevStartImageTransfer(self._camera, 1)
        if (res != 0):
            return False, None        
        buf=ctypes.POINTER(gevapi.GEV_BUFFER_OBJECT)()
   
        t=timeval(0,100000)
        res=gevapi.GevGetNextImage(self._camera, ctypes.pointer(buf), t)
                
        if (res != 0):
            return False, None     
        
        buf2=buf.contents
        
        if (buf2.format == gevapi.fmtMono8):
            n=buf2.h*buf2.w*buf2.d
            
            buf3=numpy.ctypeslib.as_array(buf2.address, (n,))
            
            buf4=numpy.reshape(buf3, (buf2.h, buf2.w))
            
            img=buf4.copy()
            
            gevapi.GevReleaseImage(self._camera, buf)
            
            return True, img
        
        elif (buf2.format == gevapi.fMtBayerRG8):
            n=buf2.h*buf2.w*buf2.d
            
            buf3=numpy.ctypeslib.as_array(buf2.address, (n,))
            
            buf4=numpy.reshape(buf3, (buf2.h, buf2.w))
            
            img=cv2.cvtColor(buf4, cv2.COLOR_BayerBG2BGR)
            
            gevapi.GevReleaseImage(self._camera, buf)
            
            return True, img
        else:
            gevapi.GevReleaseImage(self._camera, buf)
            raise Exception("Unknown image format")

    def __del__(self):
        self.release()

@atexit.register
def _rpi_gige_v_framework_cleanup():
    
    gevapi.GevApiUninitialize()    
    gevoslib._CloseSocketAPI()    
    
