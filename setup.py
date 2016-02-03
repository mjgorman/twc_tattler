from setuptools import setup

setup(name='twc-tattler',
        version='1',
        packages=['twctattler'],
        author='Michael J Gorman',
        author_email='michael@michaeljgorman.com',
        url='tbd',
        install_requires=[
            'ping',
            'sendgrid',
            ],
        entry_points={
            'console_scripts': [
                'twc-tattler = twctattler.__main__:app',
                'twc-tattler-stats = twctattler.__main__:stats',
                ]
            },
        )
