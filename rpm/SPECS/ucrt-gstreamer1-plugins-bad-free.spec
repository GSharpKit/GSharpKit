%{?ucrt_package_header}
%bcond_without extras

%global         api_version     1.0

Name:           ucrt-gstreamer1-plugins-bad-free
Version:        1.28.6
Release:        1%{?dist}
Summary:        Cross compiled GStreamer1 plug-ins "bad"

# main code is LGPL-2.1-or-later AND LGPL-2.0-or-later
# ext/aes/gstaeshelper.h ext/curl/curltask.h and several others are MIT OR LGPL-2.1-or-later
# ext/resindvd is MPL-1.1
# ext/sctp is BSD-2-Clause AND BSD-3-Clause
# ext/sctp/usrsctp/usrsctplib/netinet/sctp_ss_functions.c is BSD-2-Clause-Views
# ext/sctp/usrsctp/usrsctplib/netinet/sctp_userspace.c is BSD-2-Clause AND DOC
# gst/festival/gstfestival.c is MIT-Festival
# gst/freeverb/gstfreeverb.c is LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
# gst/mpegpsmux/mpegpsmux_h264.h is MPL-1.1 OR LGPL-2.0-or-later OR MIT
# gst-libs/gst/codecparsers/dboolhuff.c is BSD-3-Clause WITH AdditionRef-Dart
# sys/amfcode sys/dwrite/libcaption/ sys/qsv/libmfx/ are MIT
# sys/v4l2codecs/linux/media.h plus few other filese in this directory are GPL-2.0-only WITH Linux-syscall-note
License:        LGPL-2.1-or-later AND LGPL-2.0-or-later AND (MIT OR LGPL-2.1-or-later) AND MPL-1.1 AND BSD-2-Clause AND BSD-3-Clause AND BSD-2-Clause-Views AND (BSD-2-Clause AND DOC) AND MIT-Festival AND (LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain) AND (MPL-1.1 OR LGPL-2.0-or-later OR MIT) AND BSD-3-Clause WITH AdditionRef-Dart AND MIT AND GPL-2.0-only WITH Linux-syscall-note
URL:            http://gstreamer.freedesktop.org/
Source:         https://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
# Adapt for directxmath header location
Patch1:         gst-p-bad-directxmath.patch

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  orc-compiler

BuildRequires:  ucrt64-filesystem
BuildRequires:  ucrt64-gcc-c++
BuildRequires:  ucrt64-gstreamer1 >= %{version}
BuildRequires:  ucrt64-gstreamer1-plugins-base >= %{version}
BuildRequires:  ucrt64-bzip2
#BuildRequires:  ucrt64-curl
BuildRequires:  ucrt64-directx-headers
BuildRequires:  ucrt64-directxmath
BuildRequires:  ucrt64-gettext
BuildRequires:  ucrt64-gnutls
#BuildRequires:  ucrt64-gsm
BuildRequires:  ucrt64-gtk3
BuildRequires:  ucrt64-jasper
#BuildRequires:  ucrt64-lcms2
BuildRequires:  ucrt64-libgcrypt
BuildRequires:  ucrt64-librsvg2
BuildRequires:  ucrt64-libwebp
BuildRequires:  ucrt64-libxml2
BuildRequires:  ucrt64-nettle
#BuildRequires:  ucrt64-openexr
#BuildRequires:  ucrt64-openal-soft
#BuildRequires:  ucrt64-openjpeg2
#BuildRequires:  ucrt64-opus
BuildRequires:  ucrt64-orc
BuildRequires:  ucrt64-openssl
BuildRequires:  ucrt64-wavpack

# For glib-genmarshal
BuildRequires:  glib2-devel


%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested
well enough, or the code is not of good enough quality.


