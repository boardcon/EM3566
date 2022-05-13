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

+--------------+----------------+
| PC OS        | ubuntu system  |
| Network      | online         |
| Permission   | root           |
+--------------+----------------+

.. code-block:: 

 sudo apt-get install build-essential zlib1g-dev flex libx11-dev gperf libncurses5-dev bison lsb-core lib32z1-dev g++-multilib lib32ncurses5-dev uboot-mkimage g++-4.4-multilib repo git ssh make gcc libssl-dev liblz4-tool expect g++ patchelf chrpath gawk texinfo chrpath diffstat binfmt-support qemu-user-static live-build bison flex fakeroot cmake gcc-multilib g++-multilibdevice-tree-compiler python-pip ncurses-dev pyelftools unzip

2 Compile Source
-----------------

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

 
3 
-----------------

3.1
""""""""""""""""""

3.2
""""""""""""""""""

4 
-----------------

4.1  
""""""""""""""""""

4.2
""""""""""""""""""

4.3
""""""""""""""""""

5 
-----------------

6 
-----------------

6.1
""""""""""""""""""

6.2
""""""""""""""""""

6.3
""""""""""""""""""

6.4
""""""""""""""""""

6.5
""""""""""""""""""

6.6
""""""""""""""""""

6.7
""""""""""""""""""

6.8
""""""""""""""""""

6.9
""""""""""""""""""

6.10
""""""""""""""""""

6.11
""""""""""""""""""

6.12
""""""""""""""""""

6.13
""""""""""""""""""

6.14
""""""""""""""""""




Debian
--------

Buildroot
--------

