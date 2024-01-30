Name:           darwinx-libvorbis
Version:        1.3.7
Release:        1%{?dist}
Summary:        The Vorbis General Audio Compression Codec.
License:        BSD
Group:          Development/Libraries
URL:            http://www.xiph.org/downloads/
Source:         http://downloads.xiph.org/releases/vorbis/libvorbis-%{version}.tar.xz
Patch0:		libvorbis-1.3.7-clang-cputype.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc

BuildRequires:  darwinx-libogg

%description
Ogg Vorbis is a fully open, non-proprietary, patent- and royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

The libvorbis package contains runtime libraries for use in programs
that support Ogg Vorbis.

%prep
%setup -q -n libvorbis-%{version}
%patch 0 -p1

%build
%{_darwinx_configure} \
	--disable-static \
	--disable-oggtest

%{_darwinx_make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{_darwinx_make} DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%{_darwinx_libdir}/libvorbis*.dylib
%dir %{_darwinx_includedir}/vorbis
%{_darwinx_includedir}/vorbis/*.h
%{_darwinx_libdir}/pkgconfig/*.pc

%changelog
