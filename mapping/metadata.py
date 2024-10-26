import os
from exif import Image


def dms_to_dd(d, m, s):
    coord = float(d) + float(m)/60 + float(s)/3600
    return coord


files_path = 'photos'
filecount = 0

longitude = []
latitude = []

for file in os.listdir(files_path):
    if not file.startswith("."):
        with open(os.path.join(files_path, file), 'rb') as image_file:
            photo = Image(image_file)

        dms = photo.gps_longitude
        dd = dms_to_dd(dms[0], dms[1], dms[2])
        longitude.append(dd)

        dms = photo.gps_latitude
        dd = dms_to_dd(dms[0], dms[1], dms[2])
        latitude.append(dd)

        filecount += 1

for n in range(filecount-1):
    print(f"[{longitude[n]}, {latitude[n]}],")
print(f"[{longitude[-1]}, {latitude[-1]}]")
