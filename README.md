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

To enhance the user experience and streamline the ordering process, the project includes the development of a graphical user interface (GUI) map. This map empowers chefs and cashiers to create a visual representation of the restaurant layout, facilitating efficient table selection and navigation for the robot. The GUI enables the staff to designate specific tables for service and optimize the robot's route, ensuring accurate meal deliveries and minimizing delays.


<p align="center">
  <img src="https://i.imgur.com/Ygb7sot.jpg" alt="GUI Map 1">
  <img src="https://i.imgur.com/VpWJ6D4.jpg" alt="GUI Map 2">
</p>

To simplify remote control and monitoring, the project combines VNC viewer capability, enabling users to manage the robot using their mobile devices, PCs, or TVs. This function enables flexibility and ease in managing the robot's motions and activities from a distance.

The Restaurant Serving System (RSS), driven by the smart waiter service robot, promises to enhance the quality of service in restaurants by eliminating human mistakes, decreasing operating expenses, and boosting overall customer happiness. By automating the serving process, restaurants may boost production, optimize resource allocation, and create a seamless eating experience.
One of the remarkable features of the RSS is its compatibility with an online ordering platform. Customers can conveniently access the restaurant's website, select their desired menu items, and specify their table of choice. This capability empowers patrons to customize their dining experience, ensuring that their orders are accurately prepared and delivered to their designated tables. The integration of this online ordering mechanism minimizes waiting times and enhances overall customer convenience.

<p align="center">
  <img src="https://i.imgur.com/YW8eRAA.jpg" alt="Online Meal Order">
</p>

## How the System Works
The operational mechanism of the Restaurant Serving System (RSS) is designed to seamlessly blend modern technologies with the art of culinary service, ensuring efficient and precise meal deliveries. When a chef or kitchen staff member places prepared dishes onto the smart waiter service robot, they can utilize the graphical user interface (GUI) to designate the desired table for delivery within the restaurant.

## ArUco Marker-Based Navigation
Once the robot receives its mission, it taps into its array of advanced hardware components and software algorithms to execute the task. The key component in the navigation process is the use of ArUco markers strategically placed throughout the restaurant. These markers serve as navigation waypoints, allowing the robot to accurately determine its location and follow predefined pathways.As the robot navigates the restaurant environment, its onboard camera captures visual information of the ArUco markers. This information is then processed using computer vision techniques, enabling the robot to accurately identify and localize itself within the restaurant's layout. The robot's path planning algorithm relies on this marker-based navigation to efficiently reach the designated table.

## Handling Obstacles and Dynamic Path Planning
Should an obstacle be detected along the robot's path, its obstacle detection system comes into play. Utilizing ultrasonic sensors, the robot measures distances and identifies impediments. Upon detecting an obstacle, the robot emits a brief buzzer sound to alert nearby individuals. Simultaneously, the robot halts its movement, giving time for the obstacle to be addressed. Once the obstacle is cleared, the robot proceeds along its path, continuing its mission without disruption.

## Adaptive Navigation Strategy
However, if the obstacle remains in place and impedes the robot's intended route, the robot employs a sophisticated strategy. It rotates around its axis, using its sensors to assess alternative paths and navigate around the obstacle. If the robot identifies an unobstructed route, it will resume its course and proceed towards the designated table. In the event that no clear path is found, the robot reverses its direction and returns to its initial position, prompting the need for a new path designation.

## Intuitive Interaction with Staff and Patrons
Throughout this process, the robot's interactions are designed to be user-friendly and non-intrusive. Should the robot need to alter its path or seek assistance, it can gently turn around and display a visual cue indicating that it requires a new path designation. This intuitive interaction ensures that restaurant staff and patrons can easily engage with the robot, enhancing the overall dining experience.

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
