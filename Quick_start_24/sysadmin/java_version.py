#!/usr/bin/python3

java_versions = [ '1.6', '1.7', '1.8', '1.9', '2.0']
required_java_version = ['1.8']

if required_java_version in java_versions:
    print(f"This machine has required JAVA Version {required_java_version}")
else:
    print(f" Invalid Java version is installed on this machine {required_java_version}")
    
