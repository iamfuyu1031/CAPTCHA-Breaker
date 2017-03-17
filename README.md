# CAPTCHA-Breaker

## Intorduction
CAPTCHA is short for 'Completely Automated Public Turing test to tell Computers and Humans Apart', which is widely used to determine whether or not the user is human. 

The is the code to break man-shape letter CAPTCHA. The idea is taken from http://www.boyter.org/decoding-captchas/.

The folder `example-captcha` shows the examples of the CAPTCHA iamges that we are trying to break. The folder `iconset` provides the training set of the CAPTCHA characters. The file `captcha-breaker.py` is the Python code to break the CAPTCHA. The file `out.png` is the CAPTCHA image that we want to break.

In theory, it should work with all types of CAPTCHA. If you want to apply it to other CAPTCHA, you may start by inferring the training set of icons from several sample CAPTCHAs. Refer to http://www.boyter.org/decoding-captchas/ for details. Parameters in the code might need to change accordingly.

## How to use
Run the code with `python captcha-breaker.py` and you will see the crakced CAPTCHA characters are printed to the screen. If you want to crack other file other than the example `out.png`, you can copy them to the local directory and change the file name in line 44 of `captcha-breaker.py`.

