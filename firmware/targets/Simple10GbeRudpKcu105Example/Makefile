# Define target output
target: prom

# Define Firmware Version: v1.1.0.0
export PRJ_VERSION = 0x01010000

# Define target part
export PRJ_PART = XCKU040-FFVA1156-2-E

# Define the TOP_DIR path
export TOP_DIR = $(abspath $(PWD)/../..)

# Using XVC Debug bridge
export USE_XVC_DEBUG = 1

# Setup for releases.yaml
export RELEASE = all

# Use top level makefile
include ../../submodules/ruckus/system_vivado.mk
