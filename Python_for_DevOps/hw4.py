import rpm
import sys

filename = sys.argv[1]
rpm_file = open(filename)
ts = rpm.TransactionSet()
package = ts.hdrFromFdno(rpm_file)

for index in package:
    print "VERSION........", package[rpm.RPMTAG_VERSION]
    print "RELEASE........", package[rpm.RPMTAG_RELEASE]
    print "PACKAGER.......", package[rpm.RPMTAG_PACKAGER]

print (str(package[rpm.RPMTAG_VERSION])[:1]+".rel"+str(package[rpm.RPMTAG_RELEASE][:1])+"."+str(package[rpm.RPMTAG_PACKAGER])[:6])

rpm_file.close()

