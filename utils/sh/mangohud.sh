#!/usr/bin/env bash
git clone --recurse-submodules https://github.com/flightlessmango/MangoHud.git
cd MangoHud
meson build
ninja -C build install
