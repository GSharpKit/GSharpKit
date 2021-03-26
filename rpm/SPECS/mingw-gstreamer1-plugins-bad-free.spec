%{?mingw_package_header}

%global         api_version     1.0

Name:           mingw-gstreamer1-plugins-bad-free
Version:        1.18.3
Release:        1%{?dist}
Summary:        Cross compiled GStreamer1 plug-ins "bad"

# The freeze and nfs plugins are LGPLv2 (only)
License:        LGPLv2+ and LGPLv2
URL:            http://gstreamer.freedesktop.org/
# The source is:
# http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-{version}.tar.xz
# modified with gst1-p-bad-cleanup.sh from SOURCE1
Source0:        gst-plugins-bad-free-%{version}.tar.xz
Source1:        gst-p-bad-cleanup.sh
# Drop -std=c++98 from the cflags when building openexr support
#Patch0:         gst-ext-openexr-c++std.patch

BuildArch:      noarch

BuildRequires:  autoconf automake
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gstreamer1 >= %{version}
BuildRequires:  mingw64-gstreamer1 >= %{version}
BuildRequires:  mingw32-gstreamer1-plugins-base >= %{version}
BuildRequires:  mingw64-gstreamer1-plugins-base >= %{version}
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw32-orc
BuildRequires:  mingw64-orc
BuildRequires:  mingw32-pthreads
BuildRequires:  mingw64-pthreads
BuildRequires:  mingw32-jasper
BuildRequires:  mingw64-jasper
BuildRequires:  mingw32-gsm
BuildRequires:  mingw64-gsm
BuildRequires:  mingw32-openssl
BuildRequires:  mingw64-openssl
BuildRequires:  mingw32-wavpack
BuildRequires:  mingw64-wavpack
BuildRequires:  mingw32-opus
BuildRequires:  mingw64-opus
BuildRequires:  mingw32-nettle
BuildRequires:  mingw64-nettle
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw32-gnutls
BuildRequires:  mingw64-gnutls
#BuildRequires:  mingw32-curl
#BuildRequires:  mingw64-curl
BuildRequires:  mingw32-OpenEXR
BuildRequires:  mingw64-OpenEXR

# For glib-genmarshal
BuildRequires:  glib2-devel


%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested
well enough, or the code is not of good enough quality.


# Mingw32
%package -n mingw32-gstreamer1-plugins-bad-free
Summary:        %{summary}
Requires:       mingw32-gstreamer1 >= %{version}
Obsoletes:      mingw32-gstreamer1-plugins-bad < 1.14.1-1
Provides:       mingw32-gstreamer1-plugins-bad = 1.14.1-1

%description -n mingw32-gstreamer1-plugins-bad-free
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested
well enough, or the code is not of good enough quality.


# Mingw64
%package -n mingw64-gstreamer1-plugins-bad-free
Summary:        %{summary}
Requires:       mingw64-gstreamer1 >= %{version}
Obsoletes:      mingw64-gstreamer1-plugins-bad < 1.14.1-1
Provides:       mingw64-gstreamer1-plugins-bad = 1.14.1-1

%description -n mingw64-gstreamer1-plugins-bad-free
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested
well enough, or the code is not of good enough quality.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n gst-plugins-bad-%{version}

%build
%mingw_meson --default-library=shared
%mingw_ninja

