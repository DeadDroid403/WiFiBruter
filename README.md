
# WiFi-Bruter

This Is a WiFi Brute Force Script Written in Python.
We Are Using Internal WiFi Adapter For Runtime Brute Force.


## Documentation

Introduction:

This documentation outlines the usage and implementation details of a Python WiFiBruter project. The WiFiBruter Uses your Internal WiFi Adapter to Brute Force WiFi in Runtime. You Can Run This On a Single WiFi and Also on All WiFi Networks Around Your Area.

Features:

1. Multiple WiFi support: you can use this script on a single wifi or on every wifi in your area.

2.  User-friendly interface: This Script Provides a User friendly interactive Functionality.

3. Verbosity: We Can Choose if we want a Verbose Output Or Not.

4. Changable Password Length: We Can Choose How Big Password List We want to use.


Requirements:

   1. Python 3.x.
   2. Must Be run as Root or With Sudo.
   3. Only Works In Linux. Not In Windows.


### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/DeadDroid401/WiFiBruter.git
    ```

2. Navigate to the project directory:
    ```bash
    cd WiFiBruter
    ```


### Usage

1. Run the `pass.py` script using Python3:
    ```bash
    sudo python3 wifibruter.py
    ```

2. Follow the on-screen instructions to interact with script.


### Limitations

1. **No Threading Used**: This python script is a bit slow in cracking wifi passwords because we can't access a single NIC For Multiple Threads Of Connecting To a Network.

2. **Sudo Access**: To Connect to a WiFi Network We Must Become Root Cause we are accessing Our Hardware of the Device and as a Normal user We need To authenticate Again N Again.

3. **Linux Required**: Since This Script is using Linux Commands internaly to Connect to WiFi which we can't run on windows or any other os.
so we can not run this script on Windows.
