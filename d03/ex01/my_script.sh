#!/bin/bash

LIB_DIR=local_lib

pip3 --version

mkdir -pv $LIB_DIR
pip install \
	--target=$LIB_DIR \
	--force-reinstall \
	--upgrade \
	git+https://github.com/jaraco/path.py.git 2>&1 \
	| tee -a my_install.log

./my_program.py
