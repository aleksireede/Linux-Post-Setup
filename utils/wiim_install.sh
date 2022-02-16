#!/bin/bash
isofile = wit-v3.04a-r8427-x86_64.tar.gz
szsfile = szs-v2.26a-r8462-x86_64.tar.gz
wget https://wit.wiimm.de/download/$isofile
tar -xf $isofile
cd $isofile
./install.sh
cd ..
rm -rf $isofile
wget https://szs.wiimm.de/download/$szsfile
tar -xf $szsfile
cd $szsfile
./install.sh
cd ..
rm -rf $szsfile
