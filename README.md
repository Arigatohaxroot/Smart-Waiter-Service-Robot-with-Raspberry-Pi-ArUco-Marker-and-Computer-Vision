# Smart Waiter Service Robot using Raspberry Pi and ArUco Marker

<p align="center">
  <a href="https://youtu.be/QC5sIvi7I5M?si=O_mW_tvGuTnAXPjV">
    <img src="https://img.youtube.com/vi/QC5sIvi7I5M/0.jpg" alt="Watch the Video">
  </a>
</p>

The smart waiter service robot project intends to change the restaurant sector by delivering a new solution for efficient and smooth service. The project focuses on the creation and implementation of a robot that can fulfill the functions of a waiter in a restaurant setting. By integrating modern technologies such as robotics, computer vision, and artificial intelligence, the robot is meant to traverse the restaurant environment, take orders, serve meals, and assist clients.

<p align="center">
  <img src="https://i.imgur.com/VS7B6X8.jpg" alt="Smart Waiter Robot">
</p>

## Project Overview

The fundamental feature of the smart waiter service robot is built around its capacity to autonomously explore the restaurant. A mix of hardware components, including a Raspberry Pi 4 Model B with 4GB RAM, Pi camera, ultrasonic sensor, IR sensor, and DC motors with an L298N driver IC, provides the foundation for the robot's physical mobility. The robot employs computer vision capabilities, specifically the identification of Aruco markers, to accurately navigate towards preset tables or specific spots throughout the restaurant.

<p align="center">
  <img src="https://i.imgur.com/Xhxorf3.jpg" alt="Aruco Marker Detection">
</p>

To enhance the user experience and speed the ordering process, the project comprises the construction of a graphical user interface (GUI) map. This map allows customers to build a visual depiction of the restaurant layout, aiding easy table selection and navigation for the robot. Additionally, clients have the option to place their purchases using a specialized mobile app or website, eliminating the need for human order-taking and minimizing waiting times.

<p align="center">
  <img src="https://i.imgur.com/Ygb7sot.jpg" alt="GUI Map 1">
  <img src="https://i.imgur.com/VpWJ6D4.jpg" alt="GUI Map 2">
</p>

To simplify remote control and monitoring, the project combines VNC viewer capability, enabling users to manage the robot using their mobile devices, PCs, or TVs. This function enables flexibility and ease in managing the robot's motions and activities from a distance.

The Restaurant Serving System (RSS), driven by the smart waiter service robot, promises to enhance the quality of service in restaurants by eliminating human mistakes, decreasing operating expenses, and boosting overall customer happiness. By automating the serving process, restaurants may boost production, optimize resource allocation, and create a seamless eating experience.

<p align="center">
  <img src="https://i.imgur.com/YW8eRAA.jpg" alt="Online Meal Order">
</p>

In short, the smart waiter service robot project integrates hardware components, computer vision algorithms, GUI mapping, and autonomous operation to produce a dependable and efficient solution for restaurant service. The integration of innovative technology and user-friendly interfaces opens the way for increased customer experiences and improved productivity in the restaurant business.

## System Architecture

The system architecture of the smart waiter service robot project is depicted as follows:

### User Interface:
- GUI: Provides a graphical interface for constructing the restaurant map and sending orders to the robot.
- VNC Viewer: Allows remote operation of the robot from a mobile device or PC via Wi-Fi.

### Raspberry Pi 4:
- Central processing unit responsible for regulating the robot's actions and managing its components.
- Receives commands from the user interface and processes sensor data.

### Pi Camera:
- Captures visual information of the Aruco markers.
- Provides input for marker detection and localization.

### Aruco Marker Detection:
- Utilizes computer vision methods to detect and recognize Aruco markings placed on the floor.
- Extracts encoded information from the markers to calculate movement directions.

### Map Building:
- Allows the user to generate a map of the restaurant using the GUI.
- The map provides information about table placements and pathways for the robot to follow.

### Obstacle Detection:
- Ultrasonic Sensor: Measures distances to detect impediments in the robot's route.
- When an impediment is spotted, the sensor emits a buzzer to warn the obstacle and urges it to move.

### Movement Control:
- DC Motors: Connected to the L298N driver IC, controlled by the Raspberry Pi 4.
- Receives movement orders based on the Aruco marker information and map guidance.
- Enables precise movement control of the robot, following predetermined pathways and directions.

### IR Sensor:
- Assists in obtaining precise movement by sensing and following a specified path.
- Helps the robot navigate along the set itinerary inside the restaurant area.

### Wi-Fi Connectivity:
- Enables connection between the Raspberry Pi 4 and the user interface (VNC Viewer) for remote operation.
- Provides wireless control and command delivery to the robot.

### Rechargeable Battery:
- Powers the robot and supplies electrical energy for all its components.
- Offers mobility and flexibility by eliminating the need for a wired power supply.

### Restaurant Environment:
- Represents the physical environment where the robot operates, including tables, barriers, and passageways.

## Software Requirements:
- Raspbian: The operating system required for the Raspberry Pi 4.
- Python 3: The programming language used for developing the software.
- Thonny Compiler: An integrated development environment (IDE) for Python, used for coding and testing the software.
- ArucoMarker Library: A library for detecting and recognizing Aruco markers in captured images.
- OpenCV Library: A popular computer vision library used for image processing, marker detection, and camera input.
- Wi-Fi Connectivity: Required for communication between the Raspberry Pi 4 and the user interface (VNC Viewer) for remote operation.

## Hardware Requirements:
- Raspberry Pi 4: The main control unit of the robot, responsible for processing and controlling the various components.
- Pi Camera: A camera module connected to the Raspberry Pi 4, used for capturing visual information and detecting Aruco markers.
- Ultrasonic Sensor: Used for obstacle detection and measuring distances to avoid collisions.
- IR Sensor: Assists in achieving accurate movement and following predefined paths.
- DC Motors: Used for robot movement, controlled by an L298N driver IC.
- Rechargeable Battery: Powers the robot and supplies electrical energy for all its components.
- Wi-Fi Module: Enables wireless communication for remote operation and control.

## Libraries Used:
- `tkinter` for graphical user interface (GUI)
- `pygame` for interactive applications and games
- `RPi.GPIO` for Raspberry Pi GPIO control
- `cv2` for computer vision tasks using OpenCV
- `cv2.aruco` for ArUco marker detection
- `numpy` for numerical computations
- `os` for interacting with the operating system
- `time` for handling time-related operations
- `threading` and `multiprocessing` for managing threads and processes
- `pickle` for serializing and deserializing Python objects

For detailed code implementations, usage instructions, and additional project materials, please refer to the project's [Code File] and [PPT Slide] provided in the repository.
