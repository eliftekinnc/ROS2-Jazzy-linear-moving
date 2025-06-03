from setuptools import setup, find_packages

package_name = 'my_bot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='elif',
    maintainer_email='eliftknc@gmail.com',
    description='Minimal turtlebot3 controller',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'go_to_point = my_bot_controller.go_to_point:main',
        ],
    },
)
