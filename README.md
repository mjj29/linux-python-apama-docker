# Apama core python installation in Docker

This project contains Dockerfile for installing Python 3.6 or 3.7 on various
Linux base images. It also contains a simple Apama project to demonstrate use
of this Python with Apama.

These Dockerfiles are mainly intended as ways to demonstrate installing an 
appropriate Python on that distribution and the instructions contained within
will work for any installation of that distribution.

## License

Copyright (c) 2018-2019 Software AG, Darmstadt, Germany and/or its licensors

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this
file except in compliance with the License. You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the
License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied.
See the License for the specific language governing permissions and limitations under the License.

## Using the Dockerfiles

To use these Dockerfiles you will need a copy of the Apama core
installation from [http://www.apamacommunity.com](http://www.apamacommunity.com/). Unpack it into this directory
under a folder named 'core'.

Next, choose one of the following Linux distributions to use as your base image.

For Apama 10.3:

* CentOS 7 (Installs Python from EPEL repository)
* Ubuntu Bionic (Installs Python from main repository)
* Debian Buster (Installs Python from main repository)
* OpenSuse Leap 15 (Installs Python from main repository)
* Ubuntu Xenial (Installs Python from a PPA)
* Debian Stretch (Builds Python from source)
* Debian Jessie (Builds Python from source)
* OpenSuse Leap 42 (Builds Python from source)

For Apama 10.5:

* CentOS 7 (Builds Python from source)
* Ubuntu Bionic (Installs Python from main repository)
* Ubuntu Cosmic (Installs Python from main repository)
* Ubuntu Disco (Installs Python from main repository)
* Ubuntu Eoan (Installs Python from main repository)
* Debian Bullseye (Installs Python from main repository)
* Debian Buster (Installs Python from main repository)
* OpenSuse Tumbleweed (Installs Python from the main repository)
* OpenSuse Leap (Builds Python from Source)
* Ubuntu Xenial (Installs Python from a PPA)
* Debian Jessie (Builds Python from source)

Once you have chosen the distribution and release to use as a base image, build the image with:

    docker build -t projectimage -f Apama10.3/Dockerfile.distribution:release .

Once that has completed you can run the demo project in the docker image with:

    docker run --rm -t -i projectimage

## Using Python within Apama
    
For more details about how to use Python within Apama please see the documentation and forums on [http://www.apamacommunity.com](http://www.apamacommunity.com)
