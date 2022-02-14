import rpm
import sys
import rpmfile

# rpmfile module

filename = sys.argv[1]

with rpmfile.open(filename) as rpmf:
    print("name of rpm - ", rpmf.headers.get('name').decode('ascii'))
    print("release - ", rpmf.headers.get('release').decode('ascii'))
    print("version - ", rpmf.headers.get('version').decode('ascii'))
  #  print(rpmf.headers.keys())

# rpm module

filename = sys.argv[1]
rpm_file = open(filename)
ts = rpm.TransactionSet()
package = ts.hdrFromFdno(rpm_file)

for index in package:
    print ("VERSION........", package[rpm.RPMTAG_VERSION].decode('ascii'))
    print ("RELEASE........", package[rpm.RPMTAG_RELEASE].decode('ascii'))
    print ("PACKAGER.......", package[rpm.RPMTAG_PACKAGER].decode('ascii'))

rpm_file.close()

