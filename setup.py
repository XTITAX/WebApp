from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='WebApp',
    version='1.0',
    author='XTITAX',
    author_email='xtitax@yandex.ru',
    description='Библиотека для веб приложения',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/XTITAX/WebApp',
    packages=find_packages(include=['WebApp']),
    include_package_data=True,
    package_data={
        'WebApp': ['jdk-22/**/*', 'jdk-22/lib/**/*', '.gitignore'],  # Включает все файлы и папки в jdk-22
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
