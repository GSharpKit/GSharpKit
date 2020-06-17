Name:           darwinx-libvorbis
Version:        1.3.6
Release:        1%{?dist}
Summary:        The Vorbis General Audio Compression Codec.
License:        BSD
Group:          Development/Libraries
URL:            http://www.xiph.org/downloads/
Source:         http://downloads.xiph.org/releases/vorbis/libvorbis-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

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


%build
%{_darwinx_configure}
%{_darwinx_make}

%install
rm -rf $RPM_BUILD_ROOT

%{_darwinx_make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_darwinx_libdir}
%{_darwinx_includedir}
%{_darwinx_datadir}

%changelog
