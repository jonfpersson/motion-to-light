# Applied IoT Project: Desk LED Light Strip with PIR Sensor and Raspberry Pi Pico

This repository documents my project completed for the "Applied IoT" course at Linnaeus University. The project aimed to create an IoT (Internet of Things) solution that would automatically light up my desk LED light strip using a PIR (Passive Infrared) sensor and a Raspberry Pi Pico running MicroPython. The combination of hardware and software allowed me to achieve an energy-efficient and convenient lighting system for my desk.

Read more about my project at https://hackmd.io/@xIwJLprdRfeHLCV8NCsRRg/jonfp

## Table of Contents

- [Applied IoT Project: Desk LED Light Strip with PIR Sensor and Raspberry Pi Pico](#applied-iot-project-desk-led-light-strip-with-pir-sensor-and-raspberry-pi-pico)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Hardware](#hardware)
  - [Software](#software)
  - [How it Works](#how-it-works)
  - [Future Improvements](#future-improvements)
  - [Acknowledgments](#acknowledgments)

## Introduction

The project's objective was to build an IoT device that could sense the presence of a person near my desk using a PIR sensor. When the sensor detected motion, it would signal the Raspberry Pi Pico to turn on the LED light strip. After a predefined period of inactivity, the lights would automatically turn off. This project allowed me to explore concepts related to IoT, sensor integration, and basic automation using a microcontroller.

## Hardware

The hardware components used in this project are:

- Raspberry Pi Pico: The microcontroller responsible for processing the sensor data and controlling the LED light strip.
- PIR Sensor: The Passive Infrared sensor that detects motion in its vicinity.
- LED Light Strip: The addressable RGB LED strip that illuminates the desk area.
- Power Supply: Provides power to the Raspberry Pi Pico and the LED light strip.

## Software

The project's software components include:

- MicroPython: The firmware running on the Raspberry Pi Pico, programmed to read data from the PIR sensor and control the LED strip accordingly.
- Python Script: The Python script running on the Raspberry Pi or any connected device to visualize the sensor data and manage settings.

## How it Works

1. The PIR sensor continuously monitors the desk area for motion.
2. When motion is detected, the sensor sends a signal to the Raspberry Pi Pico.
3. The Raspberry Pi Pico, running MicroPython, receives the signal and activates the LED light strip.
4. After a predefined period of inactivity, the Raspberry Pi Pico turns off the LED lights.

## Future Improvements

This project lays the foundation for more advanced IoT solutions. Some potential improvements and expansions include:

- Integrating with a home automation system like Home Assistant to control the lights remotely.
- Adding Bluetooth or Wi-Fi connectivity to allow control from a smartphone app.
- Implementing different lighting patterns and colors based on user preferences.

## Acknowledgments

I would like to express my gratitude to the professors and course assistants at Linnaeus University for their guidance and support throughout the "Applied IoT" course. Additionally, I thank the MicroPython community for their excellent documentation and resources that helped me implement this project.

Feel free to explore the code and hardware setup in this repository. If you have any questions or suggestions, please feel free to reach out. Happy tinkering with IoT!
