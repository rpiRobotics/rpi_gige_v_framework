'''Wrapper for gevapi.h

Generated with:
/home/wasonj/.local/bin/ctypesgen.py -lGevApi gevapi.h -o gevapi.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["GevApi"] = load_library("GevApi")

# 1 libraries
# End libraries

# No modules

__time_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 139

__suseconds_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 141

u_int8_t = c_ubyte # /usr/include/x86_64-linux-gnu/sys/types.h: 173

u_int16_t = c_uint # /usr/include/x86_64-linux-gnu/sys/types.h: 174

u_int32_t = c_uint # /usr/include/x86_64-linux-gnu/sys/types.h: 175

# /usr/include/x86_64-linux-gnu/bits/time.h: 30
class struct_timeval(Structure):
    pass

struct_timeval.__slots__ = [
    'tv_sec',
    'tv_usec',
]
struct_timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]

pthread_t = c_ulong # /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 60

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 75
class struct___pthread_internal_list(Structure):
    pass

struct___pthread_internal_list.__slots__ = [
    '__prev',
    '__next',
]
struct___pthread_internal_list._fields_ = [
    ('__prev', POINTER(struct___pthread_internal_list)),
    ('__next', POINTER(struct___pthread_internal_list)),
]

__pthread_list_t = struct___pthread_internal_list # /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 79

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 92
class struct___pthread_mutex_s(Structure):
    pass

struct___pthread_mutex_s.__slots__ = [
    '__lock',
    '__count',
    '__owner',
    '__nusers',
    '__kind',
    '__spins',
    '__elision',
    '__list',
]
struct___pthread_mutex_s._fields_ = [
    ('__lock', c_int),
    ('__count', c_uint),
    ('__owner', c_int),
    ('__nusers', c_uint),
    ('__kind', c_int),
    ('__spins', c_short),
    ('__elision', c_short),
    ('__list', __pthread_list_t),
]

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 128
class union_anon_9(Union):
    pass

union_anon_9.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_9._fields_ = [
    ('__data', struct___pthread_mutex_s),
    ('__size', c_char * 40),
    ('__align', c_long),
]

pthread_mutex_t = union_anon_9 # /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 128

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 134
class union_anon_10(Union):
    pass

union_anon_10.__slots__ = [
    '__size',
    '__align',
]
union_anon_10._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]

pthread_mutexattr_t = union_anon_10 # /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 134

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 141
class struct_anon_11(Structure):
    pass

struct_anon_11.__slots__ = [
    '__lock',
    '__futex',
    '__total_seq',
    '__wakeup_seq',
    '__woken_seq',
    '__mutex',
    '__nwaiters',
    '__broadcast_seq',
]
struct_anon_11._fields_ = [
    ('__lock', c_int),
    ('__futex', c_uint),
    ('__total_seq', c_ulonglong),
    ('__wakeup_seq', c_ulonglong),
    ('__woken_seq', c_ulonglong),
    ('__mutex', POINTER(None)),
    ('__nwaiters', c_uint),
    ('__broadcast_seq', c_uint),
]

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 154
class union_anon_12(Union):
    pass

union_anon_12.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_12._fields_ = [
    ('__data', struct_anon_11),
    ('__size', c_char * 48),
    ('__align', c_longlong),
]

pthread_cond_t = union_anon_12 # /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 154

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 160
class union_anon_13(Union):
    pass

union_anon_13.__slots__ = [
    '__size',
    '__align',
]
union_anon_13._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]

pthread_condattr_t = union_anon_13 # /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 160

UINT8 = u_int8_t # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/cordef.h: 799

INT16 = c_int16 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/cordef.h: 800

UINT16 = u_int16_t # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/cordef.h: 801

INT32 = c_int32 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/cordef.h: 802

UINT32 = u_int32_t # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/cordef.h: 803

BOOL = c_int # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/posixcmn.h: 166

enum_anon_91 = c_int # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/corposix.h: 191

MutexType_t = enum_anon_91 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/corposix.h: 191

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/corposix.h: 204
class struct__CRITICAL_SECTION(Structure):
    pass

struct__CRITICAL_SECTION.__slots__ = [
    'type',
    'refCount',
    'waitCount',
    'ownerThread',
    'cvWaiter',
    'cvWaiterAttributes',
    'pCsMutex',
    'pCsMutexAttributes',
    'savedThreadCancelState',
]
struct__CRITICAL_SECTION._fields_ = [
    ('type', MutexType_t),
    ('refCount', c_long),
    ('waitCount', c_long),
    ('ownerThread', pthread_t),
    ('cvWaiter', pthread_cond_t),
    ('cvWaiterAttributes', pthread_condattr_t),
    ('pCsMutex', pthread_mutex_t),
    ('pCsMutexAttributes', pthread_mutexattr_t),
    ('savedThreadCancelState', c_int),
]

CRITICAL_SECTION = struct__CRITICAL_SECTION # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/corposix.h: 204

HANDLE = POINTER(None) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/corposix.h: 237

ULONG_PTR = c_ulong # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/cordef.h: 844

PUINT8 = POINTER(UINT8) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/cordef.h: 914

PUINT32 = POINTER(UINT32) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/cordef.h: 918

BOOL32 = INT32 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/cordef.h: 924

GEV_STATUS = UINT16 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gev_linux.h: 95

GEVLIB_STATUS = INT16 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gev_linux.h: 96

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/dynaqueue.h: 59
class struct__DYNAMIC_FIFO(Structure):
    pass

struct__DYNAMIC_FIFO.__slots__ = [
    'Size',
    'Head',
    'Tail',
    'Data',
]
struct__DYNAMIC_FIFO._fields_ = [
    ('Size', INT32),
    ('Head', INT32),
    ('Tail', INT32),
    ('Data', ULONG_PTR * 1),
]

PDYNAMIC_FIFO = POINTER(struct__DYNAMIC_FIFO) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/dynaqueue.h: 59

enum_anon_105 = c_int # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/dynaqueue.h: 151

QueueMode = enum_anon_105 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/dynaqueue.h: 151

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/dynaqueue.h: 169
class struct__DQUEUE(Structure):
    pass

struct__DQUEUE.__slots__ = [
    'cSection',
    'waitEvent',
    'mode',
    'valid',
    'dFifo',
]
struct__DQUEUE._fields_ = [
    ('cSection', CRITICAL_SECTION),
    ('waitEvent', HANDLE),
    ('mode', QueueMode),
    ('valid', c_int),
    ('dFifo', PDYNAMIC_FIFO),
]

DQUEUE = struct__DQUEUE # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/dynaqueue.h: 169

enum_anon_106 = c_int # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtMono8 = 17301505 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtMono8Signed = 17301506 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtMono10 = 17825795 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtMono10Packed = 17563652 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtMono12 = 17825797 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtMono12Packed = 17563654 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtMono14 = 17825829 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtMono16 = 17825799 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fMtBayerGR8 = 17301512 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fMtBayerRG8 = 17301513 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fMtBayerGB8 = 17301514 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fMtBayerBG8 = 17301515 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fMtBayerGR10 = 17825804 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fMtBayerRG10 = 17825805 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fMtBayerGB10 = 17825806 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fMtBayerBG10 = 17825807 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fMtBayerGR12 = 17825808 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fMtBayerRG12 = 17825809 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fMtBayerGB12 = 17825810 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fMtBayerBG12 = 17825811 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtRGB8Packed = 35127316 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtBGR8Packed = 35127317 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtRGBA8Packed = 35651606 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtBGRA8Packed = 35651607 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtRGB10Packed = 36700184 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtBGR10Packed = 36700185 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtRGB12Packed = 36700186 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtBGR12Packed = 36700187 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtRGB10V1Packed = 35651612 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtRGB10V2Packed = 35651613 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtYUV411packed = 34340894 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtYUV422packed = 34603039 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtYUV444packed = 35127328 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmt_PFNC_YUV422_8 = 34603058 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtRGB8Planar = 35127329 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtRGB10Planar = 36700194 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtRGB12Planar = 36700195 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmtRGB16Planar = 36700196 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmt_PFNC_BiColorBGRG8 = 34603174 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmt_PFNC_BiColorBGRG10 = 35651753 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmt_PFNC_BiColorBGRG10p = 34865322 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmt_PFNC_BiColorBGRG12 = 35651757 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmt_PFNC_BiColorBGRG12p = 35127470 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmt_PFNC_BiColorRGBG8 = 34603173 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmt_PFNC_BiColorRGBG10 = 35651751 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmt_PFNC_BiColorRGBG10p = 34865320 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmt_PFNC_BiColorRGBG12 = 35651755 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

fmt_PFNC_BiColorRGBG12p = 35127468 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

enumGevPixelFormat = enum_anon_106 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 231

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 253
if hasattr(_libs['GevApi'], 'GevIsPixelTypeMono'):
    GevIsPixelTypeMono = _libs['GevApi'].GevIsPixelTypeMono
    GevIsPixelTypeMono.argtypes = [UINT32]
    GevIsPixelTypeMono.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 254
if hasattr(_libs['GevApi'], 'GevIsPixelTypeRGB'):
    GevIsPixelTypeRGB = _libs['GevApi'].GevIsPixelTypeRGB
    GevIsPixelTypeRGB.argtypes = [UINT32]
    GevIsPixelTypeRGB.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 255
if hasattr(_libs['GevApi'], 'GevIsPixelTypeCustom'):
    GevIsPixelTypeCustom = _libs['GevApi'].GevIsPixelTypeCustom
    GevIsPixelTypeCustom.argtypes = [UINT32]
    GevIsPixelTypeCustom.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 256
if hasattr(_libs['GevApi'], 'GevIsPixelTypePacked'):
    GevIsPixelTypePacked = _libs['GevApi'].GevIsPixelTypePacked
    GevIsPixelTypePacked.argtypes = [UINT32]
    GevIsPixelTypePacked.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 257
if hasattr(_libs['GevApi'], 'GevGetPixelSizeInBytes'):
    GevGetPixelSizeInBytes = _libs['GevApi'].GevGetPixelSizeInBytes
    GevGetPixelSizeInBytes.argtypes = [UINT32]
    GevGetPixelSizeInBytes.restype = UINT32

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 258
if hasattr(_libs['GevApi'], 'GevGetPixelDepthInBits'):
    GevGetPixelDepthInBits = _libs['GevApi'].GevGetPixelDepthInBits
    GevGetPixelDepthInBits.argtypes = [UINT32]
    GevGetPixelDepthInBits.restype = UINT32

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 259
if hasattr(_libs['GevApi'], 'GevGetRGBPixelOrder'):
    GevGetRGBPixelOrder = _libs['GevApi'].GevGetRGBPixelOrder
    GevGetRGBPixelOrder.argtypes = [UINT32]
    GevGetRGBPixelOrder.restype = UINT32

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 260
if hasattr(_libs['GevApi'], 'GevTranslateRawPixelFormat'):
    GevTranslateRawPixelFormat = _libs['GevApi'].GevTranslateRawPixelFormat
    GevTranslateRawPixelFormat.argtypes = [UINT32, PUINT32, PUINT32, PUINT32]
    GevTranslateRawPixelFormat.restype = GEVLIB_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 261
if hasattr(_libs['GevApi'], 'GevGetFormatString'):
    GevGetFormatString = _libs['GevApi'].GevGetFormatString
    GevGetFormatString.argtypes = [UINT32]
    if sizeof(c_int) == sizeof(c_void_p):
        GevGetFormatString.restype = ReturnString
    else:
        GevGetFormatString.restype = String
        GevGetFormatString.errcheck = ReturnString

enum_anon_107 = c_int # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 270

GevMonitorMode = 0 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 270

GevControlMode = 2 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 270

GevExclusiveMode = 4 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 270

GevAccessMode = enum_anon_107 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 270

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 287
class struct_anon_108(Structure):
    pass

struct_anon_108.__slots__ = [
    'version',
    'logLevel',
    'numRetries',
    'command_timeout_ms',
    'discovery_timeout_ms',
    'enumeration_port',
    'gvcp_port_range_start',
    'gvcp_port_range_end',
]
struct_anon_108._fields_ = [
    ('version', UINT32),
    ('logLevel', UINT32),
    ('numRetries', UINT32),
    ('command_timeout_ms', UINT32),
    ('discovery_timeout_ms', UINT32),
    ('enumeration_port', UINT32),
    ('gvcp_port_range_start', UINT32),
    ('gvcp_port_range_end', UINT32),
]

GEVLIB_CONFIG_OPTIONS = struct_anon_108 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 287

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 277
class struct_anon_109(Structure):
    pass

struct_anon_109.__slots__ = [
    'version',
    'logLevel',
    'numRetries',
    'command_timeout_ms',
    'discovery_timeout_ms',
    'enumeration_port',
    'gvcp_port_range_start',
    'gvcp_port_range_end',
]
struct_anon_109._fields_ = [
    ('version', UINT32),
    ('logLevel', UINT32),
    ('numRetries', UINT32),
    ('command_timeout_ms', UINT32),
    ('discovery_timeout_ms', UINT32),
    ('enumeration_port', UINT32),
    ('gvcp_port_range_start', UINT32),
    ('gvcp_port_range_end', UINT32),
]

PGEVLIB_CONFIG_OPTIONS = POINTER(struct_anon_109) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 287

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 303
class struct_anon_110(Structure):
    pass

struct_anon_110.__slots__ = [
    'numRetries',
    'command_timeout_ms',
    'heartbeat_timeout_ms',
    'streamPktSize',
    'streamPktDelay',
    'streamNumFramesBuffered',
    'streamMemoryLimitMax',
    'streamMaxPacketResends',
    'streamFrame_timeout_ms',
    'streamThreadAffinity',
    'serverThreadAffinity',
    'msgChannel_timeout_ms',
]
struct_anon_110._fields_ = [
    ('numRetries', UINT32),
    ('command_timeout_ms', UINT32),
    ('heartbeat_timeout_ms', UINT32),
    ('streamPktSize', UINT32),
    ('streamPktDelay', UINT32),
    ('streamNumFramesBuffered', UINT32),
    ('streamMemoryLimitMax', UINT32),
    ('streamMaxPacketResends', UINT32),
    ('streamFrame_timeout_ms', UINT32),
    ('streamThreadAffinity', INT32),
    ('serverThreadAffinity', INT32),
    ('msgChannel_timeout_ms', UINT32),
]

GEV_CAMERA_OPTIONS = struct_anon_110 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 303

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 289
class struct_anon_111(Structure):
    pass

struct_anon_111.__slots__ = [
    'numRetries',
    'command_timeout_ms',
    'heartbeat_timeout_ms',
    'streamPktSize',
    'streamPktDelay',
    'streamNumFramesBuffered',
    'streamMemoryLimitMax',
    'streamMaxPacketResends',
    'streamFrame_timeout_ms',
    'streamThreadAffinity',
    'serverThreadAffinity',
    'msgChannel_timeout_ms',
]
struct_anon_111._fields_ = [
    ('numRetries', UINT32),
    ('command_timeout_ms', UINT32),
    ('heartbeat_timeout_ms', UINT32),
    ('streamPktSize', UINT32),
    ('streamPktDelay', UINT32),
    ('streamNumFramesBuffered', UINT32),
    ('streamMemoryLimitMax', UINT32),
    ('streamMaxPacketResends', UINT32),
    ('streamFrame_timeout_ms', UINT32),
    ('streamThreadAffinity', INT32),
    ('serverThreadAffinity', INT32),
    ('msgChannel_timeout_ms', UINT32),
]

PGEV_CAMERA_OPTIONS = POINTER(struct_anon_111) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 303

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 312
class struct_anon_112(Structure):
    pass

struct_anon_112.__slots__ = [
    'fIPv6',
    'ipAddr',
    'ipAddrLow',
    'ipAddrHigh',
    'ifIndex',
]
struct_anon_112._fields_ = [
    ('fIPv6', BOOL),
    ('ipAddr', UINT32),
    ('ipAddrLow', UINT32),
    ('ipAddrHigh', UINT32),
    ('ifIndex', UINT32),
]

GEV_NETWORK_INTERFACE = struct_anon_112 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 312

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 305
class struct_anon_113(Structure):
    pass

struct_anon_113.__slots__ = [
    'fIPv6',
    'ipAddr',
    'ipAddrLow',
    'ipAddrHigh',
    'ifIndex',
]
struct_anon_113._fields_ = [
    ('fIPv6', BOOL),
    ('ipAddr', UINT32),
    ('ipAddrLow', UINT32),
    ('ipAddrHigh', UINT32),
    ('ifIndex', UINT32),
]

PGEV_NETWORK_INTERFACE = POINTER(struct_anon_113) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 312

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 332
class struct_anon_114(Structure):
    pass

struct_anon_114.__slots__ = [
    'fIPv6',
    'ipAddr',
    'ipAddrLow',
    'ipAddrHigh',
    'macLow',
    'macHigh',
    'host',
    'mode',
    'capabilities',
    'manufacturer',
    'model',
    'serial',
    'version',
    'username',
]
struct_anon_114._fields_ = [
    ('fIPv6', BOOL),
    ('ipAddr', UINT32),
    ('ipAddrLow', UINT32),
    ('ipAddrHigh', UINT32),
    ('macLow', UINT32),
    ('macHigh', UINT32),
    ('host', GEV_NETWORK_INTERFACE),
    ('mode', UINT32),
    ('capabilities', UINT32),
    ('manufacturer', c_char * (64 + 1)),
    ('model', c_char * (64 + 1)),
    ('serial', c_char * (64 + 1)),
    ('version', c_char * (64 + 1)),
    ('username', c_char * (64 + 1)),
]

GEV_DEVICE_INTERFACE = struct_anon_114 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 332

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 316
class struct_anon_115(Structure):
    pass

struct_anon_115.__slots__ = [
    'fIPv6',
    'ipAddr',
    'ipAddrLow',
    'ipAddrHigh',
    'macLow',
    'macHigh',
    'host',
    'mode',
    'capabilities',
    'manufacturer',
    'model',
    'serial',
    'version',
    'username',
]
struct_anon_115._fields_ = [
    ('fIPv6', BOOL),
    ('ipAddr', UINT32),
    ('ipAddrLow', UINT32),
    ('ipAddrHigh', UINT32),
    ('macLow', UINT32),
    ('macHigh', UINT32),
    ('host', GEV_NETWORK_INTERFACE),
    ('mode', UINT32),
    ('capabilities', UINT32),
    ('manufacturer', c_char * (64 + 1)),
    ('model', c_char * (64 + 1)),
    ('serial', c_char * (64 + 1)),
    ('version', c_char * (64 + 1)),
    ('username', c_char * (64 + 1)),
]

PGEV_DEVICE_INTERFACE = POINTER(struct_anon_115) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 332

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 332
class struct_anon_116(Structure):
    pass

struct_anon_116.__slots__ = [
    'fIPv6',
    'ipAddr',
    'ipAddrLow',
    'ipAddrHigh',
    'macLow',
    'macHigh',
    'host',
    'mode',
    'capabilities',
    'manufacturer',
    'model',
    'serial',
    'version',
    'username',
]
struct_anon_116._fields_ = [
    ('fIPv6', BOOL),
    ('ipAddr', UINT32),
    ('ipAddrLow', UINT32),
    ('ipAddrHigh', UINT32),
    ('macLow', UINT32),
    ('macHigh', UINT32),
    ('host', GEV_NETWORK_INTERFACE),
    ('mode', UINT32),
    ('capabilities', UINT32),
    ('manufacturer', c_char * (64 + 1)),
    ('model', c_char * (64 + 1)),
    ('serial', c_char * (64 + 1)),
    ('version', c_char * (64 + 1)),
    ('username', c_char * (64 + 1)),
]

GEV_CAMERA_INFO = struct_anon_116 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 332

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 316
class struct_anon_117(Structure):
    pass

struct_anon_117.__slots__ = [
    'fIPv6',
    'ipAddr',
    'ipAddrLow',
    'ipAddrHigh',
    'macLow',
    'macHigh',
    'host',
    'mode',
    'capabilities',
    'manufacturer',
    'model',
    'serial',
    'version',
    'username',
]
struct_anon_117._fields_ = [
    ('fIPv6', BOOL),
    ('ipAddr', UINT32),
    ('ipAddrLow', UINT32),
    ('ipAddrHigh', UINT32),
    ('macLow', UINT32),
    ('macHigh', UINT32),
    ('host', GEV_NETWORK_INTERFACE),
    ('mode', UINT32),
    ('capabilities', UINT32),
    ('manufacturer', c_char * (64 + 1)),
    ('model', c_char * (64 + 1)),
    ('serial', c_char * (64 + 1)),
    ('version', c_char * (64 + 1)),
    ('username', c_char * (64 + 1)),
]

PGEV_CAMERA_INFO = POINTER(struct_anon_117) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 332

GEV_CAMERA_HANDLE = POINTER(None) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 334

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 354
class struct__tag_GEVBUF_ENTRY(Structure):
    pass

struct__tag_GEVBUF_ENTRY.__slots__ = [
    'state',
    'status',
    'timestamp_hi',
    'timestamp_lo',
    'recv_size',
    'id',
    'h',
    'w',
    'x_offset',
    'y_offset',
    'x_padding',
    'y_padding',
    'd',
    'format',
    'address',
]
struct__tag_GEVBUF_ENTRY._fields_ = [
    ('state', UINT32),
    ('status', UINT32),
    ('timestamp_hi', UINT32),
    ('timestamp_lo', UINT32),
    ('recv_size', UINT32),
    ('id', UINT32),
    ('h', UINT32),
    ('w', UINT32),
    ('x_offset', UINT32),
    ('y_offset', UINT32),
    ('x_padding', UINT32),
    ('y_padding', UINT32),
    ('d', UINT32),
    ('format', UINT32),
    ('address', PUINT8),
]

GEVBUF_ENTRY = struct__tag_GEVBUF_ENTRY # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 354

PGEVBUF_ENTRY = POINTER(struct__tag_GEVBUF_ENTRY) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 354

GEVBUF_HEADER = struct__tag_GEVBUF_ENTRY # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 354

PGEVBUF_HEADER = POINTER(struct__tag_GEVBUF_ENTRY) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 354

GEV_BUFFER_OBJECT = struct__tag_GEVBUF_ENTRY # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 354

PGEV_BUFFER_OBJECT = POINTER(struct__tag_GEVBUF_ENTRY) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 354

enum_anon_118 = c_int # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 369

Asynchronous = 0 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 369

SynchronousNextEmpty = 1 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 369

GevBufferCyclingMode = enum_anon_118 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 369

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 388
class struct__GEVBUF_QUEUE(Structure):
    pass

struct__GEVBUF_QUEUE.__slots__ = [
    'type',
    'height',
    'width',
    'depth',
    'size',
    'numBuffer',
    'lastBuffer',
    'nextBuffer',
    'trashCount',
    'cyclingMode',
    'pEmptyBuffers',
    'pFullBuffers',
    'pCurBuf',
    'buffer',
]
struct__GEVBUF_QUEUE._fields_ = [
    ('type', UINT32),
    ('height', UINT32),
    ('width', UINT32),
    ('depth', UINT32),
    ('size', UINT32),
    ('numBuffer', UINT32),
    ('lastBuffer', INT32),
    ('nextBuffer', UINT32),
    ('trashCount', UINT32),
    ('cyclingMode', GevBufferCyclingMode),
    ('pEmptyBuffers', POINTER(DQUEUE)),
    ('pFullBuffers', POINTER(DQUEUE)),
    ('pCurBuf', POINTER(GEVBUF_ENTRY)),
    ('buffer', GEVBUF_ENTRY * 1),
]

GEV_BUFFER_LIST = struct__GEVBUF_QUEUE # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 388

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 399
class struct_anon_119(Structure):
    pass

struct_anon_119.__slots__ = [
    'reserved',
    'eventNumber',
    'streamChannelIndex',
    'blockId',
    'timeStampHigh',
    'timeStampLow',
]
struct_anon_119._fields_ = [
    ('reserved', UINT16),
    ('eventNumber', UINT16),
    ('streamChannelIndex', UINT16),
    ('blockId', UINT16),
    ('timeStampHigh', UINT32),
    ('timeStampLow', UINT32),
]

EVENT_MSG = struct_anon_119 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 399

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 391
class struct_anon_120(Structure):
    pass

struct_anon_120.__slots__ = [
    'reserved',
    'eventNumber',
    'streamChannelIndex',
    'blockId',
    'timeStampHigh',
    'timeStampLow',
]
struct_anon_120._fields_ = [
    ('reserved', UINT16),
    ('eventNumber', UINT16),
    ('streamChannelIndex', UINT16),
    ('blockId', UINT16),
    ('timeStampHigh', UINT32),
    ('timeStampLow', UINT32),
]

PEVENT_MSG = POINTER(struct_anon_120) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 399

GEVEVENT_CBFUNCTION = CFUNCTYPE(UNCHECKED(None), PEVENT_MSG, PUINT8, UINT16, POINTER(None)) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 401

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 406
if hasattr(_libs['GevApi'], 'GevFormatCameraInfo'):
    GevFormatCameraInfo = _libs['GevApi'].GevFormatCameraInfo
    GevFormatCameraInfo.argtypes = [POINTER(GEV_DEVICE_INTERFACE), String, UINT32]
    GevFormatCameraInfo.restype = UINT32

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 409
if hasattr(_libs['GevApi'], 'GevPrint'):
    _func = _libs['GevApi'].GevPrint
    _restype = c_int
    _argtypes = [c_int, String, c_uint, String]
    GevPrint = _variadic_function(_func,_restype,_argtypes)

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 510
if hasattr(_libs['GevApi'], 'GevApiInitialize'):
    GevApiInitialize = _libs['GevApi'].GevApiInitialize
    GevApiInitialize.argtypes = []
    GevApiInitialize.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 511
if hasattr(_libs['GevApi'], 'GevApiUninitialize'):
    GevApiUninitialize = _libs['GevApi'].GevApiUninitialize
    GevApiUninitialize.argtypes = []
    GevApiUninitialize.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 515
if hasattr(_libs['GevApi'], 'GevGetLibraryConfigOptions'):
    GevGetLibraryConfigOptions = _libs['GevApi'].GevGetLibraryConfigOptions
    GevGetLibraryConfigOptions.argtypes = [POINTER(GEVLIB_CONFIG_OPTIONS)]
    GevGetLibraryConfigOptions.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 516
if hasattr(_libs['GevApi'], 'GevSetLibraryConfigOptions'):
    GevSetLibraryConfigOptions = _libs['GevApi'].GevSetLibraryConfigOptions
    GevSetLibraryConfigOptions.argtypes = [POINTER(GEVLIB_CONFIG_OPTIONS)]
    GevSetLibraryConfigOptions.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 520
if hasattr(_libs['GevApi'], 'GevDeviceCount'):
    GevDeviceCount = _libs['GevApi'].GevDeviceCount
    GevDeviceCount.argtypes = []
    GevDeviceCount.restype = c_int

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 521
if hasattr(_libs['GevApi'], 'GevGetCameraList'):
    GevGetCameraList = _libs['GevApi'].GevGetCameraList
    GevGetCameraList.argtypes = [POINTER(GEV_CAMERA_INFO), c_int, POINTER(c_int)]
    GevGetCameraList.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 523
if hasattr(_libs['GevApi'], 'GevForceCameraIPAddress'):
    GevForceCameraIPAddress = _libs['GevApi'].GevForceCameraIPAddress
    GevForceCameraIPAddress.argtypes = [UINT32, UINT32, UINT32, UINT32]
    GevForceCameraIPAddress.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 524
if hasattr(_libs['GevApi'], 'GevEnumerateNetworkInterfaces'):
    GevEnumerateNetworkInterfaces = _libs['GevApi'].GevEnumerateNetworkInterfaces
    GevEnumerateNetworkInterfaces.argtypes = [POINTER(GEV_NETWORK_INTERFACE), UINT32, PUINT32]
    GevEnumerateNetworkInterfaces.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 528
if hasattr(_libs['GevApi'], 'GevEnumerateGevDevices'):
    GevEnumerateGevDevices = _libs['GevApi'].GevEnumerateGevDevices
    GevEnumerateGevDevices.argtypes = [POINTER(GEV_NETWORK_INTERFACE), UINT32, POINTER(GEV_DEVICE_INTERFACE), UINT32, PUINT32]
    GevEnumerateGevDevices.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 531
if hasattr(_libs['GevApi'], 'GevSetCameraList'):
    GevSetCameraList = _libs['GevApi'].GevSetCameraList
    GevSetCameraList.argtypes = [POINTER(GEV_CAMERA_INFO), c_int]
    GevSetCameraList.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 535
if hasattr(_libs['GevApi'], 'GevOpenCamera'):
    GevOpenCamera = _libs['GevApi'].GevOpenCamera
    GevOpenCamera.argtypes = [POINTER(GEV_CAMERA_INFO), GevAccessMode, POINTER(GEV_CAMERA_HANDLE)]
    GevOpenCamera.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 536
if hasattr(_libs['GevApi'], 'GevOpenCameraByAddress'):
    GevOpenCameraByAddress = _libs['GevApi'].GevOpenCameraByAddress
    GevOpenCameraByAddress.argtypes = [c_ulong, GevAccessMode, POINTER(GEV_CAMERA_HANDLE)]
    GevOpenCameraByAddress.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 537
if hasattr(_libs['GevApi'], 'GevOpenCameraByName'):
    GevOpenCameraByName = _libs['GevApi'].GevOpenCameraByName
    GevOpenCameraByName.argtypes = [String, GevAccessMode, POINTER(GEV_CAMERA_HANDLE)]
    GevOpenCameraByName.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 538
if hasattr(_libs['GevApi'], 'GevOpenCameraBySN'):
    GevOpenCameraBySN = _libs['GevApi'].GevOpenCameraBySN
    GevOpenCameraBySN.argtypes = [String, GevAccessMode, POINTER(GEV_CAMERA_HANDLE)]
    GevOpenCameraBySN.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 540
if hasattr(_libs['GevApi'], 'GevCloseCamera'):
    GevCloseCamera = _libs['GevApi'].GevCloseCamera
    GevCloseCamera.argtypes = [POINTER(GEV_CAMERA_HANDLE)]
    GevCloseCamera.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 542
if hasattr(_libs['GevApi'], 'GevGetCameraInfo'):
    GevGetCameraInfo = _libs['GevApi'].GevGetCameraInfo
    GevGetCameraInfo.argtypes = [GEV_CAMERA_HANDLE]
    GevGetCameraInfo.restype = POINTER(GEV_CAMERA_INFO)

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 544
if hasattr(_libs['GevApi'], 'GevGetCameraInterfaceOptions'):
    GevGetCameraInterfaceOptions = _libs['GevApi'].GevGetCameraInterfaceOptions
    GevGetCameraInterfaceOptions.argtypes = [GEV_CAMERA_HANDLE, POINTER(GEV_CAMERA_OPTIONS)]
    GevGetCameraInterfaceOptions.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 545
if hasattr(_libs['GevApi'], 'GevSetCameraInterfaceOptions'):
    GevSetCameraInterfaceOptions = _libs['GevApi'].GevSetCameraInterfaceOptions
    GevSetCameraInterfaceOptions.argtypes = [GEV_CAMERA_HANDLE, POINTER(GEV_CAMERA_OPTIONS)]
    GevSetCameraInterfaceOptions.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 549
if hasattr(_libs['GevApi'], 'Gev_RetrieveXMLData'):
    Gev_RetrieveXMLData = _libs['GevApi'].Gev_RetrieveXMLData
    Gev_RetrieveXMLData.argtypes = [GEV_CAMERA_HANDLE, c_int, String, POINTER(c_int), POINTER(c_int)]
    Gev_RetrieveXMLData.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 550
if hasattr(_libs['GevApi'], 'Gev_RetrieveXMLFile'):
    Gev_RetrieveXMLFile = _libs['GevApi'].Gev_RetrieveXMLFile
    Gev_RetrieveXMLFile.argtypes = [GEV_CAMERA_HANDLE, String, c_int, BOOL]
    Gev_RetrieveXMLFile.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 554
if hasattr(_libs['GevApi'], 'GevConnectFeatures'):
    GevConnectFeatures = _libs['GevApi'].GevConnectFeatures
    GevConnectFeatures.argtypes = [GEV_CAMERA_HANDLE, POINTER(None)]
    GevConnectFeatures.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 555
if hasattr(_libs['GevApi'], 'GevGetFeatureNodeMap'):
    GevGetFeatureNodeMap = _libs['GevApi'].GevGetFeatureNodeMap
    GevGetFeatureNodeMap.argtypes = [GEV_CAMERA_HANDLE]
    GevGetFeatureNodeMap.restype = POINTER(None)

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 559
if hasattr(_libs['GevApi'], 'GevGetGenICamXML_FileName'):
    GevGetGenICamXML_FileName = _libs['GevApi'].GevGetGenICamXML_FileName
    GevGetGenICamXML_FileName.argtypes = [GEV_CAMERA_HANDLE, c_int, String]
    GevGetGenICamXML_FileName.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 560
if hasattr(_libs['GevApi'], 'GevInitGenICamXMLFeatures'):
    GevInitGenICamXMLFeatures = _libs['GevApi'].GevInitGenICamXMLFeatures
    GevInitGenICamXMLFeatures.argtypes = [GEV_CAMERA_HANDLE, BOOL]
    GevInitGenICamXMLFeatures.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 561
if hasattr(_libs['GevApi'], 'GevInitGenICamXMLFeatures_FromFile'):
    GevInitGenICamXMLFeatures_FromFile = _libs['GevApi'].GevInitGenICamXMLFeatures_FromFile
    GevInitGenICamXMLFeatures_FromFile.argtypes = [GEV_CAMERA_HANDLE, String]
    GevInitGenICamXMLFeatures_FromFile.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 562
if hasattr(_libs['GevApi'], 'GevInitGenICamXMLFeatures_FromData'):
    GevInitGenICamXMLFeatures_FromData = _libs['GevApi'].GevInitGenICamXMLFeatures_FromData
    GevInitGenICamXMLFeatures_FromData.argtypes = [GEV_CAMERA_HANDLE, c_int, POINTER(None)]
    GevInitGenICamXMLFeatures_FromData.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 564
if hasattr(_libs['GevApi'], 'GevGetFeatureValue'):
    GevGetFeatureValue = _libs['GevApi'].GevGetFeatureValue
    GevGetFeatureValue.argtypes = [GEV_CAMERA_HANDLE, String, POINTER(c_int), c_int, POINTER(None)]
    GevGetFeatureValue.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 565
if hasattr(_libs['GevApi'], 'GevSetFeatureValue'):
    GevSetFeatureValue = _libs['GevApi'].GevSetFeatureValue
    GevSetFeatureValue.argtypes = [GEV_CAMERA_HANDLE, String, c_int, POINTER(None)]
    GevSetFeatureValue.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 566
if hasattr(_libs['GevApi'], 'GevGetFeatureValueAsString'):
    GevGetFeatureValueAsString = _libs['GevApi'].GevGetFeatureValueAsString
    GevGetFeatureValueAsString.argtypes = [GEV_CAMERA_HANDLE, String, POINTER(c_int), c_int, String]
    GevGetFeatureValueAsString.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 567
if hasattr(_libs['GevApi'], 'GevSetFeatureValueAsString'):
    GevSetFeatureValueAsString = _libs['GevApi'].GevSetFeatureValueAsString
    GevSetFeatureValueAsString.argtypes = [GEV_CAMERA_HANDLE, String, String]
    GevSetFeatureValueAsString.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 571
if hasattr(_libs['GevApi'], 'GevGetImageParameters'):
    GevGetImageParameters = _libs['GevApi'].GevGetImageParameters
    GevGetImageParameters.argtypes = [GEV_CAMERA_HANDLE, PUINT32, PUINT32, PUINT32, PUINT32, PUINT32]
    GevGetImageParameters.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 572
if hasattr(_libs['GevApi'], 'GevSetImageParameters'):
    GevSetImageParameters = _libs['GevApi'].GevSetImageParameters
    GevSetImageParameters.argtypes = [GEV_CAMERA_HANDLE, UINT32, UINT32, UINT32, UINT32, UINT32]
    GevSetImageParameters.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 574
if hasattr(_libs['GevApi'], 'GevInitImageTransfer'):
    GevInitImageTransfer = _libs['GevApi'].GevInitImageTransfer
    GevInitImageTransfer.argtypes = [GEV_CAMERA_HANDLE, GevBufferCyclingMode, UINT32, POINTER(POINTER(UINT8))]
    GevInitImageTransfer.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 575
if hasattr(_libs['GevApi'], 'GevInitializeImageTransfer'):
    GevInitializeImageTransfer = _libs['GevApi'].GevInitializeImageTransfer
    GevInitializeImageTransfer.argtypes = [GEV_CAMERA_HANDLE, UINT32, POINTER(POINTER(UINT8))]
    GevInitializeImageTransfer.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 576
if hasattr(_libs['GevApi'], 'GevFreeImageTransfer'):
    GevFreeImageTransfer = _libs['GevApi'].GevFreeImageTransfer
    GevFreeImageTransfer.argtypes = [GEV_CAMERA_HANDLE]
    GevFreeImageTransfer.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 577
if hasattr(_libs['GevApi'], 'GevStartImageTransfer'):
    GevStartImageTransfer = _libs['GevApi'].GevStartImageTransfer
    GevStartImageTransfer.argtypes = [GEV_CAMERA_HANDLE, UINT32]
    GevStartImageTransfer.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 578
if hasattr(_libs['GevApi'], 'GevStopImageTransfer'):
    GevStopImageTransfer = _libs['GevApi'].GevStopImageTransfer
    GevStopImageTransfer.argtypes = [GEV_CAMERA_HANDLE]
    GevStopImageTransfer.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 579
if hasattr(_libs['GevApi'], 'GevAbortImageTransfer'):
    GevAbortImageTransfer = _libs['GevApi'].GevAbortImageTransfer
    GevAbortImageTransfer.argtypes = [GEV_CAMERA_HANDLE]
    GevAbortImageTransfer.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 581
if hasattr(_libs['GevApi'], 'GevQueryImageTransferStatus'):
    GevQueryImageTransferStatus = _libs['GevApi'].GevQueryImageTransferStatus
    GevQueryImageTransferStatus.argtypes = [GEV_CAMERA_HANDLE, PUINT32, PUINT32, PUINT32, PUINT32, POINTER(GevBufferCyclingMode)]
    GevQueryImageTransferStatus.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 582
if hasattr(_libs['GevApi'], 'GetPixelSizeInBytes'):
    GetPixelSizeInBytes = _libs['GevApi'].GetPixelSizeInBytes
    GetPixelSizeInBytes.argtypes = [UINT32]
    GetPixelSizeInBytes.restype = c_int

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 585
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'GevResetImageTransfer'):
        continue
    GevResetImageTransfer = _lib.GevResetImageTransfer
    GevResetImageTransfer.argtypes = [GEV_CAMERA_HANDLE]
    GevResetImageTransfer.restype = GEV_STATUS
    break

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 588
if hasattr(_libs['GevApi'], 'GevGetNextImage'):
    GevGetNextImage = _libs['GevApi'].GevGetNextImage
    GevGetNextImage.argtypes = [GEV_CAMERA_HANDLE, POINTER(POINTER(GEV_BUFFER_OBJECT)), POINTER(struct_timeval)]
    GevGetNextImage.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 589
if hasattr(_libs['GevApi'], 'GevGetImageBuffer'):
    GevGetImageBuffer = _libs['GevApi'].GevGetImageBuffer
    GevGetImageBuffer.argtypes = [GEV_CAMERA_HANDLE, POINTER(POINTER(None))]
    GevGetImageBuffer.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 590
if hasattr(_libs['GevApi'], 'GevGetImage'):
    GevGetImage = _libs['GevApi'].GevGetImage
    GevGetImage.argtypes = [GEV_CAMERA_HANDLE, POINTER(POINTER(GEV_BUFFER_OBJECT))]
    GevGetImage.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 591
if hasattr(_libs['GevApi'], 'GevWaitForNextImageBuffer'):
    GevWaitForNextImageBuffer = _libs['GevApi'].GevWaitForNextImageBuffer
    GevWaitForNextImageBuffer.argtypes = [GEV_CAMERA_HANDLE, POINTER(POINTER(None)), UINT32]
    GevWaitForNextImageBuffer.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 592
if hasattr(_libs['GevApi'], 'GevWaitForNextImage'):
    GevWaitForNextImage = _libs['GevApi'].GevWaitForNextImage
    GevWaitForNextImage.argtypes = [GEV_CAMERA_HANDLE, POINTER(POINTER(GEV_BUFFER_OBJECT)), UINT32]
    GevWaitForNextImage.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 594
if hasattr(_libs['GevApi'], 'GevReleaseImage'):
    GevReleaseImage = _libs['GevApi'].GevReleaseImage
    GevReleaseImage.argtypes = [GEV_CAMERA_HANDLE, POINTER(GEV_BUFFER_OBJECT)]
    GevReleaseImage.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 595
if hasattr(_libs['GevApi'], 'GevReleaseImageBuffer'):
    GevReleaseImageBuffer = _libs['GevApi'].GevReleaseImageBuffer
    GevReleaseImageBuffer.argtypes = [GEV_CAMERA_HANDLE, POINTER(None)]
    GevReleaseImageBuffer.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 599
if hasattr(_libs['GevApi'], 'GevRegisterEventCallback'):
    GevRegisterEventCallback = _libs['GevApi'].GevRegisterEventCallback
    GevRegisterEventCallback.argtypes = [GEV_CAMERA_HANDLE, UINT32, GEVEVENT_CBFUNCTION, POINTER(None)]
    GevRegisterEventCallback.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 600
if hasattr(_libs['GevApi'], 'GevRegisterApplicationEvent'):
    GevRegisterApplicationEvent = _libs['GevApi'].GevRegisterApplicationEvent
    GevRegisterApplicationEvent.argtypes = [GEV_CAMERA_HANDLE, UINT32, HANDLE]
    GevRegisterApplicationEvent.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 601
if hasattr(_libs['GevApi'], 'GevUnregisterEvent'):
    GevUnregisterEvent = _libs['GevApi'].GevUnregisterEvent
    GevUnregisterEvent.argtypes = [GEV_CAMERA_HANDLE, UINT32]
    GevUnregisterEvent.restype = GEV_STATUS

enum_anon_121 = c_int # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 627

cameraUnknown = 0 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 627

cameraGenieMono = 1 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 627

cameraGenieColor = 2 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 627

cameraGenieHM = 3 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 627

cameraDracoBased = 4 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 627

cameraSpyder3SG114K = 5 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 627

cameraSpyder3SG111K = 6 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 627

cameraSpyder3SG144K = 7 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 627

cameraSpyder3SG324K = 8 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 627

cameraSpyder3SG344K = 9 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 627

cameraGenieTS = 10 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 627

cameraXMLBased = 11 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 627

cameraType = enum_anon_121 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 627

PGENICAM_FEATURE = POINTER(None) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 637

enum_anon_122 = c_int # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 644

RO = 1 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 644

WO = 2 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 644

RW = 3 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 644

RegAccess = enum_anon_122 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 644

enum_anon_123 = c_int # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 659

stringReg = 0 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 659

floatReg = (stringReg + 1) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 659

integerReg = (floatReg + 1) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 659

bitReg = (integerReg + 1) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 659

fixedVal = (bitReg + 1) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 659

intVal = (fixedVal + 1) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 659

floatVal = (intVal + 1) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 659

dataArea = (floatVal + 1) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 659

floatRegLE = (dataArea + 1) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 659

integerRegLE = (floatRegLE + 1) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 659

bitRegLE = (integerRegLE + 1) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 659

RegType = enum_anon_123 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 659

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 665
class struct_anon_124(Structure):
    pass

struct_anon_124.__slots__ = [
    'name',
    'value',
]
struct_anon_124._fields_ = [
    ('name', c_char * 64),
    ('value', UINT32),
]

ENUM_ENTRY = struct_anon_124 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 665

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 661
class struct_anon_125(Structure):
    pass

struct_anon_125.__slots__ = [
    'name',
    'value',
]
struct_anon_125._fields_ = [
    ('name', c_char * 64),
    ('value', UINT32),
]

PENUM_ENTRY = POINTER(struct_anon_125) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 665

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 672
class union_anon_126(Union):
    pass

union_anon_126.__slots__ = [
    'bitIndex',
    'intValue',
    'floatValue',
]
union_anon_126._fields_ = [
    ('bitIndex', UINT32),
    ('intValue', UINT32),
    ('floatValue', c_float),
]

GENIREG_VALUE = union_anon_126 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 672

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 695
class struct_anon_127(Structure):
    pass

struct_anon_127.__slots__ = [
    'featureName',
    'address',
    'accessMode',
    'available',
    'type',
    'regSize',
    'regStride',
    'minSelector',
    'maxSelector',
    'value',
    'minValue',
    'maxValue',
    'readMask',
    'writeMask',
    'feature',
    'selectorName',
    'indexName',
]
struct_anon_127._fields_ = [
    ('featureName', c_char * 64),
    ('address', UINT32),
    ('accessMode', RegAccess),
    ('available', BOOL32),
    ('type', RegType),
    ('regSize', UINT32),
    ('regStride', UINT32),
    ('minSelector', UINT32),
    ('maxSelector', UINT32),
    ('value', GENIREG_VALUE),
    ('minValue', GENIREG_VALUE),
    ('maxValue', GENIREG_VALUE),
    ('readMask', UINT32),
    ('writeMask', UINT32),
    ('feature', PGENICAM_FEATURE),
    ('selectorName', c_char * 64),
    ('indexName', c_char * 64),
]

GEV_REGISTER = struct_anon_127 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 695

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 676
class struct_anon_128(Structure):
    pass

struct_anon_128.__slots__ = [
    'featureName',
    'address',
    'accessMode',
    'available',
    'type',
    'regSize',
    'regStride',
    'minSelector',
    'maxSelector',
    'value',
    'minValue',
    'maxValue',
    'readMask',
    'writeMask',
    'feature',
    'selectorName',
    'indexName',
]
struct_anon_128._fields_ = [
    ('featureName', c_char * 64),
    ('address', UINT32),
    ('accessMode', RegAccess),
    ('available', BOOL32),
    ('type', RegType),
    ('regSize', UINT32),
    ('regStride', UINT32),
    ('minSelector', UINT32),
    ('maxSelector', UINT32),
    ('value', GENIREG_VALUE),
    ('minValue', GENIREG_VALUE),
    ('maxValue', GENIREG_VALUE),
    ('readMask', UINT32),
    ('writeMask', UINT32),
    ('feature', PGENICAM_FEATURE),
    ('selectorName', c_char * 64),
    ('indexName', c_char * 64),
]

PGEV_REGISTER = POINTER(struct_anon_128) # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 695

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 953
class struct_anon_129(Structure):
    pass

struct_anon_129.__slots__ = [
    'DeviceVendorName',
    'DeviceModelName',
    'DeviceVersion',
    'DeviceFirmwareVersion',
    'DeviceID',
    'DeviceUserID',
    'DeviceScanType',
    'DeviceMaxThroughput',
    'DeviceRegistersStreamingStart',
    'DeviceRegistersStreamingEnd',
    'DeviceRegistersCheck',
    'DeviceRegistersValid',
    'SensorWidth',
    'SensorHeight',
    'WidthMax',
    'HeightMax',
    'Width',
    'Height',
    'OffsetX',
    'OffsetY',
    'LinePitch',
    'BinningHorizontal',
    'BinningVertical',
    'DecimationHorizontal',
    'DecimationVertical',
    'ReverseX',
    'ReverseY',
    'PixelColorFilter',
    'PixelCoding',
    'PixelSize',
    'PixelFormat',
    'PixelDynamicRangeMin',
    'PixelDynamicRangeMax',
    'TestImageSelector',
    'AcquisitionMode',
    'AcquisitionStart',
    'AcquisitionStop',
    'AcquisitionAbort',
    'AcquisitionArm',
    'AcquisitionFrameCount',
    'AcquisitionFrameRateMax',
    'AcquisitionFrameRateMin',
    'AcquisitionFrameRateRaw',
    'AcquisitionFrameRateAbs',
    'AcquisitionLineRateRaw',
    'AcquisitionLineRateAbs',
    'AcquisitionStatusSelector',
    'AcquisitionStatus',
    'TriggerSelector',
    'TriggerMode',
    'TriggerSoftware',
    'TriggerSource',
    'TriggerActivation',
    'TriggerOverlap',
    'TriggerDelayAbs',
    'TriggerDelayRaw',
    'TriggerDivider',
    'TriggerMultiplier',
    'ExposureMode',
    'ExposureAlignment',
    'ExposureDelay',
    'ExposureTimeRaw',
    'ExposureTimeAbs',
    'ExposureAuto',
    'ExposureTimeMin',
    'ExposureTimeMax',
    'LineSelector',
    'LineMode',
    'LineInverter',
    'LineStatus',
    'LineStatusAll',
    'LineSource',
    'OutputLineEventSource',
    'LineFormat',
    'UserOutputValue',
    'OutputLineValue',
    'UserOutputSelector',
    'UserOutputValueAll',
    'UserOutputValueAllMask',
    'InputLinePolarity',
    'InputLineDebouncingPeriod',
    'OutputLinePulsePolarity',
    'OutputLineMode',
    'OutputLinePulseDelay',
    'OutputLinePulseDuration',
    'CounterSelector',
    'CounterEventSource',
    'CounterLineSource',
    'CounterReset',
    'CounterValue',
    'CounterValueAtReset',
    'CounterDuration',
    'CounterStatus',
    'CounterTriggerSource',
    'CounterTriggerActivation',
    'TimerSelector',
    'TimerDurationAbs',
    'TimerDurationRaw',
    'TimerDelayAbs',
    'TimerDelayRaw',
    'TimerValueAbs',
    'TimerValueRaw',
    'TimerStatus',
    'TimerTriggerSource',
    'TimerTriggerActivation',
    'EventSelector',
    'EventNotification',
    'GainSelector',
    'GainRaw',
    'GainAbs',
    'GainAuto',
    'GainAutoBalance',
    'BlackLevelSelector',
    'BlackLevelRaw',
    'BlackLevelAbs',
    'BlackLevelAuto',
    'BlackLevelAutoBalance',
    'WhiteClipSelector',
    'WhiteClipRaw',
    'WhiteClipAbs',
    'BalanceRatioSelector',
    'BalanceRatioAbs',
    'BalanceWhiteAuto',
    'Gamma',
    'LUTSelector',
    'LUTEnable',
    'LUTIndex',
    'LUTValue',
    'LUTValueAll',
    'UserSetDefaultSelector',
    'UserSetSelector',
    'UserSetLoad',
    'UserSetSave',
    'PayloadSize',
    'GevSupportedIPConfigurationLLA',
    'GevSupportedIPConfigurationDHCP',
    'GevSupportedIPConfigurationPersistentIP',
    'GevCurrentIPConfigurationLLA',
    'GevCurrentIPConfigurationDHCP',
    'GevCurrentIPConfigurationPersistentIP',
    'GevCurrentIPConfiguration',
    'GevCurrentIPAddress',
    'GevCurrentSubnetMask',
    'GevCurrentDefaultGateway',
    'GevPersistentIPAddress',
    'GevPersistentSubnetMask',
    'GevPersistentDefaultGateway',
    'GevFirstURL',
    'GevSecondURL',
    'GevNumberOfInterfaces',
    'GevLinkSpeed',
    'GevIPConfigurationStatus',
    'ChunkModeActive',
    'ChunkSelector',
    'ChunkEnable',
    'ChunkOffsetX',
    'ChunkOffsetY',
    'ChunkWidth',
    'ChunkHeight',
    'ChunkPixelFormat',
    'ChunkDynamicRangeMax',
    'ChunkDynamicRangeMin',
    'ChunkTimestamp',
    'ChunkLineStatusAll',
    'ChunkCounterSelector',
    'ChunkCounter',
    'ChunkTimerSelector',
    'ChunkTimer',
    'FileSelector',
    'FileOperationSelector',
    'FileOperationExecute',
    'FileOpenModeSelector',
    'FileAccessOffset',
    'FileAccessLength',
    'FileAccessBuffer',
    'FileOperationStatus',
    'FileOperationResult',
    'FileSize',
]
struct_anon_129._fields_ = [
    ('DeviceVendorName', GEV_REGISTER),
    ('DeviceModelName', GEV_REGISTER),
    ('DeviceVersion', GEV_REGISTER),
    ('DeviceFirmwareVersion', GEV_REGISTER),
    ('DeviceID', GEV_REGISTER),
    ('DeviceUserID', GEV_REGISTER),
    ('DeviceScanType', GEV_REGISTER),
    ('DeviceMaxThroughput', GEV_REGISTER),
    ('DeviceRegistersStreamingStart', GEV_REGISTER),
    ('DeviceRegistersStreamingEnd', GEV_REGISTER),
    ('DeviceRegistersCheck', GEV_REGISTER),
    ('DeviceRegistersValid', GEV_REGISTER),
    ('SensorWidth', GEV_REGISTER),
    ('SensorHeight', GEV_REGISTER),
    ('WidthMax', GEV_REGISTER),
    ('HeightMax', GEV_REGISTER),
    ('Width', GEV_REGISTER),
    ('Height', GEV_REGISTER),
    ('OffsetX', GEV_REGISTER),
    ('OffsetY', GEV_REGISTER),
    ('LinePitch', GEV_REGISTER),
    ('BinningHorizontal', GEV_REGISTER),
    ('BinningVertical', GEV_REGISTER),
    ('DecimationHorizontal', GEV_REGISTER),
    ('DecimationVertical', GEV_REGISTER),
    ('ReverseX', GEV_REGISTER),
    ('ReverseY', GEV_REGISTER),
    ('PixelColorFilter', GEV_REGISTER),
    ('PixelCoding', GEV_REGISTER),
    ('PixelSize', GEV_REGISTER),
    ('PixelFormat', GEV_REGISTER),
    ('PixelDynamicRangeMin', GEV_REGISTER),
    ('PixelDynamicRangeMax', GEV_REGISTER),
    ('TestImageSelector', GEV_REGISTER),
    ('AcquisitionMode', GEV_REGISTER),
    ('AcquisitionStart', GEV_REGISTER),
    ('AcquisitionStop', GEV_REGISTER),
    ('AcquisitionAbort', GEV_REGISTER),
    ('AcquisitionArm', GEV_REGISTER),
    ('AcquisitionFrameCount', GEV_REGISTER),
    ('AcquisitionFrameRateMax', GEV_REGISTER),
    ('AcquisitionFrameRateMin', GEV_REGISTER),
    ('AcquisitionFrameRateRaw', GEV_REGISTER),
    ('AcquisitionFrameRateAbs', GEV_REGISTER),
    ('AcquisitionLineRateRaw', GEV_REGISTER),
    ('AcquisitionLineRateAbs', GEV_REGISTER),
    ('AcquisitionStatusSelector', GEV_REGISTER),
    ('AcquisitionStatus', GEV_REGISTER),
    ('TriggerSelector', GEV_REGISTER),
    ('TriggerMode', GEV_REGISTER),
    ('TriggerSoftware', GEV_REGISTER),
    ('TriggerSource', GEV_REGISTER),
    ('TriggerActivation', GEV_REGISTER),
    ('TriggerOverlap', GEV_REGISTER),
    ('TriggerDelayAbs', GEV_REGISTER),
    ('TriggerDelayRaw', GEV_REGISTER),
    ('TriggerDivider', GEV_REGISTER),
    ('TriggerMultiplier', GEV_REGISTER),
    ('ExposureMode', GEV_REGISTER),
    ('ExposureAlignment', GEV_REGISTER),
    ('ExposureDelay', GEV_REGISTER),
    ('ExposureTimeRaw', GEV_REGISTER),
    ('ExposureTimeAbs', GEV_REGISTER),
    ('ExposureAuto', GEV_REGISTER),
    ('ExposureTimeMin', GEV_REGISTER),
    ('ExposureTimeMax', GEV_REGISTER),
    ('LineSelector', GEV_REGISTER),
    ('LineMode', GEV_REGISTER),
    ('LineInverter', GEV_REGISTER),
    ('LineStatus', GEV_REGISTER),
    ('LineStatusAll', GEV_REGISTER),
    ('LineSource', GEV_REGISTER),
    ('OutputLineEventSource', GEV_REGISTER),
    ('LineFormat', GEV_REGISTER),
    ('UserOutputValue', GEV_REGISTER),
    ('OutputLineValue', GEV_REGISTER),
    ('UserOutputSelector', GEV_REGISTER),
    ('UserOutputValueAll', GEV_REGISTER),
    ('UserOutputValueAllMask', GEV_REGISTER),
    ('InputLinePolarity', GEV_REGISTER),
    ('InputLineDebouncingPeriod', GEV_REGISTER),
    ('OutputLinePulsePolarity', GEV_REGISTER),
    ('OutputLineMode', GEV_REGISTER),
    ('OutputLinePulseDelay', GEV_REGISTER),
    ('OutputLinePulseDuration', GEV_REGISTER),
    ('CounterSelector', GEV_REGISTER),
    ('CounterEventSource', GEV_REGISTER),
    ('CounterLineSource', GEV_REGISTER),
    ('CounterReset', GEV_REGISTER),
    ('CounterValue', GEV_REGISTER),
    ('CounterValueAtReset', GEV_REGISTER),
    ('CounterDuration', GEV_REGISTER),
    ('CounterStatus', GEV_REGISTER),
    ('CounterTriggerSource', GEV_REGISTER),
    ('CounterTriggerActivation', GEV_REGISTER),
    ('TimerSelector', GEV_REGISTER),
    ('TimerDurationAbs', GEV_REGISTER),
    ('TimerDurationRaw', GEV_REGISTER),
    ('TimerDelayAbs', GEV_REGISTER),
    ('TimerDelayRaw', GEV_REGISTER),
    ('TimerValueAbs', GEV_REGISTER),
    ('TimerValueRaw', GEV_REGISTER),
    ('TimerStatus', GEV_REGISTER),
    ('TimerTriggerSource', GEV_REGISTER),
    ('TimerTriggerActivation', GEV_REGISTER),
    ('EventSelector', GEV_REGISTER),
    ('EventNotification', GEV_REGISTER),
    ('GainSelector', GEV_REGISTER),
    ('GainRaw', GEV_REGISTER),
    ('GainAbs', GEV_REGISTER),
    ('GainAuto', GEV_REGISTER),
    ('GainAutoBalance', GEV_REGISTER),
    ('BlackLevelSelector', GEV_REGISTER),
    ('BlackLevelRaw', GEV_REGISTER),
    ('BlackLevelAbs', GEV_REGISTER),
    ('BlackLevelAuto', GEV_REGISTER),
    ('BlackLevelAutoBalance', GEV_REGISTER),
    ('WhiteClipSelector', GEV_REGISTER),
    ('WhiteClipRaw', GEV_REGISTER),
    ('WhiteClipAbs', GEV_REGISTER),
    ('BalanceRatioSelector', GEV_REGISTER),
    ('BalanceRatioAbs', GEV_REGISTER),
    ('BalanceWhiteAuto', GEV_REGISTER),
    ('Gamma', GEV_REGISTER),
    ('LUTSelector', GEV_REGISTER),
    ('LUTEnable', GEV_REGISTER),
    ('LUTIndex', GEV_REGISTER),
    ('LUTValue', GEV_REGISTER),
    ('LUTValueAll', GEV_REGISTER),
    ('UserSetDefaultSelector', GEV_REGISTER),
    ('UserSetSelector', GEV_REGISTER),
    ('UserSetLoad', GEV_REGISTER),
    ('UserSetSave', GEV_REGISTER),
    ('PayloadSize', GEV_REGISTER),
    ('GevSupportedIPConfigurationLLA', GEV_REGISTER),
    ('GevSupportedIPConfigurationDHCP', GEV_REGISTER),
    ('GevSupportedIPConfigurationPersistentIP', GEV_REGISTER),
    ('GevCurrentIPConfigurationLLA', GEV_REGISTER),
    ('GevCurrentIPConfigurationDHCP', GEV_REGISTER),
    ('GevCurrentIPConfigurationPersistentIP', GEV_REGISTER),
    ('GevCurrentIPConfiguration', GEV_REGISTER),
    ('GevCurrentIPAddress', GEV_REGISTER),
    ('GevCurrentSubnetMask', GEV_REGISTER),
    ('GevCurrentDefaultGateway', GEV_REGISTER),
    ('GevPersistentIPAddress', GEV_REGISTER),
    ('GevPersistentSubnetMask', GEV_REGISTER),
    ('GevPersistentDefaultGateway', GEV_REGISTER),
    ('GevFirstURL', GEV_REGISTER),
    ('GevSecondURL', GEV_REGISTER),
    ('GevNumberOfInterfaces', GEV_REGISTER),
    ('GevLinkSpeed', GEV_REGISTER),
    ('GevIPConfigurationStatus', GEV_REGISTER),
    ('ChunkModeActive', GEV_REGISTER),
    ('ChunkSelector', GEV_REGISTER),
    ('ChunkEnable', GEV_REGISTER),
    ('ChunkOffsetX', GEV_REGISTER),
    ('ChunkOffsetY', GEV_REGISTER),
    ('ChunkWidth', GEV_REGISTER),
    ('ChunkHeight', GEV_REGISTER),
    ('ChunkPixelFormat', GEV_REGISTER),
    ('ChunkDynamicRangeMax', GEV_REGISTER),
    ('ChunkDynamicRangeMin', GEV_REGISTER),
    ('ChunkTimestamp', GEV_REGISTER),
    ('ChunkLineStatusAll', GEV_REGISTER),
    ('ChunkCounterSelector', GEV_REGISTER),
    ('ChunkCounter', GEV_REGISTER),
    ('ChunkTimerSelector', GEV_REGISTER),
    ('ChunkTimer', GEV_REGISTER),
    ('FileSelector', GEV_REGISTER),
    ('FileOperationSelector', GEV_REGISTER),
    ('FileOperationExecute', GEV_REGISTER),
    ('FileOpenModeSelector', GEV_REGISTER),
    ('FileAccessOffset', GEV_REGISTER),
    ('FileAccessLength', GEV_REGISTER),
    ('FileAccessBuffer', GEV_REGISTER),
    ('FileOperationStatus', GEV_REGISTER),
    ('FileOperationResult', GEV_REGISTER),
    ('FileSize', GEV_REGISTER),
]

DALSA_GENICAM_GIGE_REGS = struct_anon_129 # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 953

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 962
if hasattr(_libs['GevApi'], 'GevGetCameraRegisters'):
    GevGetCameraRegisters = _libs['GevApi'].GevGetCameraRegisters
    GevGetCameraRegisters.argtypes = [GEV_CAMERA_HANDLE, POINTER(DALSA_GENICAM_GIGE_REGS), c_int]
    GevGetCameraRegisters.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 963
if hasattr(_libs['GevApi'], 'GevSetCameraRegInfo'):
    GevSetCameraRegInfo = _libs['GevApi'].GevSetCameraRegInfo
    GevSetCameraRegInfo.argtypes = [GEV_CAMERA_HANDLE, cameraType, BOOL, POINTER(DALSA_GENICAM_GIGE_REGS), c_int]
    GevSetCameraRegInfo.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 965
if hasattr(_libs['GevApi'], 'GevInitCameraRegisters'):
    GevInitCameraRegisters = _libs['GevApi'].GevInitCameraRegisters
    GevInitCameraRegisters.argtypes = [GEV_CAMERA_HANDLE]
    GevInitCameraRegisters.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 967
if hasattr(_libs['GevApi'], 'GevGetNumberOfRegisters'):
    GevGetNumberOfRegisters = _libs['GevApi'].GevGetNumberOfRegisters
    GevGetNumberOfRegisters.argtypes = [GEV_CAMERA_HANDLE, POINTER(UINT32)]
    GevGetNumberOfRegisters.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 968
if hasattr(_libs['GevApi'], 'GevGetRegisterNameByIndex'):
    GevGetRegisterNameByIndex = _libs['GevApi'].GevGetRegisterNameByIndex
    GevGetRegisterNameByIndex.argtypes = [GEV_CAMERA_HANDLE, UINT32, c_int, String]
    GevGetRegisterNameByIndex.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 969
if hasattr(_libs['GevApi'], 'GevGetRegisterByName'):
    GevGetRegisterByName = _libs['GevApi'].GevGetRegisterByName
    GevGetRegisterByName.argtypes = [GEV_CAMERA_HANDLE, String, POINTER(GEV_REGISTER)]
    GevGetRegisterByName.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 970
if hasattr(_libs['GevApi'], 'GevGetRegisterPtrByName'):
    GevGetRegisterPtrByName = _libs['GevApi'].GevGetRegisterPtrByName
    GevGetRegisterPtrByName.argtypes = [GEV_CAMERA_HANDLE, String, POINTER(POINTER(GEV_REGISTER))]
    GevGetRegisterPtrByName.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 971
if hasattr(_libs['GevApi'], 'GevGetRegisterByIndex'):
    GevGetRegisterByIndex = _libs['GevApi'].GevGetRegisterByIndex
    GevGetRegisterByIndex.argtypes = [GEV_CAMERA_HANDLE, UINT32, POINTER(GEV_REGISTER)]
    GevGetRegisterByIndex.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 972
if hasattr(_libs['GevApi'], 'GevGetRegisterPtrByIndex'):
    GevGetRegisterPtrByIndex = _libs['GevApi'].GevGetRegisterPtrByIndex
    GevGetRegisterPtrByIndex.argtypes = [GEV_CAMERA_HANDLE, UINT32, POINTER(POINTER(GEV_REGISTER))]
    GevGetRegisterPtrByIndex.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 974
if hasattr(_libs['GevApi'], 'GevReadRegisterByName'):
    GevReadRegisterByName = _libs['GevApi'].GevReadRegisterByName
    GevReadRegisterByName.argtypes = [GEV_CAMERA_HANDLE, String, c_int, UINT32, POINTER(None)]
    GevReadRegisterByName.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 975
if hasattr(_libs['GevApi'], 'GevWriteRegisterByName'):
    GevWriteRegisterByName = _libs['GevApi'].GevWriteRegisterByName
    GevWriteRegisterByName.argtypes = [GEV_CAMERA_HANDLE, String, c_int, UINT32, POINTER(None)]
    GevWriteRegisterByName.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 977
if hasattr(_libs['GevApi'], 'GevRegisterRead'):
    GevRegisterRead = _libs['GevApi'].GevRegisterRead
    GevRegisterRead.argtypes = [GEV_CAMERA_HANDLE, POINTER(GEV_REGISTER), c_int, UINT32, POINTER(None)]
    GevRegisterRead.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 978
if hasattr(_libs['GevApi'], 'GevRegisterWrite'):
    GevRegisterWrite = _libs['GevApi'].GevRegisterWrite
    GevRegisterWrite.argtypes = [GEV_CAMERA_HANDLE, POINTER(GEV_REGISTER), c_int, UINT32, POINTER(None)]
    GevRegisterWrite.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 979
if hasattr(_libs['GevApi'], 'GevRegisterWriteNoWait'):
    GevRegisterWriteNoWait = _libs['GevApi'].GevRegisterWriteNoWait
    GevRegisterWriteNoWait.argtypes = [GEV_CAMERA_HANDLE, POINTER(GEV_REGISTER), c_int, UINT32, POINTER(None)]
    GevRegisterWriteNoWait.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 981
if hasattr(_libs['GevApi'], 'GevRegisterWriteArray'):
    GevRegisterWriteArray = _libs['GevApi'].GevRegisterWriteArray
    GevRegisterWriteArray.argtypes = [GEV_CAMERA_HANDLE, POINTER(GEV_REGISTER), c_int, UINT32, UINT32, POINTER(None)]
    GevRegisterWriteArray.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 982
if hasattr(_libs['GevApi'], 'GevRegisterReadArray'):
    GevRegisterReadArray = _libs['GevApi'].GevRegisterReadArray
    GevRegisterReadArray.argtypes = [GEV_CAMERA_HANDLE, POINTER(GEV_REGISTER), c_int, UINT32, UINT32, POINTER(None)]
    GevRegisterReadArray.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 984
if hasattr(_libs['GevApi'], 'GevRegisterWriteInt'):
    GevRegisterWriteInt = _libs['GevApi'].GevRegisterWriteInt
    GevRegisterWriteInt.argtypes = [GEV_CAMERA_HANDLE, POINTER(GEV_REGISTER), c_int, UINT32]
    GevRegisterWriteInt.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 985
if hasattr(_libs['GevApi'], 'GevRegisterReadInt'):
    GevRegisterReadInt = _libs['GevApi'].GevRegisterReadInt
    GevRegisterReadInt.argtypes = [GEV_CAMERA_HANDLE, POINTER(GEV_REGISTER), c_int, POINTER(UINT32)]
    GevRegisterReadInt.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 986
if hasattr(_libs['GevApi'], 'GevRegisterWriteFloat'):
    GevRegisterWriteFloat = _libs['GevApi'].GevRegisterWriteFloat
    GevRegisterWriteFloat.argtypes = [GEV_CAMERA_HANDLE, POINTER(GEV_REGISTER), c_int, c_float]
    GevRegisterWriteFloat.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 987
if hasattr(_libs['GevApi'], 'GevRegisterReadFloat'):
    GevRegisterReadFloat = _libs['GevApi'].GevRegisterReadFloat
    GevRegisterReadFloat.argtypes = [GEV_CAMERA_HANDLE, POINTER(GEV_REGISTER), c_int, POINTER(c_float)]
    GevRegisterReadFloat.restype = GEV_STATUS

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 46
try:
    GENICAM_TARGET_ROOT_VERSION = 'GENICAM_ROOT_V3_0'
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 47
try:
    GIGEV_XML_DOWNLOAD = 'GIGEV_XML_DOWNLOAD'
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 65
try:
    GEV_LOG_LEVEL_OFF = 0
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 66
try:
    GEV_LOG_LEVEL_NORMAL = 1
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 67
try:
    GEV_LOG_LEVEL_ERRORS = 1
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 68
try:
    GEV_LOG_LEVEL_WARNINGS = 2
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 69
try:
    GEV_LOG_LEVEL_DEBUG = 3
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 70
try:
    GEV_LOG_LEVEL_TRACE = 4
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 72
try:
    GEV_LOG_FATAL = 0
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 73
try:
    GEV_LOG_ERROR = 1
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 74
try:
    GEV_LOG_WARNING = 2
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 75
try:
    GEV_LOG_INFO = 3
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 76
try:
    GEV_LOG_TRACE = 4
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 81
try:
    GEVLIB_OK = 0
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 82
try:
    GEVLIB_SUCCESS = GEVLIB_OK
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 83
try:
    GEVLIB_STATUS_SUCCESS = GEVLIB_OK
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 84
try:
    GEVLIB_STATUS_ERROR = (-1)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 87
try:
    GEVLIB_ERROR_GENERIC = (-1)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 88
try:
    GEVLIB_ERROR_NULL_PTR = (-2)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 89
try:
    GEVLIB_ERROR_ARG_INVALID = (-3)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 90
try:
    GEVLIB_ERROR_INVALID_HANDLE = (-4)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 91
try:
    GEVLIB_ERROR_NOT_SUPPORTED = (-5)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 92
try:
    GEVLIB_ERROR_TIME_OUT = (-6)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 93
try:
    GEVLIB_ERROR_NOT_IMPLEMENTED = (-10)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 94
try:
    GEVLIB_ERROR_NO_CAMERA = (-11)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 95
try:
    GEVLIB_ERROR_INVALID_PIXEL_FORMAT = (-12)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 96
try:
    GEVLIB_ERROR_PARAMETER_INVALID = (-13)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 97
try:
    GEVLIB_ERROR_SOFTWARE = (-14)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 98
try:
    GEVLIB_ERROR_API_NOT_INITIALIZED = (-15)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 99
try:
    GEVLIB_ERROR_DEVICE_NOT_FOUND = (-16)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 100
try:
    GEVLIB_ERROR_ACCESS_DENIED = (-17)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 101
try:
    GEVLIB_ERROR_NOT_AVAILABLE = (-18)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 102
try:
    GEVLIB_ERROR_NO_SPACE = (-19)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 105
try:
    GEVLIB_ERROR_SYSTEM_RESOURCE = (-2001)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 106
try:
    GEVLIB_ERROR_INSUFFICIENT_MEMORY = (-2002)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 107
try:
    GEVLIB_ERROR_INSUFFICIENT_BANDWIDTH = (-2003)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 108
try:
    GEVLIB_ERROR_RESOURCE_NOT_ALLOCATED = (-2004)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 109
try:
    GEVLIB_ERROR_RESOURCE_IN_USE = (-2005)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 110
try:
    GEVLIB_ERROR_RESOURCE_NOT_ENABLED = (-2006)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 111
try:
    GEVLIB_ERROR_RESOURCE_NOT_INITIALIZED = (-2007)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 112
try:
    GEVLIB_ERROR_RESOURCE_CORRUPTED = (-2008)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 113
try:
    GEVLIB_ERROR_RESOURCE_MISSING = (-2009)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 114
try:
    GEVLIB_ERROR_RESOURCE_LACK = (-2010)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 115
try:
    GEVLIB_ERROR_RESOURCE_ACCESS = (-2011)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 116
try:
    GEVLIB_ERROR_RESOURCE_INVALID = (-2012)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 117
try:
    GEVLIB_ERROR_RESOURCE_LOCK = (-2013)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 118
try:
    GEVLIB_ERROR_INSUFFICIENT_PRIVILEGE = (-2014)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 119
try:
    GEVLIB_ERROR_RESOURCE_WRITE_PROTECTED = (-2015)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 120
try:
    GEVLIB_ERROR_RESOURCE_INCOHERENCY = (-2016)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 123
try:
    GEVLIB_ERROR_DATA_NO_MESSAGES = (-5001)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 124
try:
    GEVLIB_ERROR_DATA_OVERFLOW = (-5002)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 125
try:
    GEVLIB_ERROR_DATA_CHECKSUM = (-5003)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 126
try:
    GEVLIB_ERROR_DATA_NOT_AVAILABLE = (-5004)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 127
try:
    GEVLIB_ERROR_DATA_OVERRUN = (-5005)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 128
try:
    GEVLIB_ERROR_DATA_XFER_ABORT = (-5006)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 129
try:
    GEVLIB_ERROR_DATA_INVALID_HEADER = (-5007)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 130
try:
    GEVLIB_ERROR_DATA_ALIGNMENT = (-5008)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 133
try:
    GEVLIB_ERROR_CONNECTION_DROPPED = (-11000)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 134
try:
    GEVLIB_ERROR_ANSWER_TIMEOUT = (-11001)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 135
try:
    GEVLIB_ERROR_SOCKET_INVALID = (-11002)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 136
try:
    GEVLIB_ERROR_PORT_NOT_AVAILABLE = (-11003)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 137
try:
    GEVLIB_ERROR_INVALID_IP = (-11004)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 138
try:
    GEVLIB_ERROR_INVALID_CAMERA_OPERATION = (-11005)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 139
try:
    GEVLIB_ERROR_INVALID_PACKET = (-11006)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 140
try:
    GEVLIB_ERROR_INVALID_CONNECTION_ATTEMPT = (-11007)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 141
try:
    GEVLIB_ERROR_PROTOCOL = (-11008)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 142
try:
    GEVLIB_ERROR_WINDOWS_SOCKET_INIT = (-11009)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 143
try:
    GEVLIB_ERROR_WINDOWS_SOCKET_CLOSE = (-11010)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 144
try:
    GEVLIB_ERROR_SOCKET_CREATE = (-11011)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 145
try:
    GEVLIB_ERROR_SOCKET_RELEASE = (-11012)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 146
try:
    GEVLIB_ERROR_SOCKET_DATA_SEND = (-11013)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 147
try:
    GEVLIB_ERROR_SOCKET_DATA_READ = (-11014)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 148
try:
    GEVLIB_ERROR_SOCKET_WAIT_ACKNOWLEDGE = (-11015)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 149
try:
    GEVLIB_ERROR_INVALID_INTERNAL_COMMAND = (-11016)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 150
try:
    GEVLIB_ERROR_INVALID_ACKNOWLEDGE = (-11017)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 151
try:
    GEVLIB_ERROR_PREVIOUS_ACKNOWLEDGE = (-11018)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 152
try:
    GEVLIB_ERROR_INVALID_MESSAGE = (-11019)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 153
try:
    GEVLIB_ERROR_GIGE_ERROR = (-11020)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 159
try:
    GEV_STATUS_SUCCESS = 0
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 160
try:
    GEV_STATUS_NOT_IMPLEMENTED = 32769
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 161
try:
    GEV_STATUS_INVALID_PARAMETER = 32770
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 162
try:
    GEV_STATUS_INVALID_ADDRESS = 32771
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 163
try:
    GEV_STATUS_WRITE_PROTECT = 32772
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 164
try:
    GEV_STATUS_BAD_ALIGNMENT = 32773
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 165
try:
    GEV_STATUS_ACCESS_DENIED = 32774
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 166
try:
    GEV_STATUS_BUSY = 32775
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 167
try:
    GEV_STATUS_LOCAL_PROBLEM = 32776
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 168
try:
    GEV_STATUS_MSG_MISMATCH = 32777
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 169
try:
    GEV_STATUS_INVALID_PROTOCOL = 32778
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 170
try:
    GEV_STATUS_NO_MSG = 32779
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 171
try:
    GEV_STATUS_PACKET_UNAVAILABLE = 32780
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 172
try:
    GEV_STATUS_DATA_OVERRUN = 32781
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 173
try:
    GEV_STATUS_INVALID_HEADER = 32782
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 175
try:
    GEV_STATUS_ERROR = 36863
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 233
try:
    GEV_PIXFORMAT_ISMONO = 16777216
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 234
try:
    GEV_PIXFORMAT_ISCOLOR = 33554432
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 235
try:
    GEV_PIXFORMAT_ISCUSTOM = 2147483648
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 237
try:
    GEV_PIXEL_FORMAT_MONO = 1
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 238
try:
    GEV_PIXEL_FORMAT_MONO_PACKED = 2
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 239
try:
    GEV_PIXEL_FORMAT_RGB = 4
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 240
try:
    GEV_PIXEL_FORMAT_RGB_PACKED = 8
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 241
try:
    GEV_PIXEL_FORMAT_BAYER = 16
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 242
try:
    GEV_PIXEL_FORMAT_YUV = 32
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 243
try:
    GEV_PIXEL_FORMAT_RGB_PLANAR = 64
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 245
try:
    GEV_PIXEL_ORDER_NONE = 0
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 246
try:
    GEV_PIXEL_ORDER_RGB = 1
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 247
try:
    GEV_PIXEL_ORDER_BGR = 2
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 248
try:
    GEV_PIXEL_ORDER_GRB = 4
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 249
try:
    GEV_PIXEL_ORDER_GBR = 8
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 250
try:
    GEV_PIXEL_ORDER_RGB10V1 = 61440
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 251
try:
    GEV_PIXEL_ORDER_RGB10V2 = 57344
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 314
try:
    MAX_GEVSTRING_LENGTH = 64
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 356
try:
    GEV_FRAME_STATUS_RECVD = 0
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 357
try:
    GEV_FRAME_STATUS_PENDING = 1
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 358
try:
    GEV_FRAME_STATUS_TIMEOUT = 2
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 359
try:
    GEV_FRAME_STATUS_OVERFLOW = 3
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 360
try:
    GEV_FRAME_STATUS_BANDWIDTH = 4
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 361
try:
    GEV_FRAME_STATUS_LOST = 5
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 362
try:
    GEV_FRAME_STATUS_RELEASED = (-1)
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 471
try:
    GENAPI_UNUSED_TYPE = 1
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 472
try:
    GENAPI_VALUE_TYPE = 0
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 473
try:
    GENAPI_BASE_TYPE = 1
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 474
try:
    GENAPI_INTEGER_TYPE = 2
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 475
try:
    GENAPI_BOOLEAN_TYPE = 3
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 476
try:
    GENAPI_COMMAND_TYPE = 4
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 477
try:
    GENAPI_FLOAT_TYPE = 5
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 478
try:
    GENAPI_STRING_TYPE = 6
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 479
try:
    GENAPI_REGISTER_TYPE = 7
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 480
try:
    GENAPI_CATEGORY_TYPE = 8
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 481
try:
    GENAPI_ENUM_TYPE = 9
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 482
try:
    GENAPI_ENUMENTRY_TYPE = 10
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 485
try:
    GENAPI_ACCESSMODE_NI = 0
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 486
try:
    GENAPI_ACCESSMODE_NA = 1
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 487
try:
    GENAPI_ACCESSMODE_WO = 2
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 488
try:
    GENAPI_ACCESSMODE_RO = 3
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 489
try:
    GENAPI_ACCESSMODE_RW = 4
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 490
try:
    GENAPI_ACCESSMODE_NONE = 5
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 493
try:
    GENAPI_VISIBILITY_BEGINNER = 0
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 494
try:
    GENAPI_VISIBILITY_EXPERT = 1
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 495
try:
    GENAPI_VISIBILITY_GURU = 2
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 496
try:
    GENAPI_VISIBILITY_INVISIBLE = 3
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 497
try:
    GENAPI_VISIBILITY_UNDEFINED = 99
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 500
try:
    GENAPI_INCREMENT_NONE = 0
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 501
try:
    GENAPI_INCREMENT_FIXED = 1
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 502
try:
    GENAPI_INCREMENT_LIST = 2
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 634
try:
    FEATURE_NAME_MAX_SIZE = 64
except:
    pass

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 635
try:
    NOREF_ADDR = 0
except:
    pass

_tag_GEVBUF_ENTRY = struct__tag_GEVBUF_ENTRY # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 354

_GEVBUF_QUEUE = struct__GEVBUF_QUEUE # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevapi.h: 388

# No inserted files

