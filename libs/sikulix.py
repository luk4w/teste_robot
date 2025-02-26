import subprocess
import os
from robot.api.deco import keyword

'''
Runs a SikuliX script using the specified script directory and script name.
Args:
    scripts_dir (str): The directory where the SikuliX scripts are located.
    script_name (str): The name of the SikuliX script to run (without the .sikuli extension).
Returns:
    str: The standard output from running the SikuliX script.
Raises:
    FileNotFoundError: If the SikuliX JAR file or the specified script file is not found.
    RuntimeError: If there is an error in executing the SikuliX script.
'''
@keyword("Run Sikuli Script")
def run_sikuli_script(scripts_dir, script_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sikuli_jar = os.path.join(dir_path, "sikulixide-2.0.5-win.jar")
    
    # Check if the JAR file exists in the specified path
    if not os.path.exists(sikuli_jar):
        raise FileNotFoundError(f"Unable to find the SikuliX JAR in directory {dir_path}")
    
    # Check if the script file exists in the scripts path
    script_path = os.path.join(scripts_dir, script_name + ".sikuli", script_name + ".py")
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"Unable to find the SikuliX script in directory {scripts_dir}")
    
    sikulix_cmd = ["java", "-Dsikuli.Debug=ERROR", "-jar", sikuli_jar, "-r", script_path, "-q"]

    # Run the command
    result = subprocess.run(sikulix_cmd, capture_output=True, text=True)

    # Check if there was an error in executing SikuliX
    if result.returncode != 0:
        raise RuntimeError(f"Test failed in SikuliX: {script_path}")

    return result.stdout
