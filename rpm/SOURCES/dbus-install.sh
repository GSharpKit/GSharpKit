#!/bin/bash

pushd $(dirname $0) &>/dev/null

if [ ! -d /etc/dbus-1 ]; then
  mkdir /etc/dbus-1
fi
if [ ! -d /etc/dbus-1/session.d ]; then
  mkdir /etc/dbus-1/session.d
fi

cp ../etc/dbus-1/session.conf /etc/dbus-1/
sed -i '' 's!unix:tmpdir=\/tmp!launchd:env=DBUS_LAUNCHD_SESSION_BUS_SOCKET!' /etc/dbus-1/session.conf 

mkdir -p /usr/local/bin/
cp dbus-daemon /usr/local/bin/
cp ../Library/LaunchAgents/org.freedesktop.dbus-session.plist /Library/LaunchAgents/

popd &>/dev/null
