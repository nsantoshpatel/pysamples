##  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | No 
##  6 : Cancel | Try Again | Continue

import ctypes  # An included library with Python install.
ctypes.windll.user32.MessageBoxW(0, "Body \nNew alert\tPlease click OK", "Self Alert", 1)