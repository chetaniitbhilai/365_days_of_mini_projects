import asyncio
import websockets
from pynput.mouse import Controller, Button
import json
from enum import Enum

class TouchGesture(Enum):
    SINGLE_TAP = "single_tap"
    DOUBLE_TAP = "double_tap"
    RIGHT_TAP = "right_tap"
    DRAG_START = "drag_start"
    DRAG_MOVE = "drag_move"
    DRAG_END = "drag_end"
    SCROLL = "scroll"
    MOVE = "move"

class TouchController:
    def _init_(self):
        self.mouse = Controller()
        self.is_dragging = False
        self.movement_scale = 2.0

    def process_touch_data(self, message):
        try:
            touch_data = json.loads(message)
            print(f"Received data: {touch_data}")

            gesture_type = touch_data.get("type", "")

            if gesture_type == TouchGesture.SINGLE_TAP.value:
                self.handle_single_tap()
            elif gesture_type == TouchGesture.DOUBLE_TAP.value:
                self.handle_double_tap()
            elif gesture_type == TouchGesture.RIGHT_TAP.value:
                self.handle_right_tap()
            elif gesture_type == TouchGesture.DRAG_START.value:
                self.handle_drag_start()
            elif gesture_type == TouchGesture.DRAG_END.value:
                self.handle_drag_end()
            elif gesture_type == TouchGesture.SCROLL.value:
                self.handle_scroll(touch_data)
            elif "dx" in touch_data and "dy" in touch_data:
                if self.is_dragging:
                    self.handle_drag_move(touch_data)
                else:
                    self.handle_move(touch_data)
            else:
                print(f"Unrecognized data: {touch_data}")

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"Error processing data: {e}")

    def handle_single_tap(self):
        self.mouse.click(Button.left)
        print("Processed left click")

    def handle_double_tap(self):
        self.mouse.click(Button.left, 2)
        print("Processed double click")

    def handle_right_tap(self):
        self.mouse.click(Button.right)
        print("Processed right click")

    def handle_drag_start(self):
        self.is_dragging = True
        self.mouse.press(Button.left)
        print("Started dragging")

    def handle_drag_move(self, touch_data):
        if self.is_dragging:
            dx = touch_data["dx"] * self.movement_scale
            dy = touch_data["dy"] * self.movement_scale
            self.mouse.move(dx, dy)
            print(f"Dragging: dx={dx}, dy={dy}")

    def handle_drag_end(self):
        if self.is_dragging:
            self.is_dragging = False
            self.mouse.release(Button.left)
            print("Ended dragging")

    def handle_scroll(self, touch_data):
        dx = touch_data.get("scroll_dx", 0)
        dy = touch_data.get("scroll_dy", 0)
        self.mouse.scroll(dx, dy)
        print(f"Scrolled: dx={dx}, dy={dy}")

    def handle_move(self, touch_data):
        dx = touch_data["dx"] * self.movement_scale
        dy = touch_data["dy"] * self.movement_scale
        self.mouse.move(dx, dy)
        print(f"Moved: dx={dx}, dy={dy}")

# WebSocket server configuration
host = '0.0.0.0'  # Listen on all interfaces
port = 5000       # Port to receive data
controller = TouchController()

async def handle_connection(websocket, path):
    print("Client connected.")
    try:
        async for message in websocket:
            controller.process_touch_data(message)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected.")
    except Exception as e:
        print(f"Connection error: {e}")

# Start the WebSocket server
def main():
    start_server = websockets.serve(handle_connection, host, port)
    print(f"WebSocket server listening on ws://{host}:{port}")
    
    try:
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("\nServer shutdown requested")
    except Exception as e:
        print(f"Server error: {e}")

if _name_ == "_main_":
    main()