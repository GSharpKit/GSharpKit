Name:           darwinx-libtiff
Version:        4.0.3
Release:        1%{?dist}
Summary:        libtiff is the official TIFF reference library.

License:        LGPLv2+
Group:          Development/Libraries
URL:            ftp://ftp.remotesensing.org/pub/libtiff/
Source0:        tiff-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 4
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext


%description
libtiff is the official TIFF reference library.

%package static
Summary:        libtiff is the official TIFF reference library.
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Static version of the libtiff library.

%prep
%setup -q -n tiff-%{version}


%build
%{_darwinx_configure}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_darwinx_bindir}/bmp2tiff
%{_darwinx_bindir}/fax2tiff
%{_darwinx_bindir}/pal2rgb
%{_darwinx_bindir}/ras2tiff
%{_darwinx_bindir}/rgb2ycbcr
%{_darwinx_bindir}/tiff2bw
%{_darwinx_bindir}/tiff2ps
%{_darwinx_bindir}/tiffcmp
%{_darwinx_bindir}/tiffcrop
%{_darwinx_bindir}/tiffdump
%{_darwinx_bindir}/tiffmedian
%{_darwinx_bindir}/tiffsplit
%{_darwinx_bindir}/fax2ps
%{_darwinx_bindir}/gif2tiff
%{_darwinx_bindir}/ppm2tiff
%{_darwinx_bindir}/raw2tiff
%{_darwinx_bindir}/thumbnail
%{_darwinx_bindir}/tiff2pdf
%{_darwinx_bindir}/tiff2rgba
%{_darwinx_bindir}/tiffcp
%{_darwinx_bindir}/tiffdither
%{_darwinx_bindir}/tiffinfo
%{_darwinx_bindir}/tiffset
%{_darwinx_libdir}/libtiff.dylib
%{_darwinx_libdir}/libtiff.*.dylib
%{_darwinx_libdir}/libtiff.la
%{_darwinx_libdir}/libtiffxx.dylib
%{_darwinx_libdir}/libtiffxx.*.dylib
%{_darwinx_libdir}/libtiffxx.la
%{_darwinx_libdir}/pkgconfig/libtiff-4.pc
%{_darwinx_includedir}/tiff.h
%{_darwinx_includedir}/tiffconf.h
%{_darwinx_includedir}/tiffio.h
%{_darwinx_includedir}/tiffio.hxx
%{_darwinx_includedir}/tiffvers.h

%files static
%defattr(-,root,root)
%{_darwinx_libdir}/libtiff.a
%{_darwinx_libdir}/libtiffxx.a

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.0.13-1
- Initial RPM release
