#!/usr/bin/env python

from fabric.api import sudo, run

def uname():
    run('uname')

def prepare():
    sudo('apt-get update')
    sudo('apt-get install -y curl tar sudo rsync python wget')
    sudo('mkdir -p /usr/java/default')
    sudo("curl -Ls 'http://download.oracle.com/otn-pub/java/jdk/8u92-b14/jdk-8u92-linux-x64.tar.gz' -H 'Cookie: oraclelicense=accept-securebackup-cookie' | tar --strip-components=1 -xz -C /usr/java/default/")
    sudo('export JAVA_HOME=/usr/java/default')
    sudo('export PATH=$PATH:$JAVA_HOME/bin')

def install_maven():
    sudo('apt-get install -q install --no-install-recommends -y ant maven')

def deploy():
    prepare()
    install_maven()
