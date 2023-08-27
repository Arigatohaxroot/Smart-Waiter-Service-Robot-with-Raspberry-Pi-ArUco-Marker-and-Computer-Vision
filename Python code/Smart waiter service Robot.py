import tkinter as tk
import pygame
import RPi.GPIO as GPIO
import cv2
import cv2.aruco as aruco
import numpy as np
import os
import time
import threading
import multiprocessing
import pickle
ids = None
import sys
GPIO.setwarnings(False)
screen =pygame.display.set_mode([240,160])
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
speedleft=GPIO.PWM(12,100)
speedright=GPIO.PWM(13,100)
speedleft.start(20)
speedright.start(20)
# Set up ultrasonic sensor pins
TRIG_PIN = 17
ECHO_PIN = 25
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
# Set the pin number for the buzzer
buzzer_pin = 26
GPIO.setup(buzzer_pin, GPIO.OUT)
lir_pin = 5
GPIO.setup(lir_pin, GPIO.IN)
rir_pin= 6
GPIO.setup(rir_pin, GPIO.IN)

'''def buzzer_on():
    GPIO.output(buzzer_pin, GPIO.HIGH)

# Function to turn the buzzer off
def buzzer_off():
    GPIO.output(buzzer_pin, GPIO.LOW)'''

class DistanceSensorThread(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.distance = 0
        self.lock = threading.Lock()
        self._stop_event = threading.Event()
        
    def run(self):
        while not self._stop_event.is_set():
            
            
            # Send 10us pulse to trigger pin
            GPIO.output(TRIG_PIN, True)
            time.sleep(0.00001)
            GPIO.output(TRIG_PIN, False)
            
            # Measure time between sending pulse and receiving echo
            start_time = time.time()
            while GPIO.input(ECHO_PIN) == 0:
                start_time = time.time()
                if (time.time() - start_time) > 1:
                    break
            while GPIO.input(ECHO_PIN) == 1:
                end_time = time.time()
                if (time.time() - start_time) > 1:
                    break
            elapsed_time = end_time - start_time
            
            # Calculate distance from time and speed of sound (343.26 m/s)
            distance = elapsed_time * 17163.0
            
            
                
            #print(distance)
            # Update distance in thread-safe manner
            with self.lock:
                self.distance = distance
                
            # Sleep for 100ms before next measurement
            time.sleep(0.3)
a=0
def findArucoMarkers(img, markerSize=6, totalMarkers=250, draw=True):
    global ids
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key =getattr(aruco,f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict =aruco.Dictionary_get(key)
    arucoParam =aruco.DetectorParameters_create()
    
    bboxs, ids, rejected = aruco.detectMarkers(imgGray,arucoDict, parameters=arucoParam)
    #print("location",ids)
    
    
    
    if draw:
        aruco.drawDetectedMarkers(img,bboxs)

cap=cv2.VideoCapture(0)
def back():
    GPIO.output(27,False)
    GPIO.output(23,True)
    GPIO.output(24,True)
    GPIO.output(22,False)
def left():
    GPIO.output(27,True)
    GPIO.output(23,False)
    GPIO.output(24,True)
    GPIO.output(22,False)
def stop():
    GPIO.output(27,False)
    GPIO.output(23,False)
    GPIO.output(24,False)
    GPIO.output(22,False)
def forward():
    GPIO.output(27,True)
    GPIO.output(23,False)
    GPIO.output(24,False)
    GPIO.output(22,True)
def rotate():
    GPIO.output(27,False)
    GPIO.output(23,True)
    GPIO.output(24,False)
    GPIO.output(22,True)
    
def right():
    GPIO.output(27,False)
    GPIO.output(23,True)
    GPIO.output(24,False)
    GPIO.output(22,True)
def rspeed():
    speedleft.start(17)
    speedright.start(17)
def sspeed():
    speedleft.start(10.5)
    speedright.start(10.5)
    
stop()    




def caamera():
    ret, img = cap.read()
    
    findArucoMarkers(img)

    cv2.imshow("image", img)
    k = cv2.waitKey(1)
       
    print("a",ids)

class GUI:
    def __init__(self):
        self.create_window()
        self.speedabc = None
        self.speedabc =[]
        
    def create_window(self, saved_map=None):
        #self.master = master
        self.window = tk.Tk()
        
        self.window.title("Welcome!")
        #master.title("Welcome!")
        
        # create canvas
        self.canvas = tk.Canvas(self.window, width=400, height=300)
        self.canvas.pack()
        # welcome message
        self.canvas.create_text(200, 80, text="Welcome to our robot \n      service system", font=("Arial", 20))
        
        # create new map button
        self.create_button = tk.Button(self.window, text="Create New Map", command=self.create_map)
        self.create_button_window = self.canvas.create_window(200, 150, window=self.create_button)
        
        # load existing map button
        self.load_button = tk.Button(self.window, text="Load Existing Map", command=self.load_map)
        self.load_button_window = self.canvas.create_window(200, 200, window=self.load_button)
    def final(self):
        #self.window.destroy
        #self.window = tk.Tk()
        self.load_map()
    def last(self):
        self.window = tk.Tk()

        self.canvas = tk.Canvas(self.window, width=300, height=200, bg="white")
        self.canvas.pack()

        self.label = tk.Label(self.window, text="Order delivered!")
        self.label.pack()

        self.return_button = tk.Button(self.window, text="Return", command=self.window.destroy)
        self.return_button.pack()

        self.path_button = tk.Button(self.window, text="Give new path", command=self.final)
        self.path_button.pack()
        self.slow_button = tk.Button(self.window, text="Slow Speed", command=lambda: self.set_speed(1))
        self.slow_button.place(relx=1.0, rely=0.1, anchor="ne")
        self.high_button = tk.Button(self.window, text="High Speed", command=lambda: self.set_speed(2))
        self.high_button.place(relx=1.0, rely=0.2, anchor="ne")
        self.window.mainloop()
    def set_speed(self, speed):
    
        if speed == 1:
            speedabc= int(1)
            self.speedabc.append(speedabc)
            print("slow speed gui")
             # Save value 1 for slow speed
        elif speed == 2:
            speedabc= int(2)
            self.speedabc.append(speedabc)
            
            print("high speed: gui")# Save value 2 for high speed

        
    
    def create_map(self):
        # close active window
        #self.master.destroy()
        #self.window.destroy()
        if self.window:
            self.window.destroy()
        # create new window
        
        self.game = Game()
        
        self.window.mainloop()
        # save button
    def on_game_close(self):
        
            return self.game # return the Game instance
    
    def load_map(self):
        
        with open("/home/pi/Downloads/saved_map.pickle", "rb") as file:
            
            saved_map = pickle.load(file)
        #if self.window:
            #self.window.destroy()
        
        #self.master.destroy()
        self.window.destroy()
        #game = Game(window=root, saved_map=saved_map)
        #self.game = Game(saved_map=saved_map)
        self.game = Game(saved_map=saved_map)
        self.window.mainloop()
        #self.window = None
        # Destroy the welcome screen and show the game screen
        
        
        
    
        
            # update the GUI window
              # create new window
    
        
class Game:
    
            def __init__(self, saved_map=None, toplevel=None):
                self.window = tk.Tk()
                self.abc = []
                self.rabc_num = None
                self.labc_num = None
                self.fabc_num = None
                self.reabc_num = None
                self.speedabc = None
                self.seabc_num = None
                self.rabc_num = []
                self.labc_num = []
                self.fabc_num = []
                self.reabc_num = []
                self.speedabc = []
                self.seabc_num = []
                
                #self.window = tk.Tk()
                self.window.title("Game")
                
                

                # Create canvas for the game board
                self.canvas = tk.Canvas(self.window, width=500, height=500)
                self.canvas.pack()
                for i in range(10):
                    for j in range(10):
                        x1 = j * 50
                        y1 = i * 50
                        x2 = x1 + 50
                        y2 = y1 + 50
                        if (i + j) % 2 == 0:
                            self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                        else:
                            self.canvas.create_rectangle(x1, y1, x2, y2, fill="beige")
                start_button = tk.Button(self.canvas, text="Start", command=self.window.destroy)
                start_button.place(relx=1.0, rely=0, anchor="ne")
                if saved_map is not None:
                    for marker_type in saved_map:
                        if isinstance(saved_map[marker_type], dict):
                            for marker_num, marker_data in saved_map[marker_type].items():
                                x, y = marker_data["position"]
                                text = marker_data["text"]
                                tags = (marker_type, f"{marker_type}_{marker_num}")
                                self.canvas.create_text(x, y, text=text, tags=tags)
                        elif isinstance(saved_map[marker_type], list):
                            for marker_data in saved_map[marker_type]:
                                x, y = marker_data["position"]
                                text = marker_data["text"]
                                tags = (marker_type, f"{marker_type}_{marker_num}")
                                self.canvas.create_text(x, y, text=text, tags=tags)
                # Create buttons for selecting marker type
                self.aruco_button = tk.Button(self.window, text="Aruco", command=lambda: self.set_marker_type("aruco"))
                self.aruco_button.pack(side="left")
                self.table_button = tk.Button(self.window, text="Table", command=lambda: self.set_marker_type("table"))
                self.table_button.pack(side="left")

                self.direction_button = tk.Button(self.window, text="right", command=lambda: self.set_marker_type("right"))
                self.direction_button.pack(side="left")
                self.direction_button = tk.Button(self.window, text="left", command=lambda: self.set_marker_type("left"))
                self.direction_button.pack(side="left")
                self.direction_button = tk.Button(self.window, text="forward", command=lambda: self.set_marker_type("forward"))
                self.direction_button.pack(side="left")
                self.direction_button = tk.Button(self.window, text="reverse", command=lambda: self.set_marker_type("reverse"))
                self.direction_button.pack(side="left")
                self.direction_button = tk.Button(self.window, text="stop", command=lambda: self.set_marker_type("stop"))
                self.direction_button.pack(side="left")
                save_button = tk.Button(self.window, text="Save Map", command=self.save_map)
                save_button.pack(side="bottom", pady=10, padx=10, anchor="se")
                self.slow_button = tk.Button(self.window, text="Slow Speed", command=lambda: self.set_speed(1))
                self.slow_button.place(relx=1.0, rely=0.1, anchor="ne")
                self.high_button = tk.Button(self.window, text="High Speed", command=lambda: self.set_speed(2))
                self.high_button.place(relx=1.0, rely=0.2, anchor="ne")
                # Initialize marker type to None
                self.marker_type = None
                
                # Bind click event to canvas
                self.canvas.bind("<Button-1>", self.on_click)
                
                # Initialize game data
                self.game_data = {
                    "table no.": {},
                    "aruco": {},
                    "right": {},
                    "forward": {},
                    "reverse": {},
                    "left": {},
                    "stop": {}
                    }
            
            def set_speed(self, speed):
                if speed == 1:
                    speedabc= int(1)
                    self.speedabc.append(speedabc)
                    print("slow speed")
                     # Save value 1 for slow speed
                elif speed == 2:
                    speedabc= int(2)
                    self.speedabc.append(speedabc)
                    
                    print("high speed:")# Save value 2 for high speed
           
            def save_map(self):
                
               
               
             # create directory if it doesn't exist
                if not os.path.exists("/home/pi/Downloads"):
                
                   
                    os.makedirs("/home/pi/Downloads")

                # save the map using pickle
                with open("/home/pi/Downloads/saved_map.pickle", "wb") as file:
                    pickle.dump(self.game_data, file)

                print("Map saved successfully!")
            
            
            def set_marker_type(self, marker_type):
                self.marker_type = marker_type
            
                
            def on_click(self, event):
                if self.marker_type == "aruco":
                    # Create ABC marker
                    '''aruco_num = len(self.canvas.find_withtag("aruco")) + 1
                    self.canvas.create_text(event.x, event.y, text=f"aruco {aruco_num}", tags="aruco")
                    self.game_data["aruco"][aruco_num] = (event.x, event.y)'''
                    aruco_num = len(self.canvas.find_withtag("aruco")) + 1
                    text = f"aruco {aruco_num}"
                    tags = ("aruco", f"aruco_{aruco_num}")
                    self.canvas.create_text(event.x, event.y, text=text, tags=tags)
                    self.game_data["aruco"][aruco_num] = {"position": (event.x, event.y), "text": text}
                elif  self.marker_type == "table":
                    # Create ABC marker
                    '''table_num = len(self.canvas.find_withtag("table")) + 1
                    self.canvas.create_text(event.x, event.y, text=f"table\nno. {table_num}", tags="table")
                    self.game_data["table no."][table_num] = (event.x, event.y)'''
                    table_num = len(self.canvas.find_withtag("table no.")) + 1
                    text = f"table no. {table_num}"
                    tags = ("table no.", f"table_no_{table_num}")
                    self.canvas.create_text(event.x, event.y, text=text, tags=tags)
                    self.game_data["table no."][table_num] = {"position": (event.x, event.y), "text": text}
                elif self.marker_type == "right":
                    
                    # Check if Direction marker overlaps with any ABC markers
                    direction_coords = (event.x, event.y)
                    for abc_id in self.canvas.find_withtag("aruco"):
                        abc_coords = self.canvas.bbox(abc_id)
                        if direction_coords[0] >= abc_coords[0] and direction_coords[0] <= abc_coords[2] and \
                           direction_coords[1] >= abc_coords[1] and direction_coords[1] <= abc_coords[3]:
                            # Store Direction-ABC pair in game data and print it
                            abc_text = self.canvas.itemcget(abc_id, "text")
                            rabc_num = int(abc_text.split()[-1])
                            self.game_data["right"][rabc_num] = True
                            print(f"right is placed on Aruco {rabc_num}")
                        
                            self.rabc_num.append(rabc_num)
                    self.canvas.create_text(event.x, event.y, text="->", tags="right",font=("Arial", 30, "bold"), fill="red")
                elif self.marker_type == "left":
                    # Check if Direction marker overlaps with any ABC markers
                    direction_coords = (event.x, event.y)
                    for abc_id in self.canvas.find_withtag("aruco"):
                        abc_coords = self.canvas.bbox(abc_id)
                        if direction_coords[0] >= abc_coords[0] and direction_coords[0] <= abc_coords[2] and \
                           direction_coords[1] >= abc_coords[1] and direction_coords[1] <= abc_coords[3]:
                            # Store Direction-ABC pair in game data and print it
                            abc_text = self.canvas.itemcget(abc_id, "text")
                            labc_num = int(abc_text.split()[-1])
                            self.game_data["left"][labc_num] = True
                            print(f"left is placed on Aruco {labc_num}")
                            self.labc_num.append(labc_num)
                    # Create Direction marker
                    self.canvas.create_text(event.x, event.y, text="<-", tags="left" ,font=("Arial", 30, "bold"), fill="red")
                elif self.marker_type == "forward":
                    # Check if Direction marker overlaps with any ABC markers
                    direction_coords = (event.x, event.y)
                    for abc_id in self.canvas.find_withtag("aruco"):
                        abc_coords = self.canvas.bbox(abc_id)
                        if direction_coords[0] >= abc_coords[0] and direction_coords[0] <= abc_coords[2] and \
                           direction_coords[1] >= abc_coords[1] and direction_coords[1] <= abc_coords[3]:
                            # Store Direction-ABC pair in game data and print it
                            abc_text = self.canvas.itemcget(abc_id, "text")
                            fabc_num = int(abc_text.split()[-1])
                            self.game_data["forward"][fabc_num] = True
                            print(f"forward is placed on Aruco {fabc_num}")
                            self.fabc_num.append(fabc_num)
                    # Create Direction marker
                    self.canvas.create_text(event.x, event.y, text="|", tags="forward",font=("Arial", 30, "bold"), fill="green")
                elif self.marker_type == "reverse":
                    # Check if Direction marker overlaps with any ABC markers
                    direction_coords = (event.x, event.y)
                    for abc_id in self.canvas.find_withtag("aruco"):
                        abc_coords = self.canvas.bbox(abc_id)
                        if direction_coords[0] >= abc_coords[0] and direction_coords[0] <= abc_coords[2] and \
                           direction_coords[1] >= abc_coords[1] and direction_coords[1] <= abc_coords[3]:
                            # Store Direction-ABC pair in game data and print it
                            abc_text = self.canvas.itemcget(abc_id, "text")
                            reabc_num = int(abc_text.split()[-1])
                            self.game_data["reverse"][reabc_num] = True
                            print(f"reverse is placed on Aruco  {reabc_num}")
                            self.reabc_num.append(reabc_num)
                    # Create Direction marker
                    self.canvas.create_text(event.x, event.y, text="O", tags="reverse",font=("Arial", 30, "bold"), fill="blue")
                elif self.marker_type == "stop":
                    # Check if Direction marker overlaps with any ABC markers
                    direction_coords = (event.x, event.y)
                    for abc_id in self.canvas.find_withtag("aruco"):
                        abc_coords = self.canvas.bbox(abc_id)
                        if direction_coords[0] >= abc_coords[0] and direction_coords[0] <= abc_coords[2] and \
                           direction_coords[1] >= abc_coords[1] and direction_coords[1] <= abc_coords[3]:
                            # Store Direction-ABC pair in game data and print it
                            abc_text = self.canvas.itemcget(abc_id, "text")
                            seabc_num = int(abc_text.split()[-1])
                            self.game_data["stop"][seabc_num] = True
                            print(f"stop is placed on Aruco  {seabc_num}")
                            self.reabc_num.append(seabc_num)
                    # Create Direction marker
                    self.canvas.create_text(event.x, event.y, text="S", tags="stop",font=("Arial", 30, "bold"), fill="blue")




gui = GUI()

gui.window.mainloop()
game = gui.on_game_close()
'''root = tk.Tk()
gui = GUI(root)

root.mainloop()
game = Game(root)'''
def return_callback():
    # Code to execute when "return" button is clicked
    window.destroy()  # Close the GUI and return to the main loop

def direction_callback():
    # Code to execute when "give new direction" button is clicked
    gui.final()  # Call the function gui.final()


    

 

# Example usage:

def read_lir_value():
    global lir_value
    while True:
        lir_value = GPIO.input(lir_pin)
        time.sleep(0.01)

def read_rir_value():
    global rir_value
    while True:
        rir_value = GPIO.input(rir_pin)
        time.sleep(0.01)  
        
        


#t = threading.Thread(target=gamee)
#t.start()
class CameraThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()

    def run(self):
        global ids
        while not self._stop_event.is_set():
            ret, img = cap.read()
            findArucoMarkers(img)

            cv2.imshow("image", img)
            k = cv2.waitKey(1)
            
    def stop(self):
        self._stop_event.set()
        
        
GPIO.output(buzzer_pin, GPIO.LOW)


try:
    sensor_thread = DistanceSensorThread()
    sensor_thread.start()
    camera_thread = CameraThread()
    camera_thread.start()
    obstacle_detected_time = None
    ir_thread = threading.Thread(target=read_lir_value)
    ir_thread.daemon = True
    ir_thread.start()
    rir_thread = threading.Thread(target=read_rir_value)
    rir_thread.daemon = True
    rir_thread.start()
    
    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stop()
                    # Spacebar key is pressed
                    # Add code to stop the car's movement here
                    # Perform any necessary actions to stop the car
                    
                    # Exit the while loop to stop the program
                    pygame.quit()
                    sys.exit()
        
        
        
        with sensor_thread.lock:
            distance = sensor_thread.distance
        if lir_value == 0:
            print("")
        
        else:
            print("blackdetect")
            if game is not None and hasattr(game, 'speedabc') and 2 in game.speedabc:
                
                speedleft.start(50)
                speedright.start(50)
            elif game is not None and hasattr(game, 'speedabc') and 1 in game.speedabc:
                speedleft.start(40)
                speedright.start(40)
            else:
                speedleft.start(40)
                speedright.start(40)
           
            left()
            
            time.sleep(0.007)
            stop()
            sspeed()
            
        if rir_value == 0:
            print("")
        
        else:
            print("blackdetect")
            if game is not None and hasattr(game, 'speedabc') and 2 in game.speedabc:
                
                speedleft.start(50)
                speedright.start(50)
            elif game is not None and hasattr(game, 'speedabc') and 1 in game.speedabc:
                speedleft.start(40)
                speedright.start(40)
            else:
                speedleft.start(40)
                speedright.start(40)
            
            right()
            time.sleep(0.007)
            stop()
            sspeed()
            
            
        #print("Distance: %.2f cm" % distance)
        if game is not None and hasattr(game, 'speedabc') and 2 in game.speedabc:
            rspeed()
            forward() 
        elif game is not None and hasattr(game, 'speedabc') and 1 in game.speedabc:
            sspeed()
            forward()
        else:
            sspeed()
            forward()
        #buzzer_off()
        
        if distance < 40:
            
            # Stop robot
            stop()
            time.sleep(2)
            #buzzer_on()
            GPIO.output(buzzer_pin, GPIO.HIGH)
            
            
            

            # If obstacle has just been detected, record the time
            if obstacle_detected_time is None:
                obstacle_detected_time = time.time()

            # If obstacle is still present after 10 seconds, reverse
            if (time.time() - obstacle_detected_time) > 10:
                GPIO.output(buzzer_pin, GPIO.LOW)
                #buzzer_off()
                if rir_value == 0:
                     stop()
                     time.sleep(0.3)
                     rspeed()
                     rotate()
                     time.sleep(0.2)
                     #stop()
                     
                     while rir_value == 0 :
                         
                         speedleft.start(35)
                         speedright.start(35)
                         # Replace with the actual code to read right IR sensor
                         time.sleep(0.005)
                     time.sleep(0.1)
                     stop()
                     sspeed()
                     gui.last()
                
                
                
                
                
            else:
                
                #buzzer_off()
                # Otherwise, do nothing and wait for obstacle to move out
                pass
        else:
            GPIO.output(buzzer_pin, GPIO.LOW)
            # If obstacle is not present, move forward
            forward()
            obstacle_detected_time = None
            
        #print(ids)       
        if ids is not None:
            
            #if game.rabc_num:
                # check if rabc_num is not empty
            # do your main task here with the rabc_num data
            for item in ids:
                
                if game is not None and hasattr(game, 'rabc_num') and item in game.rabc_num:
                    
                    
                    if lir_value == 0:
                        print("")
                        print(item ,"set right")
                        if game is not None and hasattr(game, 'speedabc') and 2 in game.speedabc:
                            speedleft.start(40)
                            speedright.start(40)
                        elif game is not None and hasattr(game, 'speedabc') and 1 in game.speedabc:
                            speedleft.start(30)
                            speedright.start(30)
                        else:
                            speedleft.start(30)
                            speedright.start(30)
                        
                        right()
                        
                        while lir_value == 0:
                            
                            right()
                            
                            if game is not None and hasattr(game, 'speedabc') and 2 in game.speedabc:
                                speedleft.start(50)
                                speedright.start(50)
                            elif game is not None and hasattr(game, 'speedabc') and 1 in game.speedabc:
                                speedleft.start(30)
                                speedright.start(30)
                            else:
                                speedleft.start(30)
                                speedright.start(30)# Replace with the actual code to read left IR sensor
                            time.sleep(0.009)
                        
                        
                    
                    else:
                        print("blackdetect")
                        speedleft.start(40)
                        speedright.start(40)
                        
                        left
                        
                        time.sleep(0.009)
                        stop()
                        sspeed()
                    
                    
                
                    #sspeed()
                    forward()
                    
                    
                    
                    
                    
                if game is not None and hasattr(game, 'labc_num') and item in game.labc_num:
                    
                    if rir_value == 0 :
                        
                        print("")
                        print(item ,"set left")
                        if game is not None and hasattr(game, 'speedabc') and 2 in game.speedabc:
                            
                            speedleft.start(50)
                            speedright.start(50)
                        elif game is not None and hasattr(game, 'speedabc') and 1 in game.speedabc:
                            speedleft.start(30)
                            speedright.start(30)
                        else:
                            speedleft.start(30)
                            speedright.start(30)
                        left()
                        time.sleep(0.2)
                        while rir_value ==0  :
                            left()
                            if game is not None and hasattr(game, 'speedabc') and 2 in game.speedabc:
                                speedleft.start(55)
                                speedright.start(55)
                            elif game is not None and hasattr(game, 'speedabc') and 1 in game.speedabc:
                                speedleft.start(30)
                                speedright.start(30)
                            else:
                                speedleft.start(30)
                                speedright.start(30)
                            # Replace with the actual code to read left IR sensor
                            time.sleep(0.009)
                        
                        
                    
                    else:
                        
                        print("blackdetect")
                        speedleft.start(35)
                        speedright.start(35)
                        
                        right
                        
                        time.sleep(0.009)
                        stop()
                        sspeed()
                    
                    
                
                    #sspeed()
                    forward()
                if game is not None and hasattr(game, 'fabc_num') and item in game.fabc_num:
                     sspeed()
                     forward()
                     print(item,"set lforward")
                     
                if game is not None and hasattr(game, 'reabc_num') and item in game.reabc_num:
                    if rir_value == 0:
                         stop()
                         time.sleep(0.3)
                         if game is not None and hasattr(game, 'speedabc') and 2 in game.speedabc:
                            
                             speedleft.start(50)
                             speedright.start(50)
                         elif game is not None and hasattr(game, 'speedabc') and 1 in game.speedabc:
                             speedleft.start(30)
                             speedright.start(30)
                         else:
                             speedleft.start(30)
                             speedright.start(30)
                         rotate()
                         time.sleep(0.3)
                         #stop()
                         print(item,"set reverse")
                         while rir_value == 0 :
                             
                             
                             if game is not None and hasattr(game, 'speedabc') and 2 in game.speedabc:
                                 
                                 speedleft.start(55)
                                 speedright.start(55)
                             elif game is not None and hasattr(game, 'speedabc') and 1 in game.speedabc:
                                 speedleft.start(33)
                                 speedright.start(33)
                             else:
                                 speedleft.start(33)
                                 speedright.start(33)
                             # Replace with the actual code to read right IR sensor
                             time.sleep(0.005)
                         time.sleep(0.1)
                         stop()
                         sspeed()
                         gui.last() 
                    else:
                        '''print("blackdetect")
                        speedleft.start(40)
                        speedright.start(40)
                        
                        right()
                         
                        time.sleep(0.1)'''
                        
                       
                      
                if game is not None and hasattr(game, 'seabc_num') and item in game.seabc_num:
                     forward()
                     time.sleep(0.2)
                     stop()
                     print(item,"order complete")
                     gui.last()
                     
                     #gui.window.mainloop()
except KeyboardInterrupt:
    GPIO.cleanup() 
        
            
finally:
    GPIO.cleanup() 