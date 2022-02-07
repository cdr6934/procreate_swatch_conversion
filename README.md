# Procreate Swatch Conversion
> Just to note, this is a work in progress at the moment and has everything needed for basic usage 

The following package is a simple Python script used to take Procreate swatches, 
unpack them and convert them to a format that is digestable for web use. 


## Usage 
Just drop your swatches into the same folder as the main.py and run
```python
python main.py
```
### Returns
A file **hex_color_value.txt** will store the entire HEX color like so: 
```text
Watts_ansky
#d74b36,#54413d,#602c1c,#e9d6d0,#ded5d1,#f6dfd3,#e8a683,#9f8166,#ececeb,#bba890,#ebd5a6,#f4f0e3,#f1efe8,#f8f2df,#d0d3b4,#d9dfe1,#c9d5dc,#b4ccdd,#8cb8db,#5a83a5,#579edc,#3090f1,#8595a6,#a8ccf7,#305e9d,#143575,#0842dd,#a8a8af,#171220,#6f555b,
```

## Breakdown of Swatches file
Once you have exported the .swatches file from an IOS device the following package is just a .ZIP file 

This file can be renamed to .zip to be recognized by any system. Once the file is unzipped a JSON 
file called (Swatches.json) will be extracted and will look like this the following:

```json
{
  "name" : "Pretty Blues",
  "swatches" : [
    {
      "alpha" : 1,
      "origin" : 2,
      "colorSpace" : 1,
      "colorModel" : 0,
      "brightness" : 0.20000000000000001,
      "components" : [
        0.20000000000000001,
        0.13725490196078433,
        0.13725490196078433
      ],
      "version" : "5.0",
      "colorProfile" : "5Gjokjn8BJPV6PubAU6RshDGyqc8ge3wTD0hpzTzd8w=",
      "saturation" : 0.31372549019607843,
      "hue" : 0.13725490196078433
    }, 
    ... }
```
Currently, the important elements in the object are **hue**, **saturation**, and **brightness**. The rest of the 
elements in the object are used internally by Procreate. I have yet to really investigate their significance or 
try to use them in any other context. 

Once extracted, these can be mapped from HSB colors to RGB which then are easy to convert to HEX color values. 