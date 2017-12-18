'''Wrapper for gevoslib.h

Generated with:
/home/wasonj/.local/bin/ctypesgen.py -lGevApi gevoslib.h -o gevoslib.py

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

UINT16 = u_int16_t # /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/cordef.h: 801

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

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 68
if hasattr(_libs['GevApi'], '_InitSocketAPI'):
    _InitSocketAPI = _libs['GevApi']._InitSocketAPI
    _InitSocketAPI.argtypes = []
    _InitSocketAPI.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 69
if hasattr(_libs['GevApi'], '_CloseSocketAPI'):
    _CloseSocketAPI = _libs['GevApi']._CloseSocketAPI
    _CloseSocketAPI.argtypes = []
    _CloseSocketAPI.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 70
if hasattr(_libs['GevApi'], '_GetSocketError'):
    _GetSocketError = _libs['GevApi']._GetSocketError
    _GetSocketError.argtypes = []
    _GetSocketError.restype = c_int

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 73
if hasattr(_libs['GevApi'], '_GetMaxNetworkInterfaces'):
    _GetMaxNetworkInterfaces = _libs['GevApi']._GetMaxNetworkInterfaces
    _GetMaxNetworkInterfaces.argtypes = []
    _GetMaxNetworkInterfaces.restype = c_int

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 74
if hasattr(_libs['GevApi'], '_GetMacAddress'):
    _GetMacAddress = _libs['GevApi']._GetMacAddress
    _GetMacAddress.argtypes = [c_int, POINTER(UINT16), POINTER(UINT32), POINTER(UINT32), POINTER(UINT32)]
    _GetMacAddress.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 75
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_SetIPAddress'):
        continue
    _SetIPAddress = _lib._SetIPAddress
    _SetIPAddress.argtypes = [UINT32, UINT32]
    _SetIPAddress.restype = BOOL
    break

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 76
if hasattr(_libs['GevApi'], '_GetMTUSetting'):
    _GetMTUSetting = _libs['GevApi']._GetMTUSetting
    _GetMTUSetting.argtypes = [c_int, POINTER(c_int)]
    _GetMTUSetting.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 79
if hasattr(_libs['GevApi'], '_CreateEvent'):
    _CreateEvent = _libs['GevApi']._CreateEvent
    _CreateEvent.argtypes = [POINTER(HANDLE)]
    _CreateEvent.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 80
if hasattr(_libs['GevApi'], '_DestroyEvent'):
    _DestroyEvent = _libs['GevApi']._DestroyEvent
    _DestroyEvent.argtypes = [POINTER(HANDLE)]
    _DestroyEvent.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 81
if hasattr(_libs['GevApi'], '_WaitForEvent'):
    _WaitForEvent = _libs['GevApi']._WaitForEvent
    _WaitForEvent.argtypes = [POINTER(HANDLE), UINT32]
    _WaitForEvent.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 82
if hasattr(_libs['GevApi'], '_ClearEvent'):
    _ClearEvent = _libs['GevApi']._ClearEvent
    _ClearEvent.argtypes = [POINTER(HANDLE)]
    _ClearEvent.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 83
if hasattr(_libs['GevApi'], '_SetEvent'):
    _SetEvent = _libs['GevApi']._SetEvent
    _SetEvent.argtypes = [POINTER(HANDLE)]
    _SetEvent.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 86
if hasattr(_libs['GevApi'], '_CreateMutex'):
    _CreateMutex = _libs['GevApi']._CreateMutex
    _CreateMutex.argtypes = [POINTER(pthread_mutex_t)]
    _CreateMutex.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 87
if hasattr(_libs['GevApi'], '_DestroyMutex'):
    _DestroyMutex = _libs['GevApi']._DestroyMutex
    _DestroyMutex.argtypes = [POINTER(pthread_mutex_t)]
    _DestroyMutex.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 88
if hasattr(_libs['GevApi'], '_AcquireMutex'):
    _AcquireMutex = _libs['GevApi']._AcquireMutex
    _AcquireMutex.argtypes = [POINTER(pthread_mutex_t), UINT32]
    _AcquireMutex.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 89
if hasattr(_libs['GevApi'], '_ReleaseMutex'):
    _ReleaseMutex = _libs['GevApi']._ReleaseMutex
    _ReleaseMutex.argtypes = [POINTER(pthread_mutex_t)]
    _ReleaseMutex.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 92
if hasattr(_libs['GevApi'], '_InitCriticalSection'):
    _InitCriticalSection = _libs['GevApi']._InitCriticalSection
    _InitCriticalSection.argtypes = [POINTER(CRITICAL_SECTION)]
    _InitCriticalSection.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 93
if hasattr(_libs['GevApi'], '_ReleaseCriticalSection'):
    _ReleaseCriticalSection = _libs['GevApi']._ReleaseCriticalSection
    _ReleaseCriticalSection.argtypes = [POINTER(CRITICAL_SECTION)]
    _ReleaseCriticalSection.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 94
if hasattr(_libs['GevApi'], '_EnterCriticalSection'):
    _EnterCriticalSection = _libs['GevApi']._EnterCriticalSection
    _EnterCriticalSection.argtypes = [POINTER(CRITICAL_SECTION)]
    _EnterCriticalSection.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 95
if hasattr(_libs['GevApi'], '_LeaveCriticalSection'):
    _LeaveCriticalSection = _libs['GevApi']._LeaveCriticalSection
    _LeaveCriticalSection.argtypes = [POINTER(CRITICAL_SECTION)]
    _LeaveCriticalSection.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 99
if hasattr(_libs['GevApi'], '_CreateThread'):
    _CreateThread = _libs['GevApi']._CreateThread
    _CreateThread.argtypes = [CFUNCTYPE(UNCHECKED(c_uint), POINTER(None)), POINTER(None), c_int, POINTER(HANDLE)]
    _CreateThread.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 100
if hasattr(_libs['GevApi'], '_WaitForThread'):
    _WaitForThread = _libs['GevApi']._WaitForThread
    _WaitForThread.argtypes = [POINTER(HANDLE), UINT32]
    _WaitForThread.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 101
if hasattr(_libs['GevApi'], '_GetNumCpus'):
    _GetNumCpus = _libs['GevApi']._GetNumCpus
    _GetNumCpus.argtypes = []
    _GetNumCpus.restype = c_int

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 104
if hasattr(_libs['GevApi'], '_IsTimedOut'):
    _IsTimedOut = _libs['GevApi']._IsTimedOut
    _IsTimedOut.argtypes = [POINTER(struct_timeval)]
    _IsTimedOut.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 105
if hasattr(_libs['GevApi'], '_GetTimeOut'):
    _GetTimeOut = _libs['GevApi']._GetTimeOut
    _GetTimeOut.argtypes = [c_int, POINTER(struct_timeval)]
    _GetTimeOut.restype = None

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 108
if hasattr(_libs['GevApi'], '_Wait'):
    _Wait = _libs['GevApi']._Wait
    _Wait.argtypes = [UINT32]
    _Wait.restype = None

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 109
if hasattr(_libs['GevApi'], '_GetTimestamp'):
    _GetTimestamp = _libs['GevApi']._GetTimestamp
    _GetTimestamp.argtypes = [POINTER(UINT32), POINTER(UINT32)]
    _GetTimestamp.restype = BOOL

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 110
if hasattr(_libs['GevApi'], '_Convert_to_LEFeature_Order'):
    _Convert_to_LEFeature_Order = _libs['GevApi']._Convert_to_LEFeature_Order
    _Convert_to_LEFeature_Order.argtypes = [UINT32]
    _Convert_to_LEFeature_Order.restype = UINT32

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 111
if hasattr(_libs['GevApi'], '_Convert_from_LEFeature_Order'):
    _Convert_from_LEFeature_Order = _libs['GevApi']._Convert_from_LEFeature_Order
    _Convert_from_LEFeature_Order.argtypes = [UINT32]
    _Convert_from_LEFeature_Order.restype = UINT32

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 112
if hasattr(_libs['GevApi'], '_CPU_to_LE32'):
    _CPU_to_LE32 = _libs['GevApi']._CPU_to_LE32
    _CPU_to_LE32.argtypes = [UINT32]
    _CPU_to_LE32.restype = UINT32

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 113
if hasattr(_libs['GevApi'], '_LE32_to_CPU'):
    _LE32_to_CPU = _libs['GevApi']._LE32_to_CPU
    _LE32_to_CPU.argtypes = [UINT32]
    _LE32_to_CPU.restype = UINT32

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 114
if hasattr(_libs['GevApi'], '_CPU_to_BE32'):
    _CPU_to_BE32 = _libs['GevApi']._CPU_to_BE32
    _CPU_to_BE32.argtypes = [UINT32]
    _CPU_to_BE32.restype = UINT32

# /home/wasonj/Downloads/GigE-V-Framework_2.02.0.0132/DALSA/GigeV/include/gevoslib.h: 115
if hasattr(_libs['GevApi'], '_BE32_to_CPU'):
    _BE32_to_CPU = _libs['GevApi']._BE32_to_CPU
    _BE32_to_CPU.argtypes = [UINT32]
    _BE32_to_CPU.restype = UINT32

# No inserted files