# Mingw64
%package -n ucrt64-gstreamer1-plugins-bad-free
Summary:        %{summary}
Requires:       ucrt64-gstreamer1 >= %{version}
Obsoletes:      ucrt64-gstreamer1-plugins-bad < 1.14.1-1
Provides:       ucrt64-gstreamer1-plugins-bad = 1.14.1-1
#Requires:       ucrt64-directxmath
#Requires:       ucrt64-directx-headers

%description -n ucrt64-gstreamer1-plugins-bad-free
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested
well enough, or the code is not of good enough quality.


%{?ucrt_debug_package}


%prep
%autosetup -p1 -n gst-plugins-bad-%{version}


%build
#   chromaprint was enabled in the !ucrt package in 6eadf04
#   openal, openjpeg, ofa, webp were enabled in the !ucrt package in c609b28
#   there are ucrt-openjpeg and ucrt-webp packages available
#   uvch264 was enabled in the !ucrt package in fcee991
#   curl and winks are disabled only in the ucrt package
mkdir build_ucrt
pushd build_ucrt
%global _old_ucrt64_cflags %{ucrt64_cflags}
%global ucrt64_cflags %{_old_ucrt64_cflags} -msse2
%ucrt64_meson \
    -Dpackage-name="Fedora Mingw GStreamer-plugins-bad package" \
    -Dpackage-origin="http://download.fedoraproject.org" \
    %{!?with_extras:-D fbdev=disabled -D decklink=disabled } \
    %{!?with_extras:-D assrender=disabled -D bs2b=disabled } \
    %{!?with_extras:-D chromaprint=disabled -D d3dvideosink=disabled } \
    %{!?with_extras:-D directsound=disabled -D dts=disabled } \
    %{!?with_extras:-D fluidsynth=disabled -D openexr=disabled } \
    %{!?with_extras:-D curl=disabled -D curl-ssh2=disabled } \
    %{!?with_extras:-D ttml=disabled -D kate=disabled } \
    %{!?with_extras:-D modplug=disabled -D ofa=disabled } \
    %{!?with_extras:-D vdpau=disabled -D openal=disabled } \
    %{!?with_extras:-D opencv=disabled -D openjpeg=disabled } \
    %{!?with_extras:-D wildmidi=disabled -D zbar=disabled } \
    %{!?with_extras:-D gme=disabled -D lv2=disabled } \
    -D doc=disabled -D magicleap=disabled -D msdk=disabled \
    -D dts=disabled -D faac=disabled -D faad=disabled \
    -D mpeg2enc=disabled -D mplex=disabled \
    -D neon=disabled -D rtmp=disabled -D rtmp2=disabled \
    -D flite=disabled -D sbc=disabled -D opencv=disabled \
    %{!?with_extras:-D spandsp=disabled -D va=disabled } \
    -D voamrwbenc=disabled -D x265=disabled \
    -D dvbsuboverlay=disabled -D dvdspu=disabled -D siren=disabled \
    -D opensles=disabled -D tinyalsa=disabled \
    -D wasapi=enabled -D wasapi2=disabled -D avtp=disabled \
    -D dc1394=disabled -D directfb=disabled -D iqa=disabled \
    -D libde265=disabled -D musepack=disabled -D openni2=disabled \
    -D sctp=disabled -D svthevcenc=disabled -D voaacenc=disabled \
    -D zxing=disabled -D wpe=disabled -D x11=disabled \
    -D openh264=disabled \
    -D examples=disabled -D tests=disabled \
    -D codec2json=disabled


ninja
popd


%install
pushd build_ucrt
DESTDIR=%{buildroot} ninja install
popd

