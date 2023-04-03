import json
import pkg_resources
import pyautogui
import subprocess

def packages(file_path):
    result = subprocess.run(['pip', 'list', '--format', 'json'], capture_output=True)
    packages = json.loads(result.stdout.decode('utf-8'))

    with open(file_path, 'w') as f:
        json.dump(packages, f, indent=4)

    pyautogui.hotkey('shift', 'alt', 'f')

def save_packages(file_path):
    result = subprocess.run(['pip', 'freeze'], capture_output=True)
    packages = result.stdout.decode('utf-8').split('\n')

    packages_with_versions = []
    for package in packages:
        try:
            package_name = package.split('==')[0]
            package_version = pkg_resources.get_distribution(package_name).version
            packages_with_versions.append(f"{package_name}=={package_version}")
        except:
            pass
    with open(file_path, 'w') as f:
        f.write('\n'.join(packages_with_versions))



# pip install -r requirements.txt
if "__main__" == __name__:
    packages('packages.json')
    save_packages('requirements.txt')
