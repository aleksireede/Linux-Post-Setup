#!/bin/bash
isofile = wit-v3.04a-r8427-x86_64
szsfile = szs-v2.26a-r8462-x86_64
wget https://wit.wiimm.de/download/$isofile.tar.gz
tar -xf $isofile.tar.gz
cd $isofile
chmod u+x ./install.sh
./install.sh
cd ..
rm -rf $isofile
rm -rf $isofile.tar.gz
wget https://szs.wiimm.de/download/$szsfile.tar.gz
tar -xf $szsfile.tar.gz
cd $szsfile
chmod u+x ./install.sh
./install.sh
cd ..
rm -rf $szsfile
rm -rf $szsfile.tar.gz