# Clean out files that should not be part of the rpm.
rm -f %{buildroot}%{ucrt64_libdir}/gstreamer-%{api_version}/*.dll.a

# Mingw64
%files -n ucrt64-gstreamer1-plugins-bad-free
%license COPYING
%doc README.md
%{ucrt64_bindir}/gst-transcoder-1.0.exe
# libraries
%{ucrt64_bindir}/libgstadaptivedemux-1.0-0.dll
%{ucrt64_bindir}/libgstanalytics-1.0-0.dll
%{ucrt64_bindir}/libgstbadaudio-1.0-0.dll
%{ucrt64_bindir}/libgstbasecamerabinsrc-1.0-0.dll
%{ucrt64_bindir}/libgstcodecs-1.0-0.dll
%{ucrt64_bindir}/libgstcodecparsers-1.0-0.dll
%{ucrt64_bindir}/libgstcuda-1.0-0.dll
%{ucrt64_bindir}/libgstd3d11-1.0-0.dll
%{ucrt64_bindir}/libgstd3d12-1.0-0.dll
%{ucrt64_bindir}/libgstd3dshader-1.0-0.dll
%{ucrt64_bindir}/libgstdxva-1.0-0.dll
%{ucrt64_bindir}/libgsthip-0.dll
%{ucrt64_bindir}/libgstinsertbin-1.0-0.dll
%{ucrt64_bindir}/libgstisoff-1.0-0.dll
%{ucrt64_bindir}/libgstmpegts-1.0-0.dll
%{ucrt64_bindir}/libgstmse-1.0-0.dll
%{ucrt64_bindir}/libgstphotography-1.0-0.dll
%{ucrt64_bindir}/libgstplay-1.0-0.dll
%{ucrt64_bindir}/libgstplayer-1.0-0.dll
%{ucrt64_bindir}/libgstsctp-1.0-0.dll
%{ucrt64_bindir}/libgsttranscoder-1.0-0.dll
%{ucrt64_bindir}/libgsturidownloader-1.0-0.dll
%{ucrt64_bindir}/libgstwebrtc-1.0-0.dll

# bad plugins
%dir %{ucrt64_libdir}/gstreamer-%{api_version}
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstaccurip.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstadpcmdec.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstadpcmenc.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstaes.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstaiff.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstanalyticsoverlay.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstasfmux.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstasio.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstaudiobuffersplit.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstaudiofxbad.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstaudiolatency.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstaudiomixmatrix.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstaudiovisualizers.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstautoconvert.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstbayer.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstbz2.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstcamerabin.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstclosedcaption.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstcodecalpha.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstcoloreffects.dll
#{ucrt64_libdir}/gstreamer-%{api_version}/libgstcolormanagement.dll
#{ucrt64_libdir}/gstreamer-%{api_version}/libgstcurl.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstd3d.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstd3d11.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstd3d12.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstdash.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstdebugutilsbad.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstdecklink.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstdirectsoundsrc.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstdtls.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstdwrite.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstdvbsubenc.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstfaceoverlay.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstfestival.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstfieldanalysis.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstfreeverb.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstfrei0r.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstgaudieffects.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstgdp.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstgeometrictransform.dll
#{ucrt64_libdir}/gstreamer-%{api_version}/libgstgsm.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgsthip.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgsthls.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstid3tag.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstinsertbin.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstinter.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstinterlace.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstipcpipeline.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstivfparse.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstivtc.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstjp2kdecimator.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstjpegformat.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstlegacyrawparse.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstmediafoundation.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstmidi.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstmpegpsdemux.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstmpegpsmux.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstmpegtsdemux.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstmpegtsmux.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstmse.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstmxf.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstnetsim.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstnvcodec.dll
#{ucrt64_libdir}/gstreamer-%{api_version}/libgstopenal.dll
#{ucrt64_libdir}/gstreamer-%{api_version}/libgstopenexr.dll
#{ucrt64_libdir}/gstreamer-%{api_version}/libgstopenjpeg.dll
#{ucrt64_libdir}/gstreamer-%{api_version}/libgstopusparse.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstpcapparse.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstpnm.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstproxy.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstremovesilence.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstrfbsrc.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstrist.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstrsvg.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstrtpmanagerbad.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstrtponvif.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstsdpelem.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstsegmentclip.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstsmooth.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstsmoothstreaming.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstspeed.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstsubenc.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstswitchbin.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgsttensordecoders.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgsttimecode.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgsttranscode.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstttmlsubs.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstvideofiltersbad.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstvideoframe_audiolevel.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstvideoparsersbad.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstvideosignal.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstvmnc.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstwasapi.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstwebp.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstwinks.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstwinscreencap.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstamfcodec.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstcodectimestamper.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstqsv.dll
%{ucrt64_libdir}/gstreamer-%{api_version}/libgstwin32ipc.dll

# plugin helper library headers
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/analytics/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/audio/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/basecamerabinsrc/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/codecparsers/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/hip/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/interfaces/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/insertbin/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/isoff/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/mse/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/mpegts/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/play/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/player/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/sctp/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/transcoder/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/uridownloader/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/webrtc/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/cuda/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/d3d11/
%{ucrt64_includedir}/gstreamer-%{api_version}/gst/d3d12/

%{ucrt64_libdir}/gstreamer-%{api_version}/include/
%{ucrt64_libdir}/libgstadaptivedemux-%{api_version}.dll.a
%{ucrt64_libdir}/libgstanalytics-%{api_version}.dll.a
%{ucrt64_libdir}/libgstbadaudio-%{api_version}.dll.a
%{ucrt64_libdir}/libgstbasecamerabinsrc-%{api_version}.dll.a
%{ucrt64_libdir}/libgstcodecs-%{api_version}.dll.a
%{ucrt64_libdir}/libgstcodecparsers-%{api_version}.dll.a
%{ucrt64_libdir}/libgstd3d11-%{api_version}.dll.a
%{ucrt64_libdir}/libgstd3d12-%{api_version}.dll.a
%{ucrt64_libdir}/libgstd3dshader-%{api_version}.dll.a
%{ucrt64_libdir}/libgstdxva-%{api_version}.dll.a
%{ucrt64_libdir}/libgsthip.dll.a
%{ucrt64_libdir}/libgstinsertbin-%{api_version}.dll.a
%{ucrt64_libdir}/libgstisoff-%{api_version}.dll.a
%{ucrt64_libdir}/libgstmpegts-%{api_version}.dll.a
%{ucrt64_libdir}/libgstmse-%{api_version}.dll.a
%{ucrt64_libdir}/libgstphotography-%{api_version}.dll.a
%{ucrt64_libdir}/libgstplay-%{api_version}.dll.a
%{ucrt64_libdir}/libgstplayer-%{api_version}.dll.a
%{ucrt64_libdir}/libgstsctp-%{api_version}.dll.a
%{ucrt64_libdir}/libgsttranscoder-%{api_version}.dll.a
%{ucrt64_libdir}/libgsturidownloader-%{api_version}.dll.a
%{ucrt64_libdir}/libgstwebrtc-%{api_version}.dll.a
%{ucrt64_libdir}/libgstcuda-%{api_version}.dll.a

%{ucrt64_libdir}/pkgconfig/gstreamer-analytics-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-bad-audio-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-codecparsers-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-hip-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-hip-gl-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-insertbin-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-mpegts-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-mse-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-photography-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-play-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-player-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-plugins-bad-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-sctp-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-transcoder-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-webrtc-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-cuda-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-d3d11-%{api_version}.pc
%{ucrt64_libdir}/pkgconfig/gstreamer-d3d12-%{api_version}.pc

%{ucrt64_datadir}/gstreamer-%{api_version}/presets/
%{ucrt64_datadir}/gstreamer-%{api_version}/encoding-profiles/

%{ucrt64_datadir}/locale


%changelog
* Sun Aug 09 2026 Sandro Mani <manisandro@gmail.com> - 1.28.6-1
- Update to 1.28.6

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jul 10 2026 Sandro Mani <manisandro@gmail.com> - 1.28.5-1
- Update to 1.28.5

* Mon Jun 15 2026 Sandro Mani <manisandro@gmail.com> - 1.28.4-1
- Update to 1.28.4

* Fri May 15 2026 Sandro Mani <manisandro@gmail.com> - 1.28.3-1
- Update to 1.28.3

* Wed Apr 15 2026 Sandro Mani <manisandro@gmail.com> - 1.28.2-2
- Rebuild (ucrt-gettext)

* Sun Apr 12 2026 Sandro Mani <manisandro@gmail.com> - 1.28.2-1
- Update to 1.28.2

* Sun Mar 01 2026 Sandro Mani <manisandro@gmail.com> - 1.28.1-1
- Update to 1.28.1

* Sat Jan 31 2026 Sandro Mani <manisandro@gmail.com> - 1.28.0-1
- Update to 1.28.0

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sat Jan 10 2026 Sandro Mani <manisandro@gmail.com> - 1.26.10-1
- Update to 1.26.10

* Sun Jan 04 2026 Sandro Mani <manisandro@gmail.com> - 1.26.9-2
- Rebuild (ucrt-openexr)

* Thu Dec 04 2025 Sandro Mani <manisandro@gmail.com> - 1.26.9-1
- Update to 1.26.9

* Sat Nov 15 2025 Sandro Mani <manisandro@gmail.com> - 1.26.8-1
- Update to 1.26.8

* Sun Oct 19 2025 Sandro Mani <manisandro@gmail.com> - 1.26.7-1
- Update to 1.26.7

* Tue Sep 16 2025 Sandro Mani <manisandro@gmail.com> - 1.26.6-1
- Update to 1.26.6

* Wed Aug 13 2025 Sandro Mani <manisandro@gmail.com> - 1.26.5-1
- Update to 1.26.5

* Mon Aug 11 2025 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.26.3-5
- Require DirectX headers

* Sun Aug 10 2025 Sandro Mani <manisandro@gmail.com> - 1.26.3-4
- Rebuild (imath)

* Wed Jul 30 2025 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.26.3-3
- Add d3d12 plugin

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jun 29 2025 Sandro Mani <manisandro@gmail.com> - 1.26.3-1
- Update to 1.26.3

* Sat May 31 2025 Sandro Mani <manisandro@gmail.com> - 1.26.2-1
- Update to 1.26.2

* Sun Apr 27 2025 Sandro Mani <manisandro@gmail.com> - 1.26.1-1
- Update to 1.26.1

* Tue Mar 18 2025 Sandro Mani <manisandro@gmail.com> - 1.26.0-1
- Update to 1.26.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Sandro Mani <manisandro@gmail.com> - 1.25.1-1
- Update to 1.25.1

* Mon Jan 13 2025 Sandro Mani <manisandro@gmail.com> - 1.24.11-1
- Update to 1.24.11

* Fri Dec 06 2024 Sandro Mani <manisandro@gmail.com> - 1.24.10-1
- Update to 1.24.10

* Wed Nov 27 2024 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.24.9-3
- Rebuild (openexr)

* Thu Nov 14 2024 Sandro Mani <manisandro@gmail.com> - 1.24.9-2
- Rebuild (openexr)

* Tue Nov 05 2024 Sandro Mani <manisandro@gmail.com> - 1.24.9-1
- Update to 1.24.9

* Mon Sep 23 2024 Sandro Mani <manisandro@gmail.com> - 1.24.8-1
- Update to 1.24.8

* Fri Aug 23 2024 Sandro Mani <manisandro@gmail.com> - 1.24.7-1
- Update to 1.24.7

* Tue Jul 30 2024 Sandro Mani <manisandro@gmail.com> - 1.24.6-1
- Update to 1.24.6

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 23 2024 Sandro Mani <manisandro@gmail.com> - 1.24.5-1
- Update to 1.24.5

* Tue Jun 11 2024 Sandro Mani <manisandro@gmail.com> - 1.24.4-2
- Rebuild (openexr)

* Thu Jun 06 2024 Sandro Mani <manisandro@gmail.com> - 1.24.4-1
- Update to 1.24.4

* Wed May 01 2024 Sandro Mani <manisandro@gmail.com> - 1.24.3-1
- Update to 1.24.3

* Thu Mar 07 2024 Sandro Mani <manisandro@gmail.com> - 1.24.0-1
- Update to 1.24.0

* Sat Jan 27 2024 Sandro Mani <manisandro@gmail.com> - 1.22.9-1
- Update to 1.22.9

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Sandro Mani <manisandro@gmail.com> - 1.22.8-1
- Update to 1.22.8

* Wed Nov 15 2023 Sandro Mani <manisandro@gmail.com> - 1.22.7-1
- Update to 1.22.7

* Thu Sep 21 2023 Sandro Mani <manisandro@gmail.com> - 1.22.6-1
- Update to 1.22.6

* Sat Jul 29 2023 Sandro Mani <manisandro@gmail.com> - 1.22.5-1
- Update to 1.22.5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Sandro Mani <manisandro@gmail.com> - 1.22.4-1
- Update to 1.22.4

* Thu May 25 2023 Sandro Mani <manisandro@gmail.com> - 1.22.3-1
- Update to 1.22.3

* Sat Apr 15 2023 Sandro Mani <manisandro@gmail.com> - 1.22.2-1
- Update to 1.22.2

* Sun Mar 19 2023 Sandro Mani <manisandro@gmail.com> - 1.22.1-1
- Update to 1.22.1

* Sat Jan 28 2023 Sandro Mani <manisandro@gmail.com> - 1.22.0-1
- Update to 1.22.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 13 2022 Sandro Mani <manisandro@gmail.com> - 1.20.4-1
- Update to 1.20.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 21 2022 Sandro Mani <manisandro@gmail.com> - 1.20.3-1
- Update to 1.20.3

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 1.20.0-4
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.20.0-3
- Rebuild with ucrt-gcc-12

* Thu Feb 17 2022 Sandro Mani <manisandro@gmail.com> - 1.19.3-3
- Rebuild (openssl)

* Sat Feb 05 2022 Sandro Mani <manisandro@gmail.com> - 1.20.0-1
- Update to 1.20.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 13 2021 Sandro Mani <manisandro@gmail.com> - 1.19.3-1
- Update to 1.19.3

* Sat Oct 02 2021 Sandro Mani <manisandro@gmail.com> - 1.19.2-1
- Update to 1.19.2

* Thu Aug 19 2021 Sandro Mani <manisandro@gmail.com> - 1.19.1-3
- Rebuild (openexr3)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Sandro Mani <manisandro@gmail.com> - 1.19.1-1
- Update to 1.19.1

* Wed Apr 14 2021 Michael Cronenworth <mike@cchtml.com> - 1.18.4-2
- Rebuild for Nettle 3.7.2

* Wed Mar 24 2021 Sandro Mani <manisandro@gmail.com> - 1.18.4-1
- Update to 1.18.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Sandro Mani <manisandro@gmail.com> - 1.18.2-2
- Rebuild (openexr)

* Thu Dec 10 2020 Sandro Mani <manisandro@gmail.com> - 1.18.2-1
- Update to 1.18.2

* Mon Nov 02 2020 Sandro Mani <manisandro@gmail.com> - 1.18.1-1
- Update to 1.18.1

* Wed Aug 12 13:38:11 GMT 2020 Sandro Mani <manisandro@gmail.com> - 1.16.2-3
- Rebuild (ucrt-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 1.16.2-1
- Update to 1.16.2

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
- Rebuild for new ucrt-openssl.

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
- Rebuilt for ucrt-gnutls 3.4 ABI change

* Mon Dec  1 2014 Victor Toso <victortoso@redhat.com> - 1.4.4-1
- Initial packaging.
  Resolves: rhbz#1166852
