#!/bin/sh

# Process a gst-plugins-bad tarball to remove
# unwanted GStreamer plugins.
#
# See https://bugzilla.redhat.com/show_bug.cgi?id=532470
# for details
#
# Bastien Nocera <bnocera@redhat.com> - 2010
#

VERSION="$1"
SOURCE_URL="http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-${VERSION}.tar.xz"
SOURCE="gst-plugins-bad-${VERSION}.tar.xz"
wget ${SOURCE_URL}
NEW_SOURCE=`echo $SOURCE | sed 's/bad-/bad-free-/'`
DIRECTORY=`echo $SOURCE | sed 's/\.tar\.xz//'`

ALLOWED="
aacparse
accurip
adpcmdec
adpcmenc
aiff
aiffparse
amrparse
asfmux
audiobuffersplit
audiofxbad
audiolatency
audiomixer
audiomixmatrix
audioparsers
audiovisualizers
autoconvert
bayer
camerabin
camerabin2
cdxaparse
codecalpha
codectimestamper
coloreffects
colorspace
compositor
dataurisrc
dccp
debugutils
dtmf
dvbsubenc
dvbsuboverlay
faceoverlay
festival
fieldanalysis
freeverb
freeze
frei0r
gaudieffects
gdp
geometrictransform
h264parse
hdvparse
hls
id3tag
insertbin
inter
interlace
invtelecine
ivfparse
ivtc
jpegformat
jp2kdecimator
legacyresample
librfb
liveadder
midi
mse
mve
mpegdemux
mpeg4videoparse
mpegpsmux
mpegtsdemux
mpegtsmux
mpegvideoparse
mxf
netsim
nsf
nuvdemux
onvif
openh264
patchdetect
pcapparse
pnm
proxy
qtmux
rawparse
removesilence
rist
rtmp2
rtp
rtpmux
rtpvp8
scaletempo
sdi
sdp
segmentclip
selector
siren
smooth
speed
stereo
subenc
switchbin
tensordecoders
timecode
transcode
tta
unixfd
valve
videofilters
videoframe_audiolevel
videomaxrate
videomeasure
videoparsers
videosignal
vmnc
yadif
y4m
"

NOT_ALLOWED="
dvdspu
"

error()
{
	MESSAGE=$1
	echo $MESSAGE
	exit 1
}

check_allowed()
{
	MODULE=$1
	for i in $ALLOWED ; do
		if test x$MODULE = x$i ; then
			return 0;
		fi
	done
	# Ignore errors coming from ext/ directory
	# they require external libraries so are ineffective anyway
	return 1;
}

check_not_allowed()
{
	MODULE=$1
	for i in $NOT_ALLOWED ; do
		if test x$MODULE = x$i ; then
			return 0;
		fi
	done
	return 1;
}

rm -rf $DIRECTORY
tar xJf $SOURCE || error "Cannot unpack $SOURCE"
pushd $DIRECTORY > /dev/null || error "Cannot open directory \"$DIRECTORY\""

unknown=""
for subdir in gst ext sys; do
	for dir in $subdir/* ; do
		# Don't touch non-directories
		if ! [ -d $dir ] ; then
			continue;
		fi
		MODULE=`basename $dir`
		if ( check_not_allowed $MODULE ) ; then
			echo "**** Removing $MODULE ****"
			echo "Removing directory $dir"
			rm -r $dir || error "Cannot remove $dir"
			echo "Removing $(basename $dir) from gst/meson.build"
			sed -i "s|'$(basename $dir)',||g" gst/meson.build
			echo
		elif test $subdir = ext  || test $subdir = sys; then
			# Ignore library or system non-blacklisted plugins
			continue;
		elif ! ( check_allowed $MODULE ) ; then
			echo "Unknown module in $dir"
			unknown="$unknown $dir"
		fi
	done
done

echo

if test "x$unknown" != "x"; then
  echo -n "Aborting due to unkown modules: "
  echo "$unknown" | sed "s/ /\n  /g"
  exit 1
fi

popd > /dev/null

tar cJf $NEW_SOURCE $DIRECTORY
echo "$NEW_SOURCE is ready to use"

