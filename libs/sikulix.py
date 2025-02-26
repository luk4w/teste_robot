import subprocess
import os
from robot.api.deco import keyword

@keyword("Run Sikuli Script")
def run_sikuli_script(script_path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sikuli_jar = os.path.join(dir_path, "sikulixide-2.0.5-win.jar")
    
    # Check if the JAR file exists in the specified path
    if not os.path.exists(sikuli_jar):
        raise FileNotFoundError(f"Unable to find the SikuliX JAR in directory {dir_path}")
    
    # Check if the script file exists in the specified path
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"Unable to find the SikuliX script in directory {script_path}")
    
    sikulix_cmd = ["java", "-Dsikuli.Debug=ERROR", "-jar", sikuli_jar, "-r", script_path, "-q"]

    # Run the command
    result = subprocess.run(sikulix_cmd, capture_output=True, text=True)

    # Check if there was an error in executing SikuliX
    if result.returncode != 0:
        raise RuntimeError(f"Test failed in SikuliX: {script_path}")

    return result.stdout
