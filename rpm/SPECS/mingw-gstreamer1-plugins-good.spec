%{?mingw_package_header}

%global         api_version     1.0

Name:           mingw-gstreamer1-plugins-good
Version:        1.18.3
Release:        1%{?dist}
Summary:        Cross compiled GStreamer1 plug-ins good

License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source:         http://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-orc
BuildRequires:  mingw64-orc
BuildRequires:  pkgconfig

# For glib-genmarshal
BuildRequires:  glib2-devel

BuildRequires:  mingw32-gstreamer1 >= %{version}
BuildRequires:  mingw64-gstreamer1 >= %{version}
BuildRequires:  mingw32-gstreamer1-plugins-base  >= %{version}
BuildRequires:  mingw64-gstreamer1-plugins-base  >= %{version}
BuildRequires:  mingw32-cairo
BuildRequires:  mingw64-cairo
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw32-libpng
BuildRequires:  mingw64-libpng
BuildRequires:  mingw32-libsoup
BuildRequires:  mingw64-libsoup
BuildRequires:  mingw32-wavpack
BuildRequires:  mingw64-wavpack
BuildRequires:  mingw32-speex
BuildRequires:  mingw64-speex

# Can't build with -Werror
# https://bugzilla.redhat.com/show_bug.cgi?id=1166306
#BuildRequires:  mingw32-taglib
#BuildRequires:  mingw64-taglib


%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.


# Mingw32
%package -n mingw32-gstreamer1-plugins-good
Summary:        %{summary}
Requires:       mingw32-gstreamer1 >= %{version}
Requires:       mingw32-gstreamer1-plugins-base >= %{version}

%description -n mingw32-gstreamer1-plugins-good
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.


# Mingw64
%package -n mingw64-gstreamer1-plugins-good
Summary:        %{summary}
Requires:       mingw64-gstreamer1 >= %{version}
Requires:       mingw64-gstreamer1-plugins-base >= %{version}

%description -n mingw64-gstreamer1-plugins-good
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.


%{?mingw_debug_package}


%prep
%setup -q -n gst-plugins-good-%{version}

%build
%mingw_meson --default-library=shared
%mingw_ninja

%install
%mingw_ninja_install

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gstreamer-%{api_version}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gstreamer-%{api_version}/*.la
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gstreamer-%{api_version}/*.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gstreamer-%{api_version}/*.a

%mingw_find_lang gstreamer1-plugins-good --all-name

# Mingw32
%files -n mingw32-gstreamer1-plugins-good -f mingw32-gstreamer1-plugins-good.lang
%license COPYING
%doc AUTHORS README REQUIREMENTS

# Equaliser presets
%{mingw32_datadir}/gstreamer-%{api_version}/presets/

# non-core plugins without external dependencies
%{mingw32_libdir}/gstreamer-%{api_version}/libgstalaw.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstalpha.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstalphacolor.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstapetag.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudiofx.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstaudioparsers.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstauparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstautodetect.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstavi.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcutter.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdebug.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdeinterlace.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdtmf.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsteffectv.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstequalizer.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstflv.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstflxdec.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgoom.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgoom2k1.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsticydemux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstid3demux.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstimagefreeze.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstinterleave.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstisomp4.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstlevel.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmatroska.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmulaw.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmultifile.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmultipart.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstnavigationtest.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstreplaygain.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrtp.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrtpmanager.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstrtsp.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstshapewipe.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsmpte.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstspectrum.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstspeex.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgtk.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstudp.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideobox.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideocrop.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideofilter.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstvideomixer.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwaveform.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwavenc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwavpack.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstwavparse.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgsty4menc.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstmonoscope.dll

# gstreamer1-plugins with external dependencies but in the main package
%{mingw32_libdir}/gstreamer-%{api_version}/libgstcairo.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstdirectsound.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstgdkpixbuf.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstjpeg.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstpng.dll
%{mingw32_libdir}/gstreamer-%{api_version}/libgstsoup.dll


# Mingw64
%files -n mingw64-gstreamer1-plugins-good -f mingw64-gstreamer1-plugins-good.lang
%license COPYING
%doc AUTHORS README REQUIREMENTS

# Equaliser presets
%{mingw64_datadir}/gstreamer-%{api_version}/presets/

# non-core plugins without external dependencies
%{mingw64_libdir}/gstreamer-%{api_version}/libgstalaw.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstalpha.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstalphacolor.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstapetag.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudiofx.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstaudioparsers.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstauparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstautodetect.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstavi.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcutter.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdebug.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdeinterlace.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdtmf.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsteffectv.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstequalizer.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstflv.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstflxdec.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgoom.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgoom2k1.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsticydemux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstid3demux.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstimagefreeze.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstinterleave.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstisomp4.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstlevel.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmatroska.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmulaw.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmultifile.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmultipart.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstnavigationtest.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstreplaygain.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrtp.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrtpmanager.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstrtsp.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstshapewipe.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsmpte.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstspectrum.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstspeex.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgtk.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstudp.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideobox.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideocrop.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideofilter.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstvideomixer.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwaveform.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwavenc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwavpack.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstwavparse.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgsty4menc.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstmonoscope.dll


# gstreamer1-plugins with external dependencies but in the main package
%{mingw64_libdir}/gstreamer-%{api_version}/libgstcairo.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstdirectsound.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstgdkpixbuf.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstjpeg.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstpng.dll
%{mingw64_libdir}/gstreamer-%{api_version}/libgstsoup.dll


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.14.1-4
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Victor Toso <victortoso@redhat.com> - 1.14.1-1
- Update to 1.14.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 1.12.3-1
- Update to 1.12.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 1.12.1-1
- Update to 1.12.1

* Tue Feb  7 2017 Victor Toso <victortoso@redhat.com> - 1.11.1-1
- Update to 1.11.1
- Fixes: CVE-2016-10198, CVE-2016-10199
- Fixes: CVE-2017-5840
- Fixes: CVE-2017-5841
- Fixes: CVE-2017-5845

* Sat Nov  5 2016 Victor Toso <victortoso@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Thu May 12 2016 Kalev Lember <klember@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 26 2015 Kalev Lember <klember@redhat.com> - 1.6.0-1
- Update to 1.6.0
- Use license macro for COPYING

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
- Add gdk-pixbuf build requirement. Resolves: rhbz#1239681

* Mon Dec  8 2014 Victor Toso <victortoso@redhat.com> - 1.4.4-1
- Initial packaging.
  Resolves: rhbz#1166697
