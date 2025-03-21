from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
    GarminConnectAuthenticationError
)
import os
import time

# Credentials
aus_email = "jeromexshi@gmail.com"
aus_password = "%Jumpswim123"

cn_email = "tim.shi89@gmail.com"
cn_password = "%Jumpswim123"

# Login to Garmin Australia
try:
    garmin_aus = Garmin(aus_email, aus_password)
    garmin_aus.login()
except GarminConnectAuthenticationError:
    print("Failed to login to Garmin Australia")

# Login to Garmin China
try:
    garmin_cn = Garmin(cn_email, cn_password)
    garmin_cn.login()
except GarminConnectAuthenticationError:
    print("Failed to login to Garmin China")