Software
========

Android
--------

1 Compiler Environment
^^^^^^^^^^^^^^^^^^^^^^^

1.1 Vmware10.0+ubuntu18.04
""""""""""""""""""""""""""

Install Vmware10.0 in windows OS, and then install ubuntu18.04 in VMware to compile. Please visit the
official website http://www.ubuntu.com/ to download and install ubuntu operating system.

.. note::

   buildroot should be complied by ubuntu 64bit OS.


1.2 Install OpenJDK1.8
""""""""""""""""""""""""""
.. code-block:: 

 sudo mkdir /usr/lib/java
 sudo tar zxvf java-8-openjdk-amd64.tar.gz –C /usr/lib/java/

Add the following information in the end of "/etc/profile"::

 export JAVA_HOME=/usr/lib/java/java-8-openjdk-amd64
 export JRE_HOME=/usr/lib/java/java-8-openjdk-amd64/jre
 export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/jre/lib:$CLASSPATH
 export PATH=$JAVA_HOME/bin:$JRE_HOME/jre/bin:$PATH

Execute command

.. code-block:: 

 source /etc/profile

Check if the jdk has been installed successfully and check the revised version:

.. code-block:: 

 java -version
 
1.2 Install Tools
""""""""""""""""""

* PC OS: ubuntu system
* Network: online  
* Permission: root

.. code-block:: 

 sudo apt-get install build-essential zlib1g-dev flex libx11-dev gperf libncurses5-dev bison lsb-core lib32z1-dev g++-multilib lib32ncurses5-dev uboot-mkimage g++-4.4-multilib repo git ssh make gcc libssl-dev liblz4-tool expect g++ patchelf chrpath gawk texinfo chrpath diffstat binfmt-support qemu-user-static live-build bison flex fakeroot cmake gcc-multilib g++-multilibdevice-tree-compiler python-pip ncurses-dev pyelftools unzip

2 Compile Source
^^^^^^^^^^^^^^^^^^^^^^^

Step 1, unzip the source and set the compile board

.. code-block:: 

 tar xvf android11.tar.gz
 cd android11
 ./build.sh -h   #view the build command

Step 2, compile uboo

.. code-block:: 

 cd u-boot
 ./make.sh rk3566

Step 3, compile the kernel
 
.. code-block:: 

 cd kernel
 make ARCH=arm64 rockchip_defconfig rk356x_evb.config android-11.config

for HDMI

.. code-block:: 

 make ARCH=arm64 em3566-boardcon-hdmi.img 

or LVDS
 
.. code-block:: 

 make ARCH=arm64 em3566-boardcon-lvds.img 
 
.. note::
 It will pop out **configuration the IO power Domain Map** window when first time compile kernel, you need to configure according to the table below.

.. figure:: ./image/IO-power-Domain-Map.png
   :align: center
   :alt: IO-power-Domain-Map
 
**boot.img** are generated in :file:`android11\kernel` directory.
 
.. Note:: 

 If only update kernel, compile kernel as follow
 
.. code-block:: 

 make ARCH=arm64 BOOT_IMG=../rockdev/Image-rk3566_r/boot.img em3566-boardcon-hdmi.img 
 # or
 make ARCH=arm64 BOOT_IMG=../rockdev/Image-rk3566_r/boot.img em3566-boardcon-lvds.img
 
Step 4, compile Android

.. code-block:: 

 source build/envsetup.sh
 lunch rk3566_r-userdebug
 make -j8

Step 5, Generated image file

.. code-block:: 

 ./mkimage.sh
 ./build.sh -u
 cd rockdev
 ls
 
Images and update.img are generated in current directory. 
After compilation, execute the follow command to clean the build.

.. code-block:: 

 ./build.sh cleanall

3 Images Operation
^^^^^^^^^^^^^^^^^^^

3.1 Pack Image
""""""""""""""

Step 1, copy all the files in Android directory :file:`rockdev/Image` to the windows :file:`AndroidTool/rockdev/Image`

Step 2, enter :file:`AndroidTool/rockdev/`, double-click to run **mkupdate_rk356x.bat**.

Step 3, the **update.img** will be generated in rockdev directory.
  
.. figure:: ./image/EM3566_SBC_Android11_figure_5.png
   :align: left
   :alt: Android directory path
   
.. figure:: ./image/EM3566_SBC_Android11_figure_16.png
   :align: left
   :alt: copy files
   
.. figure:: ./image/EM3566_SBC_Android11_figure_7.png
   :align: left
   :alt: run mkupdate_rk356x.bat
   
.. figure:: ./image/EM3566_SBC_Android11_figure_8.png
   :align: center
   :alt: run mkupdate_rk356x.bat print out-1
   
.. figure:: ./image/EM3566_SBC_Android11_figure_9.png
   :align: center
   :alt: run mkupdate_rk356x.bat print out-2
  
.. figure:: ./image/EM3566_SBC_Android11_figure_10.png
   :alt: path
 
.. figure:: ./image/EM3566_SBC_Android11_figure_11.png
   :alt: generated update.img

3.2 Unzip Firmware
"""""""""""""""""""""""

Unzip Firmware in windows.

Step1, open **RKDevTool.exe** :file:`RKDevTool_Release/RKDevTool.exe`

.. figure:: ./image/EM3566_SBC_Android11_figure_12.png
   :alt: open RKDevTool.exe
   
Step 2, click *Advanced Function -> Firmware*, select **update.img**. Click *Unpack* to Unzip.

.. figure:: ./image/EM3566_SBC_Android11_figure_13.png
   :alt: Unpack

Step 3, Unpack finish as follow

.. figure:: ./image/EM3566_SBC_Android11_figure_14.png
   :alt: Unpack finish

The unzip files will be generated in :file:`/RKDevTool/RKDevTool_Release/Output/Android/Image`

.. figure:: ./image/EM3566_SBC_Android11_figure_15.png
   :alt: path

.. figure:: ./image/EM3566_SBC_Android11_figure_16.png
   :alt: unzip files

4 Install Tools
^^^^^^^^^^^^^^^^^^^^^^^

4.1 Install CP2102 Driver  
"""""""""""""""""""""""""""""

Plug the USB-to-UART cable CP2102 to the PC, unzip **CP2102WIN7.rar** on Windows, then click *preInstaller.exe* to install

.. figure:: ./image/EM3566_SBC_Android11_figure_17.png
   :alt: Install CP2102
   :width: 472px

.. figure:: ./image/EM3566_SBC_Android11_figure_18.png
   :alt: Install successful

.. figure:: ./image/EM3566_SBC_Android11_figure_19.png
   :alt: unzip files
      
Now the device will be listed under *Device Manager -> PORTS* with unique serial port assigned

.. figure:: ./image/EM3566_SBC_Android11_figure_19.png
   :alt: serial port path

4.2 Install Rockchip Driver Assistant
""""""""""""""""""""""""""""""""""""""""

Path :file:`DriverAssitant_v5.1.1/DriverInstall.exe`

.. figure:: ./image/RK_Driver_Assitant_install-1.png
   :alt: RK_Driver_Assitant_install-1
   :width: 300px
   
.. figure:: ./image/RK_Driver_Assitant_install-2.png
   :alt: RK_Driver_Assitant_install-2
   :width: 300px

After the installation is complete, connect the board and PC with Micro USB cable and press the **Recover** key and hold then power the board, in *Computer Management* can see the following information:

.. figure:: ./image/EM3566_SBC_Android11_figure_22.png
   :alt: serial port path

The WINDOW will pop up found New Hardware Wizard dialog box, choose to install from the specified location, and then select :file:`/DriverAssitant_v5.11/DriverAssitant_v5.1.1/ADBDriver`.
After the installation is complete in *Computer Management* can see the following information:

.. figure:: ./image/EM3566_SBC_Android11_figure_23.png
   :alt: installation complete

4.3 Install Serial Terminal Tool
"""""""""""""""""""""""""""""""""

The serial terminal **SecureCRT** is used for debugging. It can be used directly after decompression. 
Open **SecureCRT.exe** after copy to PC path :file:`tools/windows/SecureCRT.exe`, then click the icon *Quick Connect* to config

.. figure:: ./image/EM3566_SBC_Android11_figure_24.png
   :alt: SecureCRT UI

.. figure:: ./image/EM3566_SBC_Android11_figure_25.png
   :alt: Quick Connect

Set the parameters as follow:

- Protocol: Serial
- Port: To be specified by user PC
- Baud rate: 1500000
- Please check **XON/XOFF** but not **RTS/CTS**
- Check *Save* session

After all, click *connect*

.. figure:: ./image/EM3566_SBC_Android11_figure_26.png
   :alt: Connect Serial
 
.. note:: 

 If open more than one serial terminal tools, and they use the same serial port, there will be reported the port is busy.
 **Solution**: Turn off the serial tool that unnecessary.



5 Burn Images
^^^^^^^^^^^^^^^^^^^^^^^

6 Android Application
^^^^^^^^^^^^^^^^^^^^^^^

6.1 HDMI Display
""""""""""""""""""

6.2 SD Card
""""""""""""""""""

6.3 USB Host
""""""""""""""""""

6.4 Vedio Player
""""""""""""""""""

6.5 Ethernet
""""""""""""""""""

6.6 Record
""""""""""""""""""

6.7 RTC
""""""""""""""""""

6.8 WiFi
""""""""""""""""""

6.9 Bluetooth
""""""""""""""""""

6.10 Camera
""""""""""""""""""

6.11 RS485
""""""""""""""""""

6.12 RS232
""""""""""""""""""

6.13 M.2 SATA
""""""""""""""""""

6.14 IR
""""""""""""""""""




Debian
--------

Buildroot
--------

