Name:           darwinx-libwebp
Version:        1.2.0
Release:        1%{?dist}
Summary:        Library and tools for the WebP graphics format
License:        BSD
Group:          Development/Libraries
URL:            http://webmproject.org/
Source0:        libwebp-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc

%description
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%prep
%setup -q -n libwebp-%{version}

%build
#sh autogen.sh
%{_darwinx_configure} --disable-static --disable-assembly  --enable-libwebpdecoder
%{_darwinx_make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install program_transform_name=""

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
%{_darwinx_bindir}/cwebp
%{_darwinx_bindir}/dwebp
%{_darwinx_includedir}/webp
%{_darwinx_libdir}/libwebp.*.dylib
%{_darwinx_libdir}/libwebp.dylib
%{_darwinx_libdir}/libwebp.la
%{_darwinx_libdir}/libwebpdecoder.*.dylib
%{_darwinx_libdir}/libwebpdecoder.dylib
%{_darwinx_libdir}/libwebpdecoder.la
%{_darwinx_libdir}/libwebpdemux.*.dylib
%{_darwinx_libdir}/libwebpdemux.dylib
%{_darwinx_libdir}/libwebpdemux.la
%{_darwinx_libdir}/pkgconfig/libwebp.pc
%{_darwinx_libdir}/pkgconfig/libwebpdecoder.pc
%{_darwinx_libdir}/pkgconfig/libwebpdemux.pc

%changelog
* Thu May  9 2013 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.4.2-1
- Initial RPM release.
