# Face Blur
 
Real-time face blurring using your webcam with OpenCV and MediaPipe.
 
## Technologies
 
- Python
- OpenCV
- MediaPipe
## Installation
 
### 1. Clone the repository
 
**Linux / macOS**
```bash
git clone https://github.com/tu-usuario/face-blur.git
```
 
**Windows (CMD o PowerShell)**
```cmd
git clone https://github.com/tu-usuario/face-blur.git
```
 
> The folder `face-blur` will be created in whatever directory you run this command from. By default that is your home directory (`~` on Linux/macOS, `C:\Users\TuUsuario` on Windows).
 
---
 
### 2. Navigate into the project folder
 
**Linux / macOS**
```bash
cd face-blur
```
 
**Windows**
```cmd
cd face-blur
```
 
---
 
### 3. Run the setup script
 
Run this once to create the virtual environment and install all dependencies.
 
```bash
python setup.py
```
 
This will:
- Create a virtual environment named `face_blur`
- Install all dependencies from `requirements.txt`
---
 
### 4. Activate the virtual environment
 
**Linux / macOS**
```bash
source face_blur/bin/activate
```
 
**Windows**
```cmd
face_blur\Scripts\activate
```
 
---
 
## Customization
 
- **Virtual environment name** — You can change the venv name by editing `setup.py` and replacing `face_blur` with any name you prefer. Make sure to update the activation command accordingly.
- **Skip virtual environment creation** — If you prefer to manage dependencies manually or use a global environment, you can install the requirements directly with `pip install -r requirements.txt` and skip the `setup.py` step.
- **Modify the script** — `face_blur.py` is designed to be easily adjustable. Feel free to modify blur intensity, detection sensitivity, or any other behavior to fit your specific use case.
---
 
## Usage
 
```bash
python face_blur.py
```
 
Press `q` to quit.
 
