Hardware
========

1 Introduction
-------------

1.1 Summary
^^^^^^^^^^^^

The EM3566 is a single-board computer powered by a Rockchip RK3566 processor featuring four
ARM Cortex-A55 CPU cores and Mali-G52-2EE graphics and designed for AIoT applications such
as AI robot, smart POS machine, face recognition terminal, and business display integrated
equipment.

1.2 RK3566 Specifications
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: 
 :header: "Item", "Specifications"
 :widths: 15, 30

 "SoC", "RockChip RK3566"
 "CPU", "Quad-core 64-bit Cortex-A55, 22nm lithography process, frequency up to 1.8GHz"
 "GPU", "ARM G52 2EE. Supports OpenGL ES 1.1/2.0/3.2. OpenCL 2.0. Vulkan 1.1. Embedded high-performance 2D acceleration hardware"
 "NPU", "0.8Tops"

1.3 EM3566 Features
^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ./image/EM3566-Interfaces.jpg
   :align: center
   :alt: EM3566_interface
   :width: 400px
   
.. list-table:: 
    :widths: 15 30
    :header-rows: 1

    * - Item
      - Description
    * - CPU
      - RockChip RK3566 quad-core Cortex-A55 @ up to 1.8GHz
    * - Memory
      - 2GB, 4GB, or 8GB LPDDR4 RAM
        32Bit, supports all-data-link ECC
    * - Storage
      - 8GB / 32GB / 64GB / 128GB eMMC. 
        M.2 PCIe 2.0 socket NVMe SSD (Expand with 2242 NVMe SSD).
        MicroSD card slot (Expand with TF card). 
        SATA3.0 (can switch between SATA and USB 3.0.
    * - Power Supply
      - 12V/3A DC input jack
    * - USB
      - 1x USB OTG 2.0
        4x USB Host 2.0 (USB-AF or 4-pin connector).
        1x USB 3.0.
    * - Connectivity
      - Gigabit Ethernet RJ45 ports via Realtek RTL8211F-CG controller. 2.4G WiFi(802.11b/g/n) with Bluetooth 4.0. mPCIe socket with Nano SIM card port to support 4G&GPS module.
    * - Serial
      - 1x Serial port for debug, 3-pin connector. 2x UART, 4-pin connectors. 1x RS485, 2-pin header or 3-pin connector.
    * - Video
      - HDMI 2.0, 4Kp60. MIPI DSI/LVDS, 1080p60. eDP 1.3, 2560x1600 @60Hz. MEMS_Module for Video output.
    * - Audio
      - 3.5mm audio I/O jack. ES8388 audio codec. 8-channel audio via HDMI.
    * - Camera(optional)
      - 2x Cameras via MIPI CSI (24pin FPC connector)
    * - Keys & Switch
      - 1x Recover Key. 1x Switch for switch between SATA and USB 3.0
    * - Other features
      - Other features	RTC with battery connector; IR receiver; GPIO; ADC
    * - Dimension
      - 135mm x 95mm

1.4 Block Diagram
^^^^^^^^^^^^^^^^^^^^^^
.. figure:: ./image/EM3566_SBC_Block_diagram.gif
   :align: center
   :alt: EM3566_SBC_Block_diagram
   :width: 400px

1.5 CPU module Introduction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The CPU module CM3566 features 2GB LPDDR4 RAM and 8GB eMMC Flash. 

**CM3566 specification** 

- Pin number – 186 pins, 0.9mm pitch
- Dimension – 40mm x 47mm
- Layer – 8 Layers, complying with EMS/EMI:
- Power supply – DC 3.3V 
- Application – smart Device, advertising devices, TV box, POS systems, vehicle control terminals, AI robot, business display integrated equipment, etc.

.. figure:: ./image/CM3566_PCB_Dimension.png
   :align: center
   :alt: CM3566_PCB_Dimension
   :width: 350px
   
**Pin Definition**

.. list-table:: 
    :widths: 15 10 30 10 15
    :header-rows: 1

    * - Pin
      - Signal
      - Description or functions
      - GPIO serial
      - IO Voltage
    * - 1
      - VCC3V3_SYS
      - 3.3V Main Power input
      - 
      - 3.3V
    * - 2
      - VCC3V3_SYS
      - 3.3V Main Power input
      - 
      - 3.3V
    * - 3
      - VCC3V3_SYS
      - 3.3V Main Power input
      - 
      - 3.3V
    * - 4
      - VCC_RTC
      - RTC button Cell Power input
      - 
      - 3.0V-1.8V
    * - 5
      - PMIC_32KOUT
      - RTC clock(32.768khz) output
      - 
      - 3.3V
    * - 6
      - GND
      - Ground
      - 
      - 0V
    * -  7                                                                                                                       
      - HDMITX_CEC_M0
      -
      - GPIO4_D1_u
      -  3.3V
    * - 8
      - HDMITX_SDA
      - Pull up 2.2K inside
      - GPIO4_D0_u
      - 3.3V
    * - 9
      - HDMITX_SCL
      - Pull up 2.2K inside
      - GPIO4_C7_u
      - 3.3V
    * - 10
      - GND
      - Ground
      -
      - 0V
    * - 11
      - GMAC1_MCLKINOUT_M0
      - RGMII reference clock input(125Mhz)
      - GPIO3_C0_d
      - 3.3V
    * - 12
      - GND
      - Ground
      -            
      - 0V
    * - 13
      - GMAC1_TXD0_M0
      -                                  
      - GPIO3_B5_d
      - 3.3V
    * - 14
      - GMAC1_TXD1_M0
      -
      - GPIO3_B6_d
      - 3.3V 
    * - 15
      - GMAC1_TXEN_M0
      -
      - GPIO3_B7_d
      - 3.3V
    * - 16
      -  GMAC1_RXDV_CRS_M0
      - 
      - GPIO3_B3_d
      - 3.3V
    * - 17
      - GMAC1_RXD1_M0
      - 
      - GPIO3_B2_d
      - 3.3V
    * - 18
      - GMAC1_RXD0_M0
      - 
      - GPIO3_B1_d
      - 3.3V
    * - 19
      - GMAC1_RXD3_M0
      -                                   
      - GPIO3_A5_d
      - 3.3V
    * - 20
      - GMAC1_RXD2_M0
      - 
      - GPIO3_A4_d
      - 3.3V
    * - 21
      - GMAC1_RXCLK_M0
      - 
      - GPIO3_A7_d
      - 3.3V
    * - 22
      - GMAC1_TXD2_M0
      - 
      - GPIO3_A2_d
      - 3.3V
    * - 23
      - GMAC1_TXD3_M0
      - 
      - GPIO3_A3_d
      - 3.3V       
    * - 24
      - GMAC1_TXCLK_M0
      - 
      - GPIO3_A6_d
      - 3.3V
    * - 25
      - MIPI_DSI_TX0_D3N/LVDS_TX0_D3N
      - MIPI DSI or LVDS TXD3N
      - 
      - 1.8V
    * - 26
      - MIPI_DSI_TX0_D3P/LVDS_TX0_D3P
      - MIPI DSI or LVDS TXD3P
      - 
      - 1.8V
    * - 27
      - MIPI_DSI_TX0_D2N/LVDS_TX0_D2N
      - MIPI DSI or LVDS TXD2N
      - 
      - 1.8V
    * - 28
      - MIPI_DSI_TX0_D2P/LVDS_TX0_D2P
      - MIPI DSI or LVDS TXD2P
      - 
      - 1.8V
    * - 29
      - MIPI_DSI_TX0_D1N/LVDS_TX0_D1N
      - MIPI DSI or LVDS TXD1N
      - 
      - 1.8V
    * - 30
      - MIPI_DSI_TX0_D1P/LVDS_TX0_D1P
      - MIPI DSI or LVDS TXD1P
      - 
      - 1.8V
    * - 31
      - MIPI_DSI_TX0_D0N/LVDS_TX0_D0N
      - MIPI DSI or LVDS TXD1N
      - 
      - 1.8V
    * -  32
      - MIPI_DSI_TX0_D0P/LVDS_TX0_D0P
      - MIPI DSI or LVDS TXD1P
      - 
      - 1.8V
    * - 33
      - MIPI_DSI_TX0_CLKN/LVDS_TX0_CLKN
      - MIPI DSI or LVDS TXD1N
      - 
      - 1.8V
    * - 34
      - MIPI_DSI_TX0_CLKP/LVDS_TX0_CLKP
      - MIPI DSI or LVDS TXD1P
      - 
      - 1.8V
    * - 35
      - HDMI_TX_HPDIN
      - HDMI HPD input
      - 
      - 3.3V
    * - 36
      - HDMI_TXCLKN
      - 
      - 
      - 1.8V
    * - 37
      - HDMI_TXCLKP
      - 
      - 
      - 1.8V
    * - 38
      - HDMI_TX0N
      - 
      - 
      - 1.8V
    * - 39
      - HDMI_TX0P
      - 
      - 
      -  1.8V
    * - 40
      - HDMI_TX1N
      - 
      - 
      - 1.8V

      

+---+-------------+------------------+---+------+--------------------+
| P | Signal      | Description      | P | Si   | Description        |
| i |             |                  | i | gnal |                    |
| n |             |                  | n |      |                    |
+===+=============+==================+===+======+====================+
| 1 | VCC12V_DCIN | Main power       | 2 | GND  | Ground             |
|   |             | supply.          |   |      |                    |
|   |             |                  |   |      |                    |
|   |             | DC 12V power in  |   |      |                    |
+---+-------------+------------------+---+------+--------------------+
| 3 | GND         | Ground           |   |      |                    |
+---+-------------+------------------+---+------+--------------------+




2 Peripherals Introduction
--------------------------

2.1 Power (P1)
^^^^^^^^^^^^^^^^^^^^^^

2.2 Audio I/O 
^^^^^^^^^^^^^^^^^^^^^^

2.3 HDMI OUT (J4)
^^^^^^^^^^^^^^^^^^^^^^

2.4 USB OTG (J29)
^^^^^^^^^^^^^^^^^^^^^^

2.5 USB HOST (P3, J6, J17)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.6 USB3.0/SATA3.0 (J25, J34)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.7 Ethernet (JP1)
^^^^^^^^^^^^^^^^^^^^^^

2.8 eDP/LVDS/MIPI Panel (CON1)
^^^^^^^^^^^^^^^^^^^^^^

2.9 BT656 (J26) 
^^^^^^^^^^^^^^^^^^^^^^

2.10 GPIO (CON4)
^^^^^^^^^^^^^^^^^^^^^^

2.11 ADC (J18)
^^^^^^^^^^^^^^^^^^^^^^

2.12 MIPI Camera (J30, J31)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.13 IR (J24)
^^^^^^^^^^^^^^^^^^^^^^

2.14 UART (J10, J11, J12)
^^^^^^^^^^^^^^^^^^^^^^

2.15 RS485 (J32, JP2)
^^^^^^^^^^^^^^^^^^^^^^

2.16 Button (K3)
^^^^^^^^^^^^^^^^^^^^^^

2.17 4G Module (CON2, P4)	25
^^^^^^^^^^^^^^^^^^^^^^

2.18 Micro SD (J3) 
^^^^^^^^^^^^^^^^^^^^^^

2.19 WiFi&Bluetooth (U20)
^^^^^^^^^^^^^^^^^^^^^^

2.20 SSD (CON3)
^^^^^^^^^^^^^^^^^^^^^^

2.21 GPS (MU4)
^^^^^^^^^^^^^^^^^^^^^^

2.22 RTC (BT1)
^^^^^^^^^^^^^^^^^^^^^^


3 Product Configurations
--------------------------

3.1 Standard Contents
^^^^^^^^^^^^^^^^^^^^^^

3.2 Optional Parts
^^^^^^^^^^^^^^^^^^^^^^
