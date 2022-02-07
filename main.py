import json
import colorsys as cs
import os
from zipfile import ZipFile
import glob


def to_hex(i):
    hx = hex(int(i))[2:]
    if len(hx) == 1:
        hx = "0" + hx
    return hx

# Converts rgb colors to
def to_color(r, g, b):
    cs = [to_hex(c) for c in [r, g, b]]
    return "#{cs[0]}{cs[1]}{cs[2]}".format(cs=cs)


# Return files from directory and adds to a list
def get_files():
    txtfiles = []
    for file in glob.glob("*.swatches"):
        txtfiles.append(file)
    return txtfiles


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fns = get_files()

    for fn in fns:
        # Checks to see if file has changed names already
        base = os.path.splitext(fn)[0]

        try:
            # Converts file extension to ZIP file
            # TODO: Take swatches file and convert to zip file
            filename = base + '.zip'
            os.rename(fn, filename)
        except FileNotFoundError:
            print('Zip file already found.')

        # TODO: Take ZIP file and extract JSON file
        # Unarchives file(s)
        with ZipFile(filename, 'r') as zipObj:
            zipObj.extractall()

        # Open swatches file (the extracted file)
        f = open('Swatches.json')
        data = json.load(f)
        hex_color_str = ""
        for i in data['swatches']:
            hsb = cs.hls_to_rgb(i['hue'], i['brightness'], i['saturation'])
            hex_color = to_color(hsb[0] * 255.0, hsb[1] * 255.0, hsb[2] * 255.0)
            hex_color_str += hex_color.strip() + ","
        f.close()

        # Write hex to files
        f = open("hex_color_values.txt", "a")
        f.write(base + "\n")
        f.write(hex_color_str + "\n")

        # Remove json file
        os.rename(filename, "Completed/" + filename)
        os.remove('Swatches.json')
        print('File has been removed.')
