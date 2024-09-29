# eci_to_ecef.py
#
# Usage: python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km
#  
# Parameters:
#  year
#  month
#  day
#  hour
#  minute
#  second
#  eci_x_km: eci cordinates
#  eci_y_km: 
#  eci_z_km: 
#
# Output:
#  ECI to ECEF 
#
# Written by Nicola DeMarinis
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys  # argv
from math import trunc

# initialize script arguments
year = int(0)  
month = int(0) 
day = int(0) 
hour = int(0) 
minute = int(0) 
sec = float('nan')
eci_x_km = float('nan')
eci_y_km = float('nan')
eci_z_km = float('nan')

# parse script arguments
if len(sys.argv)==10:
  year = int(sys.argv[1])
  month = int(sys.argv[2])
  day = int(sys.argv[3])
  hour = int(sys.argv[4])
  minute = int(sys.argv[5])
  sec = float(sys.argv[6])
  eci_x_km = float(sys.argv[7])
  eci_y_km = float(sys.argv[8])
  eci_z_km = float(sys.argv[9])
else:
  print(\
   'Usage: '\
   'python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km'\
  )
  exit()

# "constants"
R_E_KM = 6378.1363
E_E    = 0.081819221456
w = 7.292115 * (10**-5) 

# write script below this line

# First get julian frac time
 
jd = day - 32075 \
   + trunc(1461 * (year + 4800 +  trunc((month-14)/12))/4) \
   + trunc(367 * (month - 2 - (trunc((month-14)/12) *12 ))/12) \
   - trunc(3 * trunc((year + 4900 + trunc((month-14)/12))/100)/4)

jdmn = (jd) - 0.5
dfrac = (sec + 60*(minute + 60*hour))/86400
jd_frac = jdmn + dfrac

#get time and gmst angle
t_ut1 = (jd_frac - 2451545.0)/36525
theta_gmst = 67310.54841 + ((876600*60*60) + 8640184.812866)*t_ut1 + (0.093104 * (t_ut1**2)) + (-6.2*(10**-6)*(t_ut1**3) )

#Convert to radians
theta_rad = (theta_gmst%86400)*w

# Now convert Ref frames
ecef_x_km = eci_x_km*math.cos(-theta_rad) - eci_y_km*math.sin(-theta_rad)
ecef_y_km = eci_y_km*math.cos(-theta_rad) + eci_x_km*math.sin(-theta_rad)
ecef_z_km = eci_z_km

#Testing
#print(jd_frac)
#print(theta_rad)

#Print
print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)

