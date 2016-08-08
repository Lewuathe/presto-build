presto-build
===

presto-build is a docker container which includes all prerequisites for building [Presto](https://prestodb.io/).

# Why presto-build?

Presto built on OSX does not work with Linux because of JNI issue. We will see not found BSDVirtualMachine exception. And also Presto only supports x86_64 on Linux as described [here](https://github.com/prestodb/presto/issues/3849). So the easiest way to build Presto on Linux running x86_64 machine. But how can we build without Linux (like me!). I want to described a way to build Presto which can run on Linux without Linux here.

# How to build

## 1. Clone repository

```bash
$ git clone git@github.com:Lewuathe/presto-build.git
```

## 2. Set presto project directory

```bash
$ export PRESTO_HOME=/path/to/presto
```

## 3. Remove presto-doc

Due to incompatibility with PPC64 architecture. The detail is written [here](https://github.com/prestodb/presto/issues/3849).
```
$ cd /path/to/presto
$ vi pom.xml

## Comment out presto-doc from module
## <!-- <module>presto-docs</module> -->
```

## 4. Start docker container

```
$ cd presto-build
$ ./start-build-env.sh
```

Now you can build presto package on this container. The simplest command to build is

```
$ ./mvnw clean package -DskipTests
```

# LICENSE

MIT License
