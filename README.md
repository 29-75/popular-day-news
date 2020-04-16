
<!-- TOC -->

- [1. Python Virtualenv 환경 구축하기](#1-python-virtualenv-%ed%99%98%ea%b2%bd-%ea%b5%ac%ec%b6%95%ed%95%98%ea%b8%b0)
  - [virtualenv란!?](#virtualenv%eb%9e%80)
- [2. web-crawling](#2-web-crawling)
# 1. Python Virtualenv 환경 구축하기
## virtualenv란!?
> python의 가상환경 virtualenv 모듈의 사용법을 간단하게 정리한다. python의 가상환경이란, 작은 python을 새로 설치해서 내가 원하는 모듈만 운용하는 바구니라고 생각하면 된다. 운영체제 안에서 새로 운영체제를 만들어내는 가상 머신(virtual machine)과 같은 맥락이라고 볼 수 있다. 같은 모듈이라도 이 버젼 저 버젼 다른 버젼이 필요할 때나, python 프로그램을 실행하기 위한 최소한의 환경을 마련하고자 할 때, 그리고 github 등의 저장소와 연계하고자 할 때 등 가상환경은 매우 다양하게 사용될 수 있다. 이젠 필수적인 요소가 된 python 가상 환경의 리눅스/윈도우에서의 사용법을 정리한다.

출처: https://dgkim5360.tistory.com/entry/python-virtualenv-on-linux-ubuntu-and-windows [개발새발로그]

1. python(v3.7) 버전 확인

        python3 --version

2. python3.7이 아니거나, 없다면 설치
		
        wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
        tar xvf Python-3.7.0.tar.xz
        cd Python-3.7.0
        ./configure
        sudo make altinstall

3. virtualenv 구축

        python3 -m virtualenv venv
        source venv/bin/activate

4. python modeul (requirement) 설치

        pip3 install -r requirements.txt

5. flask server 실행

        cd src
        python3 main.py

6. 동작 확인

        curl localhost:8080/route_name


# 2. web-crawling
