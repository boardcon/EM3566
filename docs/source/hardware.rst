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

    * - Specifications
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
      - HDMI 2.0, 4Kp60. MIPI DSI/LVDS, 1080p60. eDP 1.3, 2560x1600@60Hz. MEMS_Module for Video output.
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
    * - 7
      - 
      - 
      - 
      -       
    * - 8
      - 
      - 
      - 
      - 
    * - 9
      - 
      - 
      - 
      -   
    * - 10
      - 
      - 
      - 
      -


 ================================================================================================================================== ========================================== ============================================== ========================= ===================== 
  
  Pin
                                                                                                                          
  Signal
                               
  Description or functions
                 
  GPIO serial
         
  IO Voltage
     
 ================================================================================================================================== ========================================== ============================================== ========================= ===================== 
  
  1
                                                                                                                            
  VCC3V3_SYS
                           
  3.3V Main Power input
                    
  &nbsp;
              
  3.3V
           
  
  2
                                                                                                                            
  VCC3V3_SYS
                           
  3.3V Main Power input
                    
  &nbsp;
              
  3.3V
           
  
  3
                                                                                                                            
  VCC3V3_SYS
                           
  3.3V Main Power input
                    
  &nbsp;
              
  3.3V
           
  
  4
                                                                                                                            
  VCC_RTC
                              
  RTC button
  Cell Power input
           
  &nbsp;
              
  3.0V-1.8V
      
  
  5
                                                                                                                            
  PMIC_32KOUT
                          
  RTC clock(32.768khz) output
              
  &nbsp;
              
  3.3V
           
  
  6
                                                                                                                            
  GND
                                  
  Ground
                                   
  &nbsp;
              
  0V
             
  
  7
                                                                                                                            
  HDMITX_CEC_M0
                        
  &nbsp;
                                   
  GPIO4_D1_u
          
  3.3V
           
  
  8
                                                                                                                            
  HDMITX_SDA
                           
  Pull up 2.2K inside
                      
  GPIO4_D0_u
          
  3.3V
           
  
  9
                                                                                                                            
  HDMITX_SCL
                           
  Pull up 2.2K inside
                      
  GPIO4_C7_u
          
  3.3V
           
  
  10
                                                                                                                           
  GND
                                  
  Ground
                                   
  &nbsp;
              
  0V
             
  
  11
                                                                                                                           
  GMAC1_MCLKINOUT_M0
                   
  RGMII reference clock input(125Mhz)
      
  GPIO3_C0_d
          
  3.3V
           
  
  12
                                                                                                                           
  GND
                                  
  Ground
                                   
  &nbsp;
              
  0V
             
  
  13
                                                                                                                           
  GMAC1_TXD0_M0
                        
  &nbsp;
                                   
  GPIO3_B5_d
          
  3.3V
           
  
  14
                                                                                                                           
  GMAC1_TXD1_M0
                        
  &nbsp;
                                   
  GPIO3_B6_d
          
  3.3V
           
  
  15
                                                                                                                           
  GMAC1_TXEN_M0
                        
  &nbsp;
                                   
  GPIO3_B7_d
          
  3.3V
           
  
  16
                                                                                                                           
  GMAC1_RXDV_CRS_M0
                    
  &nbsp;
                                   
  GPIO3_B3_d
          
  3.3V
           
  
  17
                                                                                                                           
  GMAC1_RXD1_M0
                        
  &nbsp;
                                   
  GPIO3_B2_d
          
  3.3V
           
  
  18
                                                                                                                           
  GMAC1_RXD0_M0
                        
  &nbsp;
                                   
  GPIO3_B1_d
          
  3.3V
           
  
  19
                                                                                                                           
  GMAC1_RXD3_M0
                        
  &nbsp;
                                   
  GPIO3_A5_d
          
  3.3V
           
  
  20
                                                                                                                           
  GMAC1_RXD2_M0
                        
  &nbsp;
                                   
  GPIO3_A4_d
          
  3.3V
           
  
  21
                                                                                                                           
  GMAC1_RXCLK_M0
                       
  &nbsp;
                                   
  GPIO3_A7_d
          
  3.3V
           
  
  22
                                                                                                                           
  GMAC1_TXD2_M0
                        
  &nbsp;
                                   
  GPIO3_A2_d
          
  3.3V
           
  
  23
                                                                                                                           
  GMAC1_TXD3_M0
                        
  &nbsp;
                                   
  GPIO3_A3_d
          
  3.3V
           
  
  24
                                                                                                                           
  GMAC1_TXCLK_M0
                       
  &nbsp;
                                   
  GPIO3_A6_d
          
  3.3V
           
  
  25
                                                                                                                           
  MIPI_DSI_TX0_D3N/LVDS_TX0_D3N
        
  MIPI DSI or LVDS TXD3N
                   
  &nbsp;
              
  1.8V
           
  
  26
                                                                                                                           
  MIPI_DSI_TX0_D3P/LVDS_TX0_D3P
        
  MIPI DSI or LVDS TXD3P
                   
  &nbsp;
              
  1.8V
           
  
  27
                                                                                                                           
  MIPI_DSI_TX0_D2N/LVDS_TX0_D2N
        
  MIPI DSI or LVDS TXD2N
                   
  &nbsp;
              
  1.8V
           
  
  28
                                                                                                                           
  MIPI_DSI_TX0_D2P/LVDS_TX0_D2P
        
  MIPI DSI or LVDS TXD2P
                   
  &nbsp;
              
  1.8V
           
  
  29
                                                                                                                           
  MIPI_DSI_TX0_D1N/LVDS_TX0_D1N
        
  MIPI DSI or LVDS TXD1N
                   
  &nbsp;
              
  1.8V
           
  
  30
                                                                                                                           
  MIPI_DSI_TX0_D1P/LVDS_TX0_D1P
        
  MIPI DSI or LVDS TXD1P
                   
  &nbsp;
              
  1.8V
           
  
  31
                                                                                                                           
  MIPI_DSI_TX0_D0N/LVDS_TX0_D0N
        
  MIPI DSI or LVDS TXD1N
                   
  &nbsp;
              
  1.8V
           
  
  32
                                                                                                                           
  MIPI_DSI_TX0_D0P/LVDS_TX0_D0P
        
  MIPI DSI or LVDS TXD1P
                   
  &nbsp;
              
  1.8V
           
  
  33
                                                                                                                           
  MIPI_DSI_TX0_CLKN/LVDS_TX0_CLKN
      
  MIPI DSI or LVDS TXD1N
                   
  &nbsp;
              
  1.8V
           
  
  34
                                                                                                                           
  MIPI_DSI_TX0_CLKP/LVDS_TX0_CLKP
      
  MIPI DSI or LVDS TXD1P
                   
  &nbsp;
              
  1.8V
           
  
  35
                                                                                                                           
  HDMI_TX_HPDIN
                        
  HDMI HPD input
                           
  &nbsp;
              
  3.3V
           
  
  36
                                                                                                                           
  HDMI_TXCLKN
                          
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  37
                                                                                                                           
  HDMI_TXCLKP
                          
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  38
                                                                                                                           
  HDMI_TX0N
                            
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  39
                                                                                                                           
  HDMI_TX0P
                            
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  40
                                                                                                                           
  HDMI_TX1N
                            
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  41
                                                                                                                           
  HDMI_TX1P
                            
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  42
                                                                                                                           
  HDMI_TX2N
                            
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  43
                                                                                                                           
  HDMI_TX2P
                            
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  44
                                                                                                                           
  MIPI_CSI_RX_CLK1N
                    
  MIPI CSI1 CLKN
                           
  &nbsp;
              
  1.8V
           
  
  45
                                                                                                                           
  MIPI_CSI_RX_CLK1P
                    
  MIPI CSI1 CLKP
                           
  &nbsp;
              
  1.8V
           
  
  46
                                                                                                                           
  MIPI_CSI_RX_D3N
                      
  CSI0 RXD3N or CSI1 RXD1N
                 
  &nbsp;
              
  1.8V
           
  
  47
                                                                                                                           
  MIPI_CSI_RX_D3P
                      
  CSI0 RXD3P or CSI1
  RXD1P
              
  &nbsp;
              
  1.8V
           
  
  48
                                                                                                                           
  MIPI_CSI_RX_D2N
                      
  CSI0 RXD2N or CSI1 RXD0N
                 
  &nbsp;
              
  1.8V
           
  
  49
                                                                                                                           
  MIPI_CSI_RX_D2P
                      
  CSI0 RXD2P or CSI1
  RXD0P
              
  &nbsp;
              
  1.8V
           
  
  50
                                                                                                                           
  MIPI_CSI_RX_D1P
                      
  CSI0 RXD1P
                               
  &nbsp;
              
  1.8V
           
  
  51
                                                                                                                           
  MIPI_CSI_RX_D1N
                      
  CSI0 RXD1N
                               
  &nbsp;
              
  1.8V
           
  
  52
                                                                                                                           
  MIPI_CSI_RX_D0N
                      
  CSI0 RXD0N
                               
  &nbsp;
              
  1.8V
           
  
  53
                                                                                                                           
  MIPI_CSI_RX_D0P
                      
  CSI0 RXD0P
                               
  &nbsp;
              
  1.8V
           
  
  54
                                                                                                                           
  MIPI_CSI_RX_CLK0N
                    
  MIPI CSI0 CLKN
                           
  &nbsp;
              
  1.8V
           
  
  55
                                                                                                                           
  MIPI_CSI_RX_CLK0P
                    
  MIPI CSI0 CLKP
                           
  &nbsp;
              
  1.8V
           
  
  56
                                                                                                                           
  GND
                                  
  Ground
                                   
  &nbsp;
              
  0V
             
  
  57
                                                                                                                           
  PWM5
                                 
  &nbsp;
                                   
  GPIO0_C4_d
          
  3.3V
           
  
  58
                                                                                                                           
  LCD_BL_PWM
                           
  PWM4
                                     
  GPIO0_C3_d
          
  3.3V
           
  
  59
                                                                                                                           
  PWM3_IR
                              
  &nbsp;
                                   
  GPIO0_C2_d
          
  3.3V
           
  
  60
                                                                                                                           
  PCIE20_SATA2_RXP
                     
  PCIE or SATA2 RXP
                        
  &nbsp;
              
  1.8V
           
  
  61
                                                                                                                           
  PCIE20_SATA2_RXN
                     
  PCIE or SATA2 RXN
                        
  &nbsp;
              
  1.8V
           
  
  62
                                                                                                                           
  PCIE20_SATA2_TXN
                     
  PCIE or SATA2 TXN
                        
  &nbsp;
              
  1.8V
           
  
  63
                                                                                                                           
  PCIE20_SATA2_TXP
                     
  PCIE or SATA2 TXP
                        
  &nbsp;
              
  1.8V
           
  
  64
                                                                                                                           
  PCIE20_REFCLKP
                       
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  65
                                                                                                                           
  PCIE20_REFCLKN
                       
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  66
                                                                                                                           
  USB3_HOST1_SSTXP
                     
  USB3.0 or SATA1 TXP
                      
  &nbsp;
              
  1.8V
           
  
  67
                                                                                                                           
  USB3_HOST1_SSTXN
                     
  USB3.0 or SATA1 TXN
                      
  &nbsp;
              
  1.8V
           
  
  68
                                                                                                                           
  USB3_HOST1_SSRXP
                     
  USB3.0 or SATA1 RXN
                      
  &nbsp;
              
  1.8V
           
  
  69
                                                                                                                           
  USB3_HOST1_SSRXN
                     
  USB3.0 or SATA1 RXP
                      
  &nbsp;
              
  1.8V
           
  
  70
                                                                                                                           
  USB_OTG0_DM
                          
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  71
                                                                                                                           
  USB_OTG0_DP
                          
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  72
                                                                                                                           
  USB3_HOST1_DP
                        
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  73
                                                                                                                           
  USB3_HOST1_DM
                        
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  74
                                                                                                                           
  EDP_TX_D2N
                           
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  75
                                                                                                                           
  EDP_TX_D2P
                           
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  76
                                                                                                                           
  EDP_TX_D1N
                           
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  77
                                                                                                                           
  EDP_TX_D1P
                           
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  78
                                                                                                                           
  EDP_TX_D0N
                           
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  79
                                                                                                                           
  EDP_TX_D0P
                           
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  80
                                                                                                                           
  EDP_TX_D3N
                           
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  81
                                                                                                                           
  EDP_TX_D3P
                           
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  82
                                                                                                                           
  EDP_TX_AUXN
                          
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  83
                                                                                                                           
  EDP_TX_AUXP
                          
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  84
                                                                                                                           
  SDMMC0_DET_L
                         
  &nbsp;
                                   
  GPIO0_A4_u
          
  3.3V
           
  
  85
                                                                                                                           
  SDMMC0_CLK
                           
  UART5_TX_M0
                              
  GPIO2_A2_d
          
  3.3V
           
  
  86
                                                                                                                           
  GND
                                  
  Ground
                                   
  &nbsp;
              
  0V
             
  
  87
                                                                                                                           
  SDMMC0_CMD
                           
  UART5_RX_M0
                              
  GPIO2_A1_u
          
  3.3V
           
  
  88
                                                                                                                           
  SDMMC0_D3
                            
  UART5_RTSn_M0
                            
  GPIO2_A0_u
          
  3.3V
           
  
  89
                                                                                                                           
  SDMMC0_D2
                            
  UART5_CTSn_M0
                            
  GPIO1_D7_u
          
  3.3V
           
  
  90
                                                                                                                           
  SDMMC0_D1
                            
  UART6_RX_M1
                              
  GPIO1_D6_u
          
  3.3V
           
  
  91
                                                                                                                           
  SDMMC0_D0
                            
  UART6_TX_M1
                              
  GPIO1_D5_u
          
  3.3V
           
  
  92
                                                                                                                           
  USB_OTG0_ID
                          
  &nbsp;
                                   
  &nbsp;
              
  3.3V
           
  
  93
                                                                                                                           
  USB_OTG0_VBUSDET
                     
  USB OTG VBUS input
                       
  &nbsp;
              
  3.3V
           
  
  94
                                                                                                                           
  UART1_RX_M0
                          
  &nbsp;
                                   
  GPIO2_B3_u
          
  1.8V
           
  
  95
                                                                                                                           
  UART1_TX_M0
                          
  &nbsp;
                                   
  GPIO2_B4_u
          
  1.8V
           
  
  96
                                                                                                                           
  UART1_RTSn_M0
                        
  &nbsp;
                                   
  GPIO2_B5_u
          
  1.8V
           
  
  97
                                                                                                                           
  UART1_CTSn_M0
                        
  &nbsp;
                                   
  GPIO2_B6_u
          
  1.8V
           
  
  98
                                                                                                                           
  BT_REG_ON_H
                          
  I2S2_SCLK_RX_M0
                          
  GPIO2_B7_d
          
  1.8V
           
  
  99
                                                                                                                           
  BT_WAKE_HOST_H
                       
  I2S2_LRCLK_RX_M0
                         
  GPIO2_C0_d
          
  1.8V
           
  
  100
                                                                                                                          
  HOST_WAKE_BT_H
                       
  I2S2_MCLK_M0
                             
  GPIO2_C1_d
          
  1.8V
           
  
  101
                                                                                                                          
  WIFI_WAKE_HOST_H
                     
  I2C4_SCL_M1
                              
  GPIO2_B2_d
          
  1.8V
           
  
  102
                                                                                                                          
  WIFI_REG_ON_H
                        
  UART8_RX_M0
                              
  GPIO2_C6_d
          
  1.8V
           
  
  103
                                                                                                                          
  I2S2_SCLK_TX_M0
                      
  SPI2_MISO_M0
                             
  GPIO2_C2_d
          
  1.8V
           
  
  104
                                                                                                                          
  I2S2_LRCK_TX_M0
                      
  SPI2_MOSI_M0
                             
  GPIO2_C3_d
          
  1.8V
           
  
  105
                                                                                                                          
  I2S2_SDO_M0
                          
  SPI2_CS0_M0
                              
  GPIO2_C4_d
          
  1.8V
           
  
  106
                                                                                                                          
  I2S2_SDI_M0
                          
  UART8_TX_M0
                              
  GPIO2_C5_d
          
  1.8V
           
  
  107
                                                                                                                          
  SDMMC1_D3
                            
  UART7_TX_M0
                              
  GPIO2_A6_u
          
  1.8V
           
  
  108
                                                                                                                          
  SDMMC1_D2
                            
  UART7_RX_M0
                              
  GPIO2_A5_u
          
  1.8V
           
  
  109
                                                                                                                          
  SDMMC1_D1
                            
  UART6_TX_M0
                              
  GPIO2_A4_u
          
  1.8V
           
  
  110
                                                                                                                          
  SDMMC1_D0
                            
  UART6_RX_M0
                              
  GPIO2_A3_u
          
  1.8V
           
  
  111
                                                                                                                          
  SDMMC1_CMD
                           
  UART9_RX_M0
                              
  GPIO2_A7_u
          
  1.8V
           
  
  112
                                                                                                                          
  SDMMC1_CLK
                           
  UART9_TX_M0
                              
  GPIO2_B0_d
          
  1.8V
           
  
  113
                                                                                                                          
  GND
                                  
  Ground
                                   
  &nbsp;
              
  0V
             
  
  114
                                                                                                                          
  SARADC_VIN3
                          
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  115
                                                                                                                          
  SARADC_VIN2_HP_HOOK
                  
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  116
                                                                                                                          
  SARADC_VIN0_KEY/RECOVERY
             
  Pull up 10K inside
                       
  &nbsp;
              
  1.8V
           
  
  117
                                                                                                                          
  GND
                                  
  Ground
                                   
  &nbsp;
              
  0V
             
  
  118
                                                                                                                          
  PCIE20_PERSTn_M2
                     
  PDM_SDI1_M0
                              
  GPIO1_B2_d
          
  3.3V
           
  
  119
                                                                                                                          
  PCIE20_WAKEn_M2
                      
  PDM_SDI2_M0
                              
  GPIO1_B1_d
          
  3.3V
           
  
  120
                                                                                                                          
  PCIE20_CLKREQn_M2
                    
  PDM_SDI3_M0
                              
  GPIO1_B0_d
          
  3.3V
           
  
  121
                                                                                                                          
  UART3_RX_M0
                          
  AudioPWM_LOUT_P/I2C3_SDA_M0
              
  GPIO1_A0_u
          
  3.3V
           
  
  122
                                                                                                                          
  UART3_TX_M0
                          
  AudioPWM_LOUT_N/I2C3_SCL_M0
              
  GPIO1_A1_u
          
  3.3V
           
  
  123
                                                                                                                          
  UART4_RX_M0
                          
  PDM_CLK1_M0/SPDIF_TX_M0
                  
  GPIO1_A4_d
          
  3.3V
           
  
  124
                                                                                                                          
  UART4_TX_M0
                          
  AudioPWM_ROUT_P /PDM_CLK0_M0
             
  GPIO1_A6_d
          
  3.3V
           
  
  125
                                                                                                                          
  I2S1_LRCK_TX_M0_PMIC
                 
  &nbsp;
                                   
  GPIO1_A5_d
          
  3.3V
           
  
  126
                                                                                                                          
  I2S1_SDI0_M0/PDM_SDI0_M0_PMIC
        
  PDM_SDI0_M0
                              
  GPIO1_B3_d
          
  3.3V
           
  
  127
                                                                                                                          
  I2S1_SCLK_TX_M0_PMIC
                 
  UART3_CTSn_M0
                            
  GPIO1_A3_d
          
  3.3V
           
  
  128
                                                                                                                          
  I2S1_SDO0_M0_PMIC
                    
  AudioPWM_ROUT_N/UART4_CTSn_M0
            
  GPIO1_A7_d
          
  3.3V
           
  
  129
                                                                                                                          
  I2S1_MCLK_M0_PMIC
                    
  UART3_RTSn_M0
                            
  GPIO1_A2_d
          
  3.3V
           
  
  130
                                                                                                                          
  GND
                                  
  Ground
                                   
  &nbsp;
              
  0V
             
  
  131
                                                                                                                          
  SPI0_CS0_M0
                          
  PWM7
                                     
  GPIO0_C6_d
          
  3.3V
           
  
  132
                                                                                                                          
  SPI0_MISO_M0
                         
  PWM6
                                     
  GPIO0_C5_d
          
  3.3V
           
  
  133
                                                                                                                          
  SPI0_MOSI_M0
                         
  I2C2_SDA_M0
                              
  GPIO0_B6_u
          
  3.3V
           
  
  134
                                                                                                                          
  SPI0_CLK_M0
                          
  I2C2_SCL_M0
                              
  GPIO0_B5_u
          
  3.3V
           
  
  135
                                                                                                                          
  SPI3_CS0_M1
                          
  I2S3_SDI _M1
                             
  GPIO4_C6_d
          
  3.3V
           
  
  136
                                                                                                                          
  SPI3_MISO_M1
                         
  I2S3_SDO _M1
                             
  GPIO4_C5_d
          
  3.3V
           
  
  137
                                                                                                                          
  SPI3_MOSI_M1
                         
  I2S3_SCLK_M1
                             
  GPIO4_C3_d
  
      
  3.3V
           
  
  138
                                                                                                                          
  SPI3_CLK_M1
                          
  I2S3_MCLK_M1
                             
  GPIO4_C2_d
          
  3.3V
           
  
  139
                                                                                                                          
  LCD_PWREN_H
                          
  &nbsp;
                                   
  GPIO0_C7_d
          
  3.3V
           
  
  140
                                                                                                                          
  PWM0_M0
                              
  &nbsp;
                                   
  GPIO0_B7_d
          
  3.3V
           
  
  141
                                                                                                                          
  UART5_RX_M1
                          
  &nbsp;
                                   
  GPIO3_C3_d
          
  3.3V
           
  
  142
                                                                                                                          
  UART5_TX_M1
                          
  &nbsp;
                                   
  GPIO3_C2_d
          
  3.3V
           
  
  143
                                                                                                                          
  UART2DBG_RX
                          
  UART2 for Debug
                          
  GPIO0_D0_u
          
  3.3V
           
  
  144
                                                                                                                          
  UART2DBG_TX
                          
  UART2 for Debug
                          
  GPIO0_D1_u
          
  3.3V
           
  
  145
                                                                                                                          
  SPDIF_TX_M2
                          
  I2S3_LRCK_M1/EDP_HPDIN_M0
                
  GPIO4_C4_d
          
  3.3V
           
  
  146
                                                                                                                          
  GPIO0_A6_d
                           
  &nbsp;
                                   
  &nbsp;
              
  3.3V
           
  
  147
                                                                                                                          
  GPIO0_A3_u
                           
  &nbsp;
                                   
  &nbsp;
              
  3.3V
           
  
  148
                                                                                                                          
  GPIO0_A0_d
                           
  &nbsp;
                                   
  &nbsp;
              
  3.3V
           
  
  149
                                                                                                                          
  CAMERAF_RST_L
                        
  CAM_CLKOUT1
                              
  GPIO4_B0_d
          
  1.8V
           
  
  150
                                                                                                                          
  CAMERAB_RST_L
                        
  &nbsp;
                                   
  GPIO4_B1_d
          
  1.8V
           
  
  151
                                                                                                                          
  CIF_8BIT_D7
                          
  CIF_D15
                                  
  GPIO4_A5_d
          
  1.8V
           
  
  152
                                                                                                                          
  CIF_8BIT_D6
                          
  CIF_D14
                                  
  GPIO4_A4_d
          
  1.8V
           
  
  153
                                                                                                                          
  CIF_8BIT_D5
                          
  CIF_D13
                                  
  GPIO4_A3_d
          
  1.8V
           
  
  154
                                                                                                                          
  CIF_8BIT_D4
                          
  CIF_D12
                                  
  GPIO4_A2_d
          
  1.8V
           
  
  155
                                                                                                                          
  CIF_8BIT_D3
                          
  CIF_D11
                                  
  GPIO4_A1_d
          
  1.8V
           
  
  156
                                                                                                                          
  CIF_8BIT_D2
                          
  CIF_D10
                                  
  GPIO4_A0_d
          
  1.8V
           
  
  157
                                                                                                                          
  CIF_8BIT_D1
                          
  CIF_D9
                                   
  GPIO3_D7_d
          
  1.8V
           
  
  158
                                                                                                                          
  CIF_8BIT_D0
                          
  CIF_D8
                                   
  GPIO3_D6_d
          
  1.8V
           
  
  159
                                                                                                                          
  GND
                                  
  Ground
                                   
  &nbsp;
              
  0V
             
  
  160
                                                                                                                          
  USB2_HOST2_DM
                        
  HOST2_DM
                                 
  &nbsp;
              
  1.8V
           
  
  161
                                                                                                                          
  USB2_HOST2_DP
                        
  HOST2_DP
                                 
  &nbsp;
              
  1.8V
           
  
  162
                                                                                                                          
  USB2_HOST3_DP
                        
  HOST3_DP
                                 
  &nbsp;
              
  1.8V
           
  
  163
                                                                                                                          
  USB2_HOST3_DM
                        
  HOST3_DM
                                 
  &nbsp;
              
  1.8V
           
  
  164
                                                                                                                          
  CIF_8BIT_VSYNC
                       
  &nbsp;
                                   
  GPIO4_B7_d
          
  1.8V
           
  
  165
                                                                                                                          
  CIF_8BIT_HREF
                        
  &nbsp;
                                   
  GPIO4_B6_d
          
  1.8V
           
  
  166
                                                                                                                          
  CIF_8BIT_CLKIN
                       
  &nbsp;
                                   
  GPIO4_C1_d
          
  1.8V
           
  
  167
                                                                                                                          
  GND
                                  
  Ground
                                   
  &nbsp;
              
  0V
             
  
  168
                                                                                                                          
  CIF_CLKOUT
                           
  &nbsp;
                                   
  GPIO4_C0_d
          
  1.8V
           
  
  169
                                                                                                                          
  VOP_BT656_D7_M1
                      
  CIF_D7
                                   
  GPIO3_D5_d
          
  1.8V
           
  
  170
                                                                                                                          
  VOP_BT656_D6_M1
                      
  CIF_D6
                                   
  GPIO3_D4_d
          
  1.8V
           
  
  171
                                                                                                                          
  VOP_BT656_D5_M1
                      
  CIF_D5
                                   
  GPIO3_D3_d
          
  1.8V
           
  
  172
                                                                                                                          
  VOP_BT656_D4_M1
                      
  CIF_D4
                                   
  GPIO3_D2_d
          
  1.8V
           
  
  173
                                                                                                                          
  VOP_BT656_D3_M1
                      
  CIF_D3
                                   
  GPIO3_D1_d
          
  1.8V
           
  
  174
                                                                                                                          
  VOP_BT656_D2_M1
                      
  CIF_D2
                                   
  GPIO3_D0_d
          
  1.8V
           
  
  175
                                                                                                                          
  VOP_BT656_D1_M1
                      
  CIF_D1
                                   
  GPIO3_C7_d
          
  1.8V
           
  
  176
                                                                                                                          
  VOP_BT656_D0_M1
                      
  CIF_D0
                                   
  GPIO3_C6_d
          
  1.8V
           
  
  177
                                                                                                                          
  VOP_BT656_CLK_M1
                     
  &nbsp;
                                   
  GPIO4_B4_d
          
  1.8V
           
  
  178
                                                                                                                          
  GPIO4_B5_d_1V8
                       
  &nbsp;
                                   
  &nbsp;
              
  1.8V
           
  
  179
                                                                                                                          
  I2C4_SDA_M0_1V8
                      
  Pull up 2.2K inside
                      
  GPIO4_B2_d
          
  1.8V
           
  
  180
                                                                                                                          
  I2C4_SCL_M0_1V8
                      
  Pull up 2.2K inside
                      
  GPIO4_B3_d
          
  1.8V
           
  
  181
                                                                                                                          
  GND
                                  
  Ground
                                   
  &nbsp;
              
  0V
             
  
  182
                                                                                                                          
  I2C1_SDA
                             
  Pull up 2.2K inside
                      
  GPIO0_B4_u
          
  3.3V
           
  
  183
                                                                                                                          
  I2C1_SCL
                             
  Pull up 2.2K inside
                      
  GPIO0_B3_u
          
  3.3V
           
  
  184
                                                                                                                          
  GPIO0_A5_d
                           
  PCIE20_CLKREQn_M0
                        
  &nbsp;
              
  3.3V
           
  
  185
                                                                                                                          
  GMAC1_MDIO_M0
                        
  &nbsp;
                                   
  GPIO3_C5_d
          
  3.3V
           
  
  186
                                                                                                                          
  GMAC1_MDC_M0
                         
  &nbsp;
                                   
  GPIO3_C4_d
          
  3.3V
           
  
  Note:
  I2C1 can not be used for exclusive bus, such
  as CTP.
  RGMII default is 3.3V IO, but can
  change to 1.8V.
     
 ================================================================================================================================== 






























      

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
