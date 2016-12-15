** Light Pollution Camera

*What it does?*
1. Take a photo using picam.
2. Extract light information by converting the image to grayscale and setting treshold on alpha value.
3. Average light value in each pixel and and calculate a quotient between 0 and 255 as a measure of light pollution
4. Finally, merge 6 images onto one to compare calibration (i.e. which alpha cutoff looks best)

*Specs for hardware*
Great documentation of RasPi camera V1.3
http://www.truetex.com/raspberrypi

*Libraries Used*
- Pillow (from PIL import ...): Rudimentary image processing
- Picamera (from picamera import …): Powerful abstractions for raspberry pi cameras

Libraries considered:
- OpenCV - excessive footprint for the application
- Scikit-image - no support for RasPi, currently broken for my distribution of macOS
