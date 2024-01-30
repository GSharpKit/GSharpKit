Name:           darwinx-hunspell
Version:        1.7.2
Release:        1%{?dist}
Summary:        Hunspell is a free spell checker and morphological analyzer library and command-line tool
License:        LGPL/GPL/MPL tri-license
Group:          Development/Libraries
URL:            https://github.com/hunspell/hunspell/archive/refs/tags/v%{version}.tar.gz
Source0:        hunspell-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 12
BuildRequires:  darwinx-gcc

BuildRequires:  pkgconfig

%description
Hunspell is used by LibreOffice office suite, free browsers, like Mozilla Firefox and Google Chrome, 
and other tools and OSes, like Linux distributions and macOS. It is also a command-line tool 
for Linux, Unix-like and other OSes.

It is designed for quick and high quality spell checking and correcting for languages with 
word-level writing system, including languages with rich morphology, complex word 
compounding and character encoding.


%prep
%setup -q -n hunspell-%{version}

%build
%{_darwinx_configure} \
	--disable-static \
	--disable-nls \
	--without-ui \
	--without-readline

%{_darwinx_make} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%{_darwinx_bindir}/*
%{_darwinx_libdir}/libhunspell-*.dylib
%{_darwinx_libdir}/pkgconfig/hunspell.pc
%{_darwinx_includedir}/

%changelog
* Thu May  9 2013 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.6.0-1
- Initial RPM release.

