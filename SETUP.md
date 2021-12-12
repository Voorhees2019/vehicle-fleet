## Prerequisites
> Python 3.9

### Installing Python 3.9 with Apt

Update the packages list and install the prerequisites:
```
sudo apt update
sudo apt install software-properties-common
```

Add the deadsnakes PPA to your system’s sources list:
```
sudo add-apt-repository ppa:deadsnakes/ppa
```
- When prompted, press `[Enter]` to continue.

Once the repository is enabled, you can install Python 3.9 by executing:
```
sudo apt install python3.9
```

### Installing Python 3.9 from source [Alternative way]

Install the dependencies necessary to build Python:
```
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
```

Download release’s source code from the [Python download page](https://www.python.org/downloads/source/) with [wget](https://linuxize.com/post/wget-command-examples/):
```
wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tgz
```

Once the download is complete, [extract the gzipped archive](https://linuxize.com/post/how-to-extract-unzip-tar-gz-file/):
```
tar -xf Python-3.9.2.tgz
```

Switch to the Python source directory and run the configure script, which performs a number of checks to make sure all of the dependencies on your system are present:
```
cd Python-3.9.2
./configure --enable-optimizations
```
- The `--enable-optimizations` option optimizes the Python binary by running multiple tests. This makes the build process slower.

Start the Python 3.9 build process:
```
make -j 8
```
- For faster build time, modify the `-j` to correspond to the number of cores in your processor. You can find the number by typing `nproc`.

When the build process is complete, install the Python binaries by typing:
```
sudo make altinstall
```
- We’re using `altinstall` instead of `install` because later will overwrite the default system python3 binary.

## Project Setup

Clone repo
```
git clone https://github.com/Voorhees2019/vehicle-fleet.git
cd vehicle-fleet
```

Install dependencies:
```
make setup
```
or
```
pip install -r requirements.txt
```

Apply project migrations:
```
make db
```
or
```
python manage.py migrate
```

Create a new superuser: 
```
make createsuperuser
```
or
```
python manage.py createsuperuser
```

Run the server:
```
make run
```
or
```
python manage.py runserver
```
