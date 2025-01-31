# this project comes with CV2, a basic display emulation package for SPI displays
# Set this to False to run on your Pi, or True to run on your windows desktop. note, it's small!
RUN_EMULATOR = False

# If True, the shown will be interpolated between the latest and previous values. Simply giving the display more 'movement'
# If True, it will take a couple cycles of the various screens for the interpolated values to catch up with latest
SHOW_INTERPOLATED_VALUE = True

# used to convert from dollars to pounds, set to 1 for displaying USD
USD_EUR = 0.82237184

WITHDRAWL_TARGET = 0.001

# For testing purposes use api-test.nicehash.com. Register here: https://test.nicehash.com
# HOST = 'https://api-test.nicehash.com'
# ORGANISATION_ID = ''
# KEY = ''
# SECRET = ''

# For production
HOST = 'https://api2.nicehash.com'
KEY = ''
SECRET = ''
ORGANISATION_ID = ''
