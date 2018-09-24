Lookalike Demo
==============

Orange3 Lookalike Demo extends [Orange3](http://orange.biolab.si), a data mining software
package, with widgets for demonstration purposes. The add-on is designed for introducing primary and secondary school children to data mining and machine learning concepts in a fun way.

More about the project in our [Celebrity Lookalike](https://blog.biolab.si/2016/11/25/celebrity-lookalike-or-how-to-make-students-love-machine-learning/) blogpost.

Installing
----------
This add-on requires Orange3 and Python 3.4 or newer. To install
it, run:

    # Clone the repository and move into it
    git clone https://github.com/biolab/looklike-demo.git
    cd lookalike-demo

    # Setup the add-on
    pip install .

To install Orange in editable/development mode, run

    pip install -e .


### OpenCV dependency

To access Face Detector and Webcam widgets, you need OpenCV library.

#### Windows

Download the required [OpenCV] package. Make sure you download the package for your version of Python and OS.

[OpenCV]: http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv

Then go to the folder containing the downloaded file and open the terminal. Run (insert the right file name after install):

    pip install <opencv_python‑3.2.0‑cp36‑cp36m‑win_amd64.whl>

#### MacOS

In the terminal, run:

    /Applications/Orange3.app/Contents/MacOS/pip install opencv-python
    
