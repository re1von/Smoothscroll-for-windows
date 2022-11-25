import ctypes.wintypes


class MSLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_long),
        ('y', ctypes.c_long),
        ('data', ctypes.c_int32),
        ('reserved', ctypes.c_int32),
        ('flags', ctypes.wintypes.DWORD),
        ('time', ctypes.c_int),
    ]


LowLevelMouseProc = ctypes.CFUNCTYPE(
    ctypes.c_int,
    ctypes.wintypes.WPARAM,
    ctypes.wintypes.LPARAM,
    ctypes.POINTER(MSLLHOOKSTRUCT)
)
