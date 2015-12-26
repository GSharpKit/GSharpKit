# Mac OS X Build

This is RPM and autoconfig for Mac OS X

- Install

clone to homedir under "Projects"

sh build.sh

- RPM

cp rpmmacros ~/.rpmmacros 

# El Capitan SIP (System Integrity Protection)

- Reboot and hold down Cmd+r
- Select Utility -> Terminal
- Type "csrutil disable"
- Reboot into normal
- sudo vi /System/Library/Sandbox/rootless.conf
```
*				/usr/darwinx
```
- sudo mkdir /usr/darwinx
- sudo chflags norestricted /usr/darwinx/
- Reboot and hold down Cmd+r
- Select Utility -> Terminal
- Type "csrutil enable"
- Reboot into normal

