import os
from glob import glob
from setuptools import setup

package_name = 'mail_delivery_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=["preceptions.IRDistanceCalc","control.actionTranslator","control.robotDriver","navigation.captain","preceptions.beaconSensor","preceptions.bumperSensor"],
    data_files=[
        # Install marker file in the package index
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        # Include our package.xml file
        (os.path.join('share', package_name), ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Stephen Wicklund',
    maintainer_email='stevewicklund@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'IRSensor = preceptions.IRDistanceCalc:main',
            'beacon_reader = preceptions.beaconSensor:main',
            'action_translator = control.actionTranslator:main',
            'robot_driver = control.robotDriver:main',
            'captain = navigation.captain:main',
            'bumper_sensor = preceptions.bumperSensor:main'
        ],
    },
)
