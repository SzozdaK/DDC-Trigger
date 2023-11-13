# DDC-Trigger
KVM switch solution utilising an industrial USB switch as the KM component and a Raspberry Pi as a DDC console that changes the input source of the connected monitor upon detecting a port change on the USB switch. This tandem switch thus implements KVM switch functionality without interfering with video output in any way. By connecting the RPi via video cable to the monitor we expose the monitor's I2C interface (if it exists) and can use feature 60 of the Monitor Command and Control Specification (MCCS): switch input source.

This script requires ddcutil and python-serial to be installed.

Hardware requirements:

!!! A monitor that has at least three input ports, with one of those ports free for the device to take up. Ideally the device should take up an HDMI port, as HDMI-to-HDMI cables are cheap, but other ports should work fine, too, with the equivalent cable (I avoid adapters, personally, but they should work as they shouldn’t block the DDC lines).
        The monitor must be able to accept the DDC command to switch input source from an input source that is not the currently active source. The creator of ddcutil, says this is not necessarily a universal feature. I think Dell monitors are fine, though.

Any Raspberry Pi model with an HDMI output (micro- or mini-HDMI is fine). A Model B has two output ports, which could be useful for those looking to switch two monitors at once (provided they both meet the previous requirement).

A USB or KVM switch that has a serial port (RS232 or RS485, for example).
        It must be capable of sending its port status back to the console server. We’re not interested in controlling the USB   switch directly—only in listening to its status and triggering the DDC command on the RPi accordingly. The manual should contain information on what command needs to be used to get the switch status.
        The Aten US3344i is the only switch I know of so far that meets this requirement. Since v1.2.112 the ‘info’ command prints the switch’s port status, not just its firmware version (the manual has not been updated to reflect this fact).
