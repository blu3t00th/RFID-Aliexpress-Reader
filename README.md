# RFID-Aliexpress-Reader

A small fix for aliexpress Reader that does not outputs whole decimal  and added a converter that automaticly converts from decimal to HEXDecimal in order to clone for proxmark


IN ORDER TO WORK YOU NEED TO FIND COM PORT:
 
Linux system:

Connect your USB RFID Reader to your computer.

Open a terminal.

Run the following command to list all connected USB devices:
lsusb

Find your USB RFID Reader in the list. The output might look something like this:

Bus 001 Device 005: ID 1234:abcd A Company Inc. RFID Reader
Remember the ID '1234:abcd' – you'll need it in the next step.

Now, run the following command to list all TTY devices and filter for your RFID Reader's ID:

ls /dev/tty* | grep -i '1234:abcd'

Replace '1234:abcd' with the ID from the previous step. The command should return a device path like '/dev/ttyUSB0' or '/dev/ttyACM0'.

Replace 'COM#' in the Python script with the device path:

ser = serial.Serial('/dev/ttyUSB#', 9600)


Windows System:

Connect your USB RFID Reader to your computer.

Open the Device Manager by pressing Win + X and selecting 'Device Manager' from the list.

In the Device Manager, expand the 'Ports (COM & LPT)' category.

Look for your USB RFID Reader in the list. The COM port number should be displayed next to its name, for example, 'USB Serial Port (COM3)'.

Replace 'COM#' in the Python script with the correct COM port number (e.g., 'COM3').

![image](https://github.com/blu3t00th/RFID-Aliexpress-Reader/assets/39458873/fba8c308-cfce-417c-8dc0-4a0d63621492)
