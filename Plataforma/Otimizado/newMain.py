"""
Programmers: Mateus Souza and Werikson Alves
Start Date: 01/05/2022 - End Date: 31/01/2023
Last Revision Date: ??/08/2023
"""

import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import ttk, StringVar
import threading

# The class AppBDP is a placeholder for a Python application.
class AppBDP:
    def __init__(self):
        """
        The above function initializes various variables and sets up the main window and buttons for a
        computer vision application.
        """
        self.median_blur = 3
        self.fps = 15
        self.camera_mode = 0

        self._camera_on = False
        self._preview_on = False
        self._preview_thread = None
        self._calibration_successful = False

        self.current_folder = os.path.dirname(__file__)
        self.field_mm_image = cv2.imread(os.path.join(self.current_folder, 'Field_mm.png'))
        self.field_px_image = cv2.imread(os.path.join(self.current_folder, 'Field_px.png'))

        self.var_ptm = np.ones((3, 3))
        self.var_kernel = np.ones((3, 3), np.uint8)
        self.var_matrix_color = np.array([
            [0, 255, 0, 255, 0, 255],
            [0, 255, 0, 255, 0, 255],
            [0, 255, 0, 255, 0, 255],
            [0, 255, 0, 255, 0, 255],
            [0, 255, 0, 255, 0, 255],
            [0, 255, 0, 255, 0, 255],
            [0, 255, 0, 255, 0, 255],
        ], dtype=np.uint8)
        self._target = np.ones((3, 1))
        self._validation_points = np.ones((3, 1))

        self.create_window()
        self.create_buttons()
        self.window_main.protocol("WM_DELETE_WINDOW", self.on_window_close)

    def create_window(self):
        """
        The function creates a window with a title, size, background color, and a status bar at the
        bottom.
        """
        self.window_main = tk.Tk()
        self.window_main.title("BDP 2023")
        self.window_main.minsize(600, 400)
        self.window_main.maxsize(600, 400)
        self.window_main.configure(bg="#229A00")

        self.main_status_bar = tk.Label(
            self.window_main,
            text="Instructions:\n \
                    Default: Connect a camera (F) ==> Load the latest calibration (F) ==> Enable startup (F).\n \
                    Calibration: Connect a camera (F) ==> Calibrate the field (F) ==> Calibrate the colors (F) ==> Enable startup (F).\n \
                    Test: Choose a test routine to run",
            bd=1,
            relief=tk.SUNKEN,
            anchor="center",
        )
        self.main_status_bar.pack(side="bottom", fill="x")

    def clear_status_bar(self):
        """
        The function clears the text of the main status bar and updates it.
        """
        self.main_status_bar.config(text="")
        self.main_status_bar.update_idletasks()

    def set_status_bar(self, text):
        """
        The function sets the text of the main status bar and updates it.
        
        :param text: The text parameter is a string that represents the text that you want to display in
        the status bar
        """
        self.main_status_bar.config(text=text)
        self.main_status_bar.update_idletasks()

    def create_buttons(self):
        """
        The function creates buttons and places them in a tkinter window for a camera application.
        """
        self.camera_list = self.get_available_cameras()
        self.selected_camera = StringVar(value=self.camera_list[0])
        self.chosen_camera = ttk.Combobox(
            self.window_main, state='readonly', textvariable=self.selected_camera, values=self.camera_list, justify='center'
        )
        self.chosen_camera.place(height=20, width=150, x=10, y=10)
        self.selected_camera.trace('w', self.on_camera_index_change)

        self.__connect_button = tk.Button(self.window_main, text="Connect", command=self.connect_camera)
        self.__connect_button.place(height=50, width=150, x=10, y=70)

        self.__disconnect_button = tk.Button(self.window_main, text="Disconnect", command=self.disconnect_camera, state='disabled')
        self.__disconnect_button.place(height=50, width=150, x=10, y=130)

        self.__open_preview_button = tk.Button(self.window_main, text="Open Preview", command=self.toggle_preview, state='disabled')
        self.__open_preview_button.place(height=50, width=150, x=10, y=190)

        # Section 2: Field
        self.__capture_image_button = tk.Button(self.window_main, text="Capture Image", command=self.capture_image, state='disabled')
        self.__capture_image_button.place(height=50, width=150, x=180, y=10)

        self.__correlate_points_button = tk.Button(self.window_main, text="Correlate Points", command=self.correlate_points, state='disabled')
        self.__correlate_points_button.place(height=50, width=150, x=180, y=70)

        self.__validate_points_button = tk.Button(self.window_main, text="Validate Points", command=self.validate_points, state='disabled')
        self.__validate_points_button.place(height=50, width=150, x=180, y=130)

        self.__save_calibration_button = tk.Button(self.window_main, text="Save Calibration", command=self.save_calibration, state='disabled')
        self.__save_calibration_button.place(height=50, width=150, x=180, y=190)

        # Section 3: Configuration and game
        self.__colors_button = tk.Button(self.window_main, text="Calibrate Colors", command=self.open_colors_window, state='disabled')
        self.__colors_button.place(height=50, width=150, x=350, y=10)

        self.__load_settings_button = tk.Button(self.window_main, text="Load Calibration", command=self.load_settings)
        self.__load_settings_button.place(height=50, width=150, x=350, y=70)

        self.__game_button = tk.Button(self.window_main, text="Enable Game", command=self.open_game_window, state='disabled')
        self.__game_button.place(height=50, width=150, x=350, y=130)

        # Section 4: Ending
        close_button = tk.Button(self.window_main, text="Exit", bg="grey", activebackground="red", command=self.exit_program)
        close_button.place(height=50, width=150, x=350, y=190)

    # Section 1: Camera
    def get_available_cameras(self):
        """
        The function `get_available_cameras` returns a list of available cameras by checking if each
        camera index is opened and releasing it after reading a frame.
        :return: a list of available cameras.
        """
        cameras = []
        for i in range(10):
            cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
            if cap.isOpened():
                _, _ = cap.read()
                camera_name = f"{i}: Camera {i}"
                cameras.append(camera_name)
                cap.release()
        return cameras

    def on_camera_index_change(self, *args):
        """
        The function updates the camera mode and releases the camera information if the camera is
        currently on.
        """
        self.camera_mode = int(self.camera_list[self.chosen_camera.current()][0])
        if self._camera_on:
            self.camera_information.release()
            self._camera_on = False

    def connect_camera(self):
        """
        The function `connect_camera` connects to a camera and displays a status message indicating
        whether the connection was successful or not.
        """
        if not self._camera_on:
            self.clear_status_bar()
            self.set_status_bar("Connecting to the camera")
            try:
                self.camera_information = cv2.VideoCapture(self.camera_mode, cv2.CAP_DSHOW)
                self._camera_on, _ = self.camera_information.read()
                self.__disconnect_button.configure(state='active')
                self.__connect_button.configure(state='disabled')
                self.__open_preview_button.configure(state='active')
                self.__capture_image_button.configure(state='active')
                self.__correlate_points_button.configure(state='active')
                self.__validate_points_button.configure(state='active')
                self.__save_calibration_button.configure(state='active')
                self.__colors_button.configure(state='active')
                
                self.clear_status_bar()
                self.set_status_bar("Camera connected successfully. Check the preview.")
            except cv2.error as e:
                self.clear_status_bar()
                self.set_status_bar(f"Failed to connect to the camera\nError: {str(e)}")
            except Exception as e:
                self.clear_status_bar()
                self.set_status_bar(f"Another error occurred\nError: {str(e)}")
        else:
            self.clear_status_bar()
            self.set_status_bar("The camera is already connected. Check the preview.")

    def disconnect_camera(self):
        """
        The function disconnects the camera if it is currently connected, and displays appropriate
        status messages.
        """
        if self._camera_on:
            self.clear_status_bar()
            self.set_status_bar("Disconnecting the camera")
            self.__connect_button.configure(state='active')
            self.__disconnect_button.configure(state='disabled')
            self.__open_preview_button.configure(state='disabled')
            self.__capture_image_button.configure(state='disabled')
            self.__correlate_points_button.configure(state='disabled')
            self.__validate_points_button.configure(state='disabled')
            self.__save_calibration_button.configure(state='disabled')
            self.__colors_button.configure(state='disabled')
                
            try:
                self.camera_information.release()
                self._camera_on = False
                self.clear_status_bar()
                self.set_status_bar("Camera disconnected successfully")
            except cv2.error as e:
                self.clear_status_bar()
                self.set_status_bar(f"Failed to disconnect the camera\nError: {str(e)}")
            except Exception as e:
                self.clear_status_bar()
                self.set_status_bar(f"Another error occurred\nError: {str(e)}")
        else:
            self.clear_status_bar()
            self.set_status_bar("The camera is already disconnected")

    def show_preview(self):
        """
        The function `show_preview` displays a live preview of frames from a camera, applying a median
        blur filter, and handles errors that may occur.
        """
        try:
            self.clear_status_bar()
            self.set_status_bar("Viewing in the Preview window.")

            while True:
                _, self.frames = self.camera_information.read()
                self.frames = cv2.medianBlur(self.frames, self.median_blur)
                cv2.imshow("Preview", self.frames)
                cv2.waitKey(self.fps)

                self._preview_on = True

                if cv2.getWindowProperty("Preview", cv2.WND_PROP_VISIBLE) < 1:
                    self.clear_status_bar()
                    self.set_status_bar("Vision system connected\nGo to color calibration")
                    self._preview_on = False
                    break
        except cv2.error as e:
            self.clear_status_bar()
            self.set_status_bar(f"Error opening the preview\nError: {str(e)}")
        except Exception as e:
            self.clear_status_bar()
            self.set_status_bar(f"Another error occurred\nError: {str(e)}")

    def toggle_preview(self):
        """
        The function toggles the preview on and off.
        """
        if self._preview_on:
            self.close_preview()
        else:
            self.open_preview()

    def open_preview(self):
        """
        The function `open_preview` starts a new thread to show a preview if the camera is on and the
        preview is not already on.
        """
        if self._camera_on and not self._preview_on:
            self._preview_thread = threading.Thread(target=self.show_preview)
            self._preview_thread.start()

    def close_preview(self):
        """
        The function `close_preview` is used to close the preview window if it is currently open.
        """
        if self._preview_on:
            self._preview_on = False
            self._preview_thread.join()
            cv2.destroyAllWindows()

    def on_window_close(self):
        """
        The function `on_window_close` is used to close a preview window.
        """
        self.close_preview()

    # Section 3: Field
    def capture_image(self):
        """
        The function captures an image using a camera and displays a status message indicating success
        or failure.
        """
        self.clear_status_bar()
        self.set_status_bar("Capturing field image")
        try:
            _, self.frames = self.camera_information.read()
            self.clear_status_bar()
            self.set_status_bar("Image captured")
        except Exception as e:
            self.clear_status_bar()
            self.set_status_bar(f"Error capturing image: {str(e)}")

    def correlate_points(self):
        """
        The function `correlate_points` performs point correlation between two sets of points and
        calculates a perspective transformation matrix.
        """
        self.clear_status_bar()
        self.set_status_bar("Correlating points")

        wf, wa, hf, ha = 750, 600, 650, 350
        real_points = np.array([[-wf, 0, wf, wf, 0, -wf, -wa, wa, wa, -wa],
                                [-hf, -hf, -hf, hf, hf, hf, -ha, -ha, ha, ha],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

        if np.size(self._target, 1) > 1:
            self._target = self._target[:, :1]

        try:
            while True:
                frame = cv2.resize(self.frames, (640, 480))
                field_image = cv2.resize(self.field_mm_image, (640, 480))
                concatenated_images = np.concatenate((field_image, frame), axis=1)

                self.clear_status_bar()
                self.set_status_bar(f"Correlating point {np.size(self._target, 1)}.")

                if np.size(self._target, 1) == 11:
                    self.transformation_matrix = real_points @ np.linalg.pinv(self._target[:, 1:])
                    break

                cv2.imshow('Capture points', concatenated_images)
                cv2.setMouseCallback('Capture points', self.correlate_points_mouse)
                cv2.waitKey(self.fps)

                if cv2.getWindowProperty('Capture points', cv2.WND_PROP_VISIBLE) < 1:
                    break
        except Exception as e:
            self.clear_status_bar()
            self.set_status_bar(f"Error correlating points: {str(e)}")

        self.clear_status_bar()
        self.set_status_bar("Perspective transformation matrix obtained.")
        cv2.destroyAllWindows()

    def correlate_points_mouse(self, event, x, y, flags, param):
        """
        The function `correlate_points_mouse` is used to add or remove points from a target array based
        on left and right mouse button clicks.
        
        :param event: The "event" parameter represents the type of mouse event that occurred. It can
        have different values depending on the event, such as cv2.EVENT_LBUTTONDOWN for left button down
        event and cv2.EVENT_RBUTTONDOWN for right button down event
        :param x: The x-coordinate of the mouse click event
        :param y: The parameter "y" represents the y-coordinate of the mouse event. It indicates the
        vertical position of the mouse cursor when the event occurred
        :param flags: The "flags" parameter in the "correlate_points_mouse" function is not used in the
        provided code snippet. It is included as a parameter in the function definition but is not
        referenced or used within the function body
        :param param: The `param` parameter is not used in the given code snippet. It is typically used
        to pass additional parameters or data to the callback function. In this case, it is not being
        used
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            point = np.array([[x - 640], [y], [1]])
            self._target = np.concatenate((self._target, point), 1)
        elif event == cv2.EVENT_RBUTTONDOWN:
            if np.size(self._target, 1) > 1:
                self._target = self._target[:, 0:-1]

    def validate_points(self):
        """
        The function `validate_points` is used to validate the calibration of points by displaying
        images and allowing the user to interact with them using the mouse.
        """
        self.clear_status_bar()
        self.set_status_bar("Validating calibration")

        img_frame = cv2.resize(self.frames, [640, 480])
        preview_image = cv2.resize(self.field_px_image, [640, 480])
        concatenated_images = np.concatenate((preview_image, img_frame), axis=1)

        while True:
            cv2.imshow('Validation of Points', concatenated_images)
            cv2.setMouseCallback('Validation of Points', self.validate_points_mouse)
            cv2.waitKey(self.fps)

            if cv2.getWindowProperty('Validation of Points', cv2.WND_PROP_VISIBLE) < 1:
                break

        if self._calibration_successful:
            self.clear_status_bar()
            self.set_status_bar("Calibration validated")

    def validate_points_mouse(self, event, x, y, flags, param):
        """
        The function validates points clicked by the user on an image and applies a transformation
        matrix to draw a circle on the image.
        
        :param event: The "event" parameter represents the type of mouse event that occurred. In this
        case, it is checking if the left button of the mouse was clicked
        :param x: The parameter `x` represents the x-coordinate of the mouse click event
        :param y: The parameter `y` represents the y-coordinate of the mouse click event
        :param flags: The `flags` parameter in the `validate_points_mouse` function is not used in the
        provided code snippet. It is a parameter that can be used to specify any special flags for the
        mouse event. In OpenCV, the `flags` parameter is typically used in conjunction with the `event`
        parameter
        :param param: The `param` parameter is not used in the given code snippet. It is included in the
        function signature to match the required callback function signature for the OpenCV
        `setMouseCallback` function. The `param` parameter can be used to pass additional user-defined
        data to the callback function if needed
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            self._validation_points[0, 0] = x - 640
            self._validation_points[1, 0] = y

            try:
                applied_points = self.transformation_matrix @ self._validation_points + np.array([[900], [750], [0]])
                self.field_px_image = self.field_px_image.copy()
                cv2.circle(self.field_px_image, (int(applied_points[0, 0]), int(applied_points[1, 0])), 15, (255, 0, 0), 10)

                img_field = cv2.resize(self.field_px_image, (640, 480))
                concatenated_images = np.concatenate((img_field, self.frames), axis=1)

                self._calibration_successful = True
            except:
                self.clear_status_bar()
                self.set_status_bar('Load or perform a calibration.')

    def save_calibration(self):
        """
        The function saves a calibration by writing a transformation matrix to a text file.
        """
        self.clear_status_bar()
        self.set_status_bar("Saving calibration")

        try:
            np.savetxt(os.path.join(self.current_folder, 'Transformation_Matrix.txt'), self.transformation_matrix, newline='\n')
            self.clear_status_bar()
            self.set_status_bar("Calibration saved")
        except Exception as e:
            self.clear_status_bar()
            self.set_status_bar(f"Error saving calibration: {str(e)}")

    # Section 4: Configuration and game
    def load_settings(self):
        """
        The function loads settings from specific files and displays a status message indicating whether
        the files were found or not.
        """
        try:
            self.var_matrix_color = np.loadtxt(
                os.path.join(self.current_folder, "Cores", "MatrixHSV.txt")
            )
            self.var_ptm = np.loadtxt(
                os.path.join(self.current_folder, "Campo", "TransformationMatrix.txt")
            )
            self.clear_status_bar()
            self.set_status_bar("Calibration loaded.")
            self.__game_button.config(state='active')
        except:
            self.clear_status_bar()
            self.set_status_bar("File not found. Perform a new calibration.")

    def open_camera_window(self):
        """
        The function opens a camera window and starts the camera.
        """
        self.camera_window = CameraWindow(
            self.var_camera_on, self.var_median_blur, self.var_fps
        )
        self.clear_status_bar()
        self.set_status_bar(
            "Instructions:\nInitialize the camera: In progress\nCalibrate colors: Pending\nCalibrate field: Pending\nStart the game: Pending"
        )
        self.camera_window.start()

    def open_colors_window(self):
        """
        The function opens a colors window and sets the status bar accordingly.
        """
        try:
            self.var_camera_on = self.camera_window.var_camera_on
            self.var_cam_info = self.camera_window.var_camera_information

            self.colors_window = ColorsWindow(
                self.var_kernel,
                self.var_median_blur,
                self.var_matrix_color,
                self.var_cam_info,
                self.var_fps,
            )

            self.clear_status_bar()
            self.set_status_bar(
                "Instructions:\nInitialize the camera: Done\nCalibrate colors: In progress\nCalibrate field: Pending\nStart the game: Pending"
            )

            self.colors_window.start_command()
        except:
            self.clear_status_bar()
            self.set_status_bar(
                "Instructions:\nInitialize the camera: Connect a camera first\nCalibrate colors: Pending\nCalibrate field: Pending\nStart the game: Pending"
            )

    def open_field_window(self):
        """
        The function opens a field window and sets the status bar accordingly.
        """
        try:
            self.var_camera_on = self.camera_window.var_camera_on
            self.var_cam_info = self.camera_window.var_camera_information

            self.field_window = FieldWindow(self.var_cam_info, self.var_fps)

            self.clear_status_bar()
            self.set_status_bar(
                "Instructions:\nInitialize the camera: Done\nCalibrate colors: Done\nCalibrate field: In progress\nStart the game: Pending"
            )

            self.field_window.start_command()
        except:
            self.clear_status_bar()
            self.set_status_bar(
                "Instructions:\nInitialize the camera: Connect a camera first\nCalibrate colors: Pending\nCalibrate field: Pending\nStart the game: Pending"
            )

    def open_game_window(self):
        """
        The function opens a game window and starts the game with the given camera information and
        calibration settings.
        """
        try:
            self.var_camera_on = self.camera_window.var_camera_on
            self.var_cam_info = self.camera_window.var_camera_information

            self.game_window = PDIGameWindow(
                self.var_matrix_color,
                self.var_cam_info,
                self.var_fps,
                self.var_kernel,
                self.var_median_blur,
                self.var_ptm,
            )

            self.clear_status_bar()
            self.set_status_bar(
                "Instructions:\nInitialize the camera: Done\nCalibrate colors: Done\nCalibrate field: Done\nStart the game: In progress"
            )

            self.game_window.start_command()
        except:
            self.clear_status_bar()
            self.set_status_bar(
                "Instructions:\nMake or load the Camera, Colors, and/or Field calibrations"
            )

    # Section 5: main
    def exit_program(self):
        """
        The function `exit_program` is used to release the camera, close any open windows, and quit the
        main window of a program.
        """
        try:
            if self._camera_on:
                self.camera_information.release()
            cv2.destroyAllWindows()
            self.window_main.quit()
        except Exception as e:
            print(f"Error stopping the window\nError: {str(e)}")

    def run_command(self):
        """
        The function runs the main loop of the tkinter window.
        """
        self.window_main.mainloop()


'''.............................................................................................................'''
def main(args):
    app = AppBDP()
    app.run_command()

if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))
