## JEB 1.5.201408040(full) keygen

### Origin Keygen Author
* [JEB 1.5.201408040(full) + keygen](http://bbs.pediy.com/showthread.php?t=202793)

### Downloads
* [Baidu cloud](http://pan.baidu.com/s/1eQscz6M): `http://pan.baidu.com/s/1eQscz6M`
* Password: `ea8m`

### Usage
* Windows : `java keygen`
* Windows, Linux, Mac : `python keygen.py`

### Note Issue In Mac
* `XstartOnFirstThread` : repleace old `JEB/64-bits/bin/swt.jar` to last release [swt-4.5-cocoa-macosx-x86_64](http://www.eclipse.org/swt/). or download directly [swt-4.5.2-cocoa-macosx-x86_64.zip](./jeb1.5/swt-4.5.2-cocoa-macosx-x86_64.zip)

## JEB2.2.7

### JDK install

jdk 1.8.0_121, [jdk all versions](https://www.oracle.com/technetwork/java/javase/downloads/java-archive-javase8-2177648.html)

### jenv install

```
brew install jenv

jenv add /Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Home
```

### JNI，BundleApp

```
sudo cp /Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Info.plist /Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Info.plist.bak

sudo vim /Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Info.plist
```

```
<key>JVMCapabilities</key>
<array>
    <string>CommandLine</string>
    <string>JNI</string> <!--++++-->
    <string>BundledApp</string>  <!--++++-->
</array>

```

```
sudo mkdir -p /Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Home/bundle/Libraries

sudo ln -s /Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Home/jre/lib/server/libjvm.dylib /Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Home/bundle/Libraries/libserver.dylib
```

### Downloads

[JEB-2.2.7破解版 for macOS](https://bbs.pediy.com/thread-230293.htm)

### Crack

download [crack.tar.gz](./jeb2.2/crack.tar.gz), unpack and copy all files to /path/to/jeb/

jenv local 1.8.0.121

./jeb_macos.sh