%install
%mingw_ninja_install

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gstreamer-%{api_version}/*.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gstreamer-%{api_version}/*.a

find $RPM_BUILD_ROOT -name '*.la' -delete

%mingw_find_lang gstreamer1-plugins-bad-free --all-name


# Mingw32
%files -n mingw32-gstreamer1-plugins-bad-free -f mingw32-gstreamer1-plugins-bad-free.lang
%license COPYING
%doc AUTHORS README REQUIREMENTS

# exe
%{mingw32_bindir}/gst-transcoder-1.0.exe
%{mingw32_bindir}/playout.exe

# libraries
%{mingw32_bindir}/libgstadaptivedemux-1.0-0.dll
%{mingw32_bindir}/libgstbadaudio-1.0-0.dll
%{mingw32_bindir}/libgstbasecamerabinsrc-1.0-0.dll
%{mingw32_bindir}/libgstcodecparsers-1.0-0.dll
%{mingw32_bindir}/libgstinsertbin-1.0-0.dll
%{mingw32_bindir}/libgstisoff-1.0-0.dll
%{mingw32_bindir}/libgstmpegts-1.0-0.dll
%{mingw32_bindir}/libgstphotography-1.0-0.dll
%{mingw32_bindir}/libgstplayer-1.0-0.dll
%{mingw32_bindir}/libgsturidownloader-1.0-0.dll
%{mingw32_bindir}/libgstwebrtc-1.0-0.dll
%{mingw32_bindir}/libgstsctp-1.0-0.dll
%{mingw32_bindir}/libgstcodecs-1.0-0.dll
%{mingw32_bindir}/libgsttranscoder-1.0-0.dll


# bad plugins
%dir %{mingw32_libdir}/gstreamer-%{api_version}
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaccurip.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstadpcmdec.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstadpcmenc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaiff.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstasfmux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiobuffersplit.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiofxbad.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiolatency.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiomixmatrix.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiovisualizers.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstautoconvert.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstbayer.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstbz2.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcamerabin.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcoloreffects.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstd3d.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdebugutilsbad.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdecklink.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdirectsoundsrc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdtls.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstfaceoverlay.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstfestival.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstfieldanalysis.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstfreeverb.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstfrei0r.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgaudieffects.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgdp.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgeometrictransform.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgsm.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsthls.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstid3tag.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstinter.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstinterlace.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstivfparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstivtc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstjp2kdecimator.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstjpegformat.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstlegacyrawparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmidi.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmpegpsdemux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmpegpsmux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmpegtsdemux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmpegtsmux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmxf.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstnetsim.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstopenexr.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstopusparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstpcapparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstpnm.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstproxy.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstremovesilence.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrfbsrc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrtponvif.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsdpelem.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsegmentclip.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsmooth.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsmoothstreaming.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstspeed.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsubenc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsttimecode.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstttmlsubs.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideofiltersbad.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideoframe_audiolevel.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideoparsersbad.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideosignal.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvmnc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwasapi.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwinscreencap.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsty4mdec.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstclosedcaption.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrsvg.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstd3d11.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdash.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdvbsubenc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdvbsuboverlay.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdvdspu.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstipcpipeline.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstnvcodec.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrist.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrtmp2.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrtpmanagerbad.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsctp.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsiren.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstswitchbin.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsttranscode.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwebp.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwinks.dll

# %files devel
# plugin helper library headers
%{mingw32_includedir}/gstreamer-%{api_version}/gst/audio/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/basecamerabinsrc/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/codecparsers/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/interfaces/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/insertbin/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/isoff/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/mpegts/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/player/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/uridownloader/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/webrtc/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/sctp/
%{mingw32_includedir}/gstreamer-%{api_version}/gst/transcoder/

%{mingw32_libdir}/libgstadaptivedemux-1.0.dll.a
%{mingw32_libdir}/libgstbadaudio-1.0.dll.a
%{mingw32_libdir}/libgstbasecamerabinsrc-1.0.dll.a
%{mingw32_libdir}/libgstcodecparsers-1.0.dll.a
%{mingw32_libdir}/libgstinsertbin-1.0.dll.a
%{mingw32_libdir}/libgstisoff-1.0.dll.a
%{mingw32_libdir}/libgstmpegts-1.0.dll.a
%{mingw32_libdir}/libgstphotography-1.0.dll.a
%{mingw32_libdir}/libgstplayer-1.0.dll.a
%{mingw32_libdir}/libgsturidownloader-1.0.dll.a
%{mingw32_libdir}/libgstwebrtc-1.0.dll.a
%{mingw32_libdir}/libgstsctp-1.0.dll.a
%{mingw32_libdir}/libgstcodecs-1.0.dll.a
%{mingw32_libdir}/libgsttranscoder-1.0.dll.a

%{mingw32_libdir}/pkgconfig/gstreamer-bad-audio-1.0.pc
%{mingw32_libdir}/pkgconfig/gstreamer-codecparsers-1.0.pc
%{mingw32_libdir}/pkgconfig/gstreamer-insertbin-1.0.pc
%{mingw32_libdir}/pkgconfig/gstreamer-mpegts-1.0.pc
%{mingw32_libdir}/pkgconfig/gstreamer-player-1.0.pc
%{mingw32_libdir}/pkgconfig/gstreamer-plugins-bad-1.0.pc
%{mingw32_libdir}/pkgconfig/gstreamer-webrtc-1.0.pc
%{mingw32_libdir}/pkgconfig/gstreamer-sctp-1.0.pc
%{mingw32_libdir}/pkgconfig/gstreamer-photography-1.0.pc
%{mingw32_libdir}/pkgconfig/gstreamer-transcoder-1.0.pc

%{mingw32_datadir}/gstreamer-1.0/presets/GstFreeverb.prs

%dir %{mingw32_datadir}/gstreamer-%{api_version}/encoding-profiles
%{mingw32_datadir}/gstreamer-%{api_version}/encoding-profiles/

# Mingw64
%files -n mingw64-gstreamer1-plugins-bad-free -f mingw64-gstreamer1-plugins-bad-free.lang

# exe
%{mingw64_bindir}/gst-transcoder-1.0.exe
%{mingw64_bindir}/playout.exe

# libraries
%{mingw64_bindir}/libgstadaptivedemux-1.0-0.dll
%{mingw64_bindir}/libgstbadaudio-1.0-0.dll
%{mingw64_bindir}/libgstbasecamerabinsrc-1.0-0.dll
%{mingw64_bindir}/libgstcodecparsers-1.0-0.dll
%{mingw64_bindir}/libgstinsertbin-1.0-0.dll
%{mingw64_bindir}/libgstisoff-1.0-0.dll
%{mingw64_bindir}/libgstmpegts-1.0-0.dll
%{mingw64_bindir}/libgstphotography-1.0-0.dll
%{mingw64_bindir}/libgstplayer-1.0-0.dll
%{mingw64_bindir}/libgsturidownloader-1.0-0.dll
%{mingw64_bindir}/libgstwebrtc-1.0-0.dll
%{mingw64_bindir}/libgstsctp-1.0-0.dll
%{mingw64_bindir}/libgstcodecs-1.0-0.dll
%{mingw64_bindir}/libgsttranscoder-1.0-0.dll

# bad plugins
%dir %{mingw64_libdir}/gstreamer-%{api_version}
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaccurip.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstadpcmdec.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstadpcmenc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaiff.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstasfmux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiobuffersplit.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiofxbad.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiolatency.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiomixmatrix.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiovisualizers.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstautoconvert.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstbayer.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstbz2.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcamerabin.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcoloreffects.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstd3d.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdebugutilsbad.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdecklink.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdirectsoundsrc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdtls.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstfaceoverlay.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstfestival.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstfieldanalysis.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstfreeverb.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstfrei0r.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgaudieffects.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgdp.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgeometrictransform.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgsm.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsthls.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstid3tag.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstinter.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstinterlace.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstivfparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstivtc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstjp2kdecimator.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstjpegformat.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstlegacyrawparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmidi.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmpegpsdemux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmpegpsmux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmpegtsdemux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmpegtsmux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmxf.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstnetsim.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstopenexr.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstopusparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstpcapparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstpnm.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstproxy.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstremovesilence.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrfbsrc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrtponvif.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsdpelem.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsegmentclip.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsmooth.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsmoothstreaming.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstspeed.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsubenc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsttimecode.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstttmlsubs.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideofiltersbad.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideoframe_audiolevel.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideoparsersbad.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideosignal.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvmnc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwasapi.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwinscreencap.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsty4mdec.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstclosedcaption.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrsvg.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstd3d11.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdash.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdvbsubenc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdvbsuboverlay.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdvdspu.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstipcpipeline.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstnvcodec.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrist.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrtmp2.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrtpmanagerbad.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsctp.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsiren.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstswitchbin.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsttranscode.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwebp.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwinks.dll

# %files devel
# plugin helper library headers
%{mingw64_includedir}/gstreamer-%{api_version}/gst/audio/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/basecamerabinsrc/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/codecparsers/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/interfaces/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/insertbin/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/isoff/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/mpegts/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/player/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/uridownloader/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/webrtc/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/sctp/
%{mingw64_includedir}/gstreamer-%{api_version}/gst/transcoder/

%{mingw64_libdir}/libgstadaptivedemux-1.0.dll.a
%{mingw64_libdir}/libgstbadaudio-1.0.dll.a
%{mingw64_libdir}/libgstbasecamerabinsrc-1.0.dll.a
%{mingw64_libdir}/libgstcodecparsers-1.0.dll.a
%{mingw64_libdir}/libgstinsertbin-1.0.dll.a
%{mingw64_libdir}/libgstisoff-1.0.dll.a
%{mingw64_libdir}/libgstmpegts-1.0.dll.a
%{mingw64_libdir}/libgstphotography-1.0.dll.a
%{mingw64_libdir}/libgstplayer-1.0.dll.a
%{mingw64_libdir}/libgsturidownloader-1.0.dll.a
%{mingw64_libdir}/libgstwebrtc-1.0.dll.a
%{mingw64_libdir}/libgstsctp-1.0.dll.a
%{mingw64_libdir}/libgstcodecs-1.0.dll.a
%{mingw64_libdir}/libgsttranscoder-1.0.dll.a

%{mingw64_libdir}/pkgconfig/gstreamer-bad-audio-1.0.pc
%{mingw64_libdir}/pkgconfig/gstreamer-codecparsers-1.0.pc
%{mingw64_libdir}/pkgconfig/gstreamer-insertbin-1.0.pc
%{mingw64_libdir}/pkgconfig/gstreamer-mpegts-1.0.pc
%{mingw64_libdir}/pkgconfig/gstreamer-player-1.0.pc
%{mingw64_libdir}/pkgconfig/gstreamer-plugins-bad-1.0.pc
%{mingw64_libdir}/pkgconfig/gstreamer-webrtc-1.0.pc
%{mingw64_libdir}/pkgconfig/gstreamer-sctp-1.0.pc
%{mingw64_libdir}/pkgconfig/gstreamer-photography-1.0.pc
%{mingw64_libdir}/pkgconfig/gstreamer-transcoder-1.0.pc

%{mingw64_datadir}/gstreamer-1.0/presets/GstFreeverb.prs

%dir %{mingw64_datadir}/gstreamer-%{api_version}/encoding-profiles
%{mingw64_datadir}/gstreamer-%{api_version}/encoding-profiles/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 1.14.2-7
- Rebuild (OpenEXR)

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.14.2-6
- Rebuild (Changes/Mingw32GccDwarf2)

* Tue Aug 20 2019 Michael Cronenworth <mike@cchtml.com> - 1.14.2-5
- Rebuild for Nettle 3.5.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Sandro Mani <manisandro@gmail.com> - 1.14.2-3
- Rebuild (OpenEXR)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 24 2018 Christophe Fergeau <cfergeau@redhat.com> - 1.14.2-1
- Update to 1.14.2

* Fri Aug 24 2018 Richard W.M. Jones <rjones@redhat.com> - 1.14.1-2
- Rebuild for new mingw-openssl.

* Thu Jul 19 2018 Victor Toso <victortoso@redhat.com> - 1.14.1-1
- Update to 1.14.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Sandro Mani <manisandro@gmail.com> - 1.12.3-2
- Rebuild (OpenEXR)

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 1.12.3-1
- Update to 1.12.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 1.12.1-1
- Update to 1.12.1

* Wed Feb  8 2017 Victor Toso <victortoso@redhat.com> - 1.11.1-1
- Update to 1.11.1
- Add audiobuffersplit
- Dataurisrc was moved to core
- Add ttmlsubs plugin
- Fix CVE-2017-5843
- Fix CVE-2017-5848

* Sat Nov  5 2016 Victor Toso <victortoso@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Thu May 12 2016 Kalev Lember <klember@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 26 2015 Kalev Lember <klember@redhat.com> - 1.6.0-1
- Update to 1.6.0
- Use license macro for COPYING
- Drop libtool .la files

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.4.4-3
- Add proper obsoletes/provides tags to provide working upgrade path
  This is needed as the binary packages were renamed in a recent commit

* Thu May 14 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.4-2
- Rebuilt for mingw-gnutls 3.4 ABI change

* Mon Dec  1 2014 Victor Toso <victortoso@redhat.com> - 1.4.4-1
- Initial packaging.
  Resolves: rhbz#1166852
