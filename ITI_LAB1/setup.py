from setuptools import setup

package_name = 'ITI_LAB1'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='saeed',
    maintainer_email='saed01151599985@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        "iti_pub_lab1=ITI_LAB1.str_publisher:main",
        "iti_sub_lab1=ITI_LAB1.number_counter:main"
        ],
    },
)
