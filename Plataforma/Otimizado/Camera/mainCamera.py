
'''
:::::::::::::::::::::::::::::::::::::::::::::::::::
Programmers: Mateus Souza and Werikson Alves
:::::::::::::::::::::::::::::::::::::::::::::::::::

Scrip for camera-related functions.
'''

import tkinter as tk
import tkinter.ttk as ttk
import cv2
import threading

class CameraConfigWindow:
    def __init__(self, camera_on, median_blur, fps):
        self.camera_on = camera_on
        self.median_blur = median_blur
        self.fps = fps
        self.preview_on = False
        self.preview_thread = None

        self.create_window()
        self.create_menu()
        self.window.protocol("WM_DELETE_WINDOW", self.on_window_close)

    def create_window(self):
        self.window = tk.Toplevel()
        self.window.title("Camera Configuration")
        self.window.geometry("300x500")
        self.window.configure(bg="#229A00")

        fps_label = tk.Label(self.window, text="FPS:")
        fps_label.place(x=50, y=60)

        median_blur_label = tk.Label(self.window, text="MedianBlur:")
        median_blur_label.place(x=130, y=60)

        self.status_bar = tk.Label(self.window, text="Instructions:\nSelect camera\nConnect camera\nView preview",
                                   bd=1, relief=tk.SUNKEN, anchor=tk.CENTER)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def clear_status_bar(self):
        try:
            self.status_bar.config(text="")
            self.status_bar.update_idletasks()
        except tk.TclError:
            pass

    def set_status_bar(self, text):
        try:
            self.status_bar.config(text=text)
            self.status_bar.update_idletasks()
        except tk.TclError:
            pass

    def create_menu(self):
        available_cameras = self.get_available_cameras()
        selected_camera = tk.StringVar(value=available_cameras[0])
        self.__chosen_camera = ttk.Combobox(self.window, state='readonly', textvariable=selected_camera,
                                     values=available_cameras, justify='center')
        self.__chosen_camera.place(height=20, width=200, x=50, y=10)
        selected_camera.trace('w', self.on_selected_camera_change)

        fps_var = tk.StringVar(value=str(self.fps))
        self.fps_entry = tk.Entry(self.window, textvariable=fps_var)
        self.fps_entry.place(height=20, width=40, x=80, y=60)

        median_blur_var = tk.StringVar(value=str(self.median_blur))
        self.median_blur_entry = tk.Entry(self.window, textvariable=median_blur_var)
        self.median_blur_entry.place(height=20, width=40, x=210, y=60)

        connect_button = tk.Button(self.window, text="Connect", command=self.connect_camera)
        connect_button.place(height=50, width=200, x=50, y=100)

        disconnect_button = tk.Button(self.window, text="Disconnect", command=self.disconnect_camera)
        disconnect_button.place(height=50, width=200, x=50, y=160)

        preview_button = tk.Button(self.window, text="Open Preview", command=self.toggle_preview)
        preview_button.place(height=50, width=200, x=50, y=220)

    def get_available_cameras(self):
        cameras = []
        for i in range(10):  # Check up to 10 possible cameras (adjust as needed)
            cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
            if cap.isOpened():
                _, _ = cap.read()
                camera_name = f"{i}: Camera {i}"
                cameras.append(camera_name)
                cap.release()
        return cameras

    def on_selected_camera_change(self, *args):
        self.selected_camera_index = int(self.chosen_camera.current())
        if self.camera_on:
            self.camera.release()
            self.camera_on = False

    def connect_camera(self):
        self.fps = int(self.fps_entry.get())
        self.median_blur = int(self.median_blur_entry.get())

        if not self.camera_on:
            self.clear_status_bar()
            self.set_status_bar("Connecting to the camera")
            try:
                self.camera = cv2.VideoCapture(self.selected_camera_index, cv2.CAP_DSHOW)
                self.camera_on, _ = self.camera.read()
                self.clear_status_bar()
                self.set_status_bar("Camera connected successfully. Check the Preview.")
            except cv2.error as e:
                self.clear_status_bar()
                self.set_status_bar(f"Failed to connect to the camera\nError: {str(e)}")
            except Exception as e:
                self.clear_status_bar()
                self.set_status_bar(f"An error occurred\nError: {str(e)}")
        else:
            self.clear_status_bar()
            self.set_status_bar("The camera is already connected. Check the Preview.")

    def disconnect_camera(self):
        if self.camera_on:
            self.clear_status_bar()
            self.set_status_bar("Disconnecting the camera")
            try:
                self.camera.release()
                self.camera_on = False
                self.clear_status_bar()
                self.set_status_bar("Camera disconnected successfully")
            except cv2.error as e:
                self.clear_status_bar()
                self.set_status_bar(f"Failed to disconnect the camera\nError: {str(e)}")
            except Exception as e:
                self.clear_status_bar()
                self.set_status_bar(f"An error occurred\nError: {str(e)}")
        else:
            self.clear_status_bar()
            self.set_status_bar("The camera is already disconnected")

    def open_preview(self):
        try:
            self.clear_status_bar()
            self.set_status_bar("Viewing in Preview window")

            while True:
                _, self.frames = self.camera.read()
                self.frames = cv2.medianBlur(self.frames, self.median_blur)
                cv2.imshow("Preview", self.frames)
                cv2.waitKey(self.fps)

                self.preview_on = True

                if cv2.getWindowProperty("Preview", cv2.WND_PROP_VISIBLE) < 1:
                    self.clear_status_bar()
                    self.set_status_bar("Vision system connected\nGo to color calibration")
                    self.preview_on = False
                    break
        except cv2.error as e:
            self.clear_status_bar()
            self.set_status_bar(f"Error opening preview\nError: {str(e)}")
        except Exception as e:
            self.clear_status_bar()
            self.set_status_bar(f"Another error occurred\nError: {str(e)}")

    def toggle_preview(self):
        if self.preview_on:
            self.close_preview()
        else:
            self.open_preview()

    def close_preview(self):
        if self.preview_on:
            self.preview_on = False
            self.preview_thread.join()
            cv2.destroyAllWindows()

    def on_window_close(self):
        self.close_preview()
        self.window.destroy()

    def start(self):
        try:
            self.window.mainloop()
        except Exception as e:
            print(f"Error running the window\nError: {str(e)}")

    def stop(self):
        try:
            if self.camera_on:
                self.camera.release()
            self.window.quit()
        except Exception as e:
            print(f"Error stopping the window\nError: {str(e)}")

# def main():
#     camera_config = CameraConfigWindow(False, 3, 15)
#     camera_config.start()

# if __name__ == "__main__":
#     main()
