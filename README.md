# Tesseract OCR

[![Build Status](https://travis-ci.org/tesseract-ocr/tesseract.svg?branch=master)](https://travis-ci.org/tesseract-ocr/tesseract)
[![Build status](https://ci.appveyor.com/api/projects/status/miah0ikfsf0j3819/branch/master?svg=true)](https://ci.appveyor.com/project/zdenop/tesseract/)
![Build status](https://github.com/tesseract-ocr/tesseract/workflows/sw/badge.svg)<br>
[![Coverity Scan Build Status](https://scan.coverity.com/projects/tesseract-ocr/badge.svg)](https://scan.coverity.com/projects/tesseract-ocr)
[![Code Quality: Cpp](https://img.shields.io/lgtm/grade/cpp/g/tesseract-ocr/tesseract.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tesseract-ocr/tesseract/context:cpp)
[![Total Alerts](https://img.shields.io/lgtm/alerts/g/tesseract-ocr/tesseract.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tesseract-ocr/tesseract/alerts)
[![OSS-Fuzz](https://img.shields.io/badge/oss--fuzz-fuzzing-brightgreen)](https://bugs.chromium.org/p/oss-fuzz/issues/list?sort=-opened&can=2&q=proj:tesseract-ocr)
<br/>
[![GitHub license](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://raw.githubusercontent.com/tesseract-ocr/tesseract/master/LICENSE)
[![Downloads](https://img.shields.io/badge/download-all%20releases-brightgreen.svg)](https://github.com/tesseract-ocr/tesseract/releases/)

## About

This package uses the **OCR engine** - `libtesseract` and a **command line program** - `tesseract`
with **UB-Manheim** English train-data to mark attendance of Google Meet participants in Google Sheets

The lead developer is Anhat Singh

This package uses various python libraries to take attendance effeciently and make google sheets using **Google Sheets API v4**

## Building / Installing Python-Auto-Attendance

### Building the Package
1. Install the Python dependencies by running the following pip commands
    ```
    pip install pysimplegui
    pip install selenium
    pip install pyautogui
    pip install pygetwindow
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    pip install pyscreenshot
    pip install pytesseract
    pip install opencv-python
    ```
2. Install `UB-Mannheim Windows pre-built binary` of [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) from [here](https://tesseract-ocr.github.io/tessdoc/Home.html#binaries). (Note: Make sure you are installing at default directory only, and not changing it)
3. Use the included `chromedriver.exe` or download the latest one from [ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/) and keep it in the root directory.
4. Follow bullet 3 and 4 of Prerequisites at [Google Sheets API v4 Guide](https://developers.google.com/sheets/api/quickstart/python) to create a Google Cloud Platform Project, enable Sheets API and get the Google `credentials.json` file to be put into the root directory.

### Get pre-built binary package
1. Copy everything in `dist/` folder onto your pc.
2. Use the included `chromedriver.exe` or download the latest one from [ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/) and keep it in the root directory.
3. Follow bullet 3 and 4 of Prerequisites at [Google Sheets API v4 Guide](https://developers.google.com/sheets/api/quickstart/python) to create a Google Cloud Platform Project, enable Sheets API and get the Google `credentials.json` file to be put into the root directory.

## Running Python-Auto-Attendance

* If you have pre-built package, simply run `app.exe` file.
* If you have downloaded the source-code, run the following command:
    ```
    py app.py
    ```
### How to Use
    Coming soon

## License

    The code in this repository is licensed under the GNU General Public Licence, Version 3.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       https://www.gnu.org/licenses/gpl-3.0.en.html

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

**NOTE**: This software depends on other packages that may be licensed under different open source licenses.

Tesseract uses [Leptonica library](http://leptonica.com/) which essentially
uses a [BSD 2-clause license](http://leptonica.com/about-the-license.html).