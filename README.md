# rpi_gige_v_framework
ROS package providing a basic Python API to access DALSA GigE cameras using OpenCV and numpy. Tested with DALSA Genie Nano C2450. See "Issues" section for know issues.

The [https://www.teledynedalsa.com/imaging/products/software/linux-gige-v/ | DALSA GigE-V Framework for Linux] must be installed. Be sure to run 'corinstall' and then logout/login to fully install the framework.

Interfaces to the GevApi library were generated using [https://github.com/davidjamesca/ctypesgen | ctypesgen.py].
