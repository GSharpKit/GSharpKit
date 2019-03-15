%{?mingw_package_header}

%global mingw_pkg_name webkitgtk3-sharp
%global mingw_build_win32 1
%global mingw_build_win64 1

%define libdir /bin
%define debug_package %{nil}

Name:		mingw-webkitgtk3-sharp
Version:	2.4.11
Release:	2%{?dist}
Summary:	.NET bindings for WebKit
Group:		Development/Languages
License:	MIT
URL:		http://ftp.novell.com/pub/mono/sources/webkit-sharp/
Source0:        webkitgtk3-sharp-%{version}.tar.xz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	mingw32-webkitgtk3
BuildRequires:	mingw64-webkitgtk3

BuildRequires:	webkitgtk3-devel
BuildRequires:	mono-devel
BuildRequires:	gtk-sharp3-devel
BuildRequires:	gtk-sharp3-gapi
BuildRequires:	monodoc-devel

%description
WebKit-sharp is .NET bindings for the WebKit rendering engine.


# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw32-glib2
Requires:       mingw32-webkitgtk3

%description -n mingw32-%{mingw_pkg_name}
WebKit-sharp is .NET bindings for the WebKit rendering engine.


# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw64-glib2
Requires:       mingw64-webkitgtk3

%description -n mingw64-%{mingw_pkg_name}
WebKit-sharp is .NET bindings for the WebKit rendering engine.


%prep
%setup -q -n webkitgtk3-sharp-%{version}

%build
sh autogen.sh --prefix=/usr
make distclean

%install
%{__rm} -rf %{buildroot}
MINGW32_PKG_CONFIG=/usr/pkg-config %mingw32_configure
%mingw32_make
%mingw32_make install DESTDIR=%{buildroot}
%mingw32_make clean

MINGW64_PKG_CONFIG=/usr/pkg-config %mingw64_configure
%mingw64_make
%mingw64_make install DESTDIR=%{buildroot}


# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 $RPM_BUILD_ROOT%{mingw32_libdir}/mono/gac/webkitgtk3-sharp/*/*.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/

sed -i -e 's!/usr/i686-w64-mingw32/sys-root/mingw/lib!/usr/i686-w64-mingw32/sys-root/mingw/bin!' $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/webkitgtk3-sharp-3.0.pc
sed -i -e 's!/mono/webkitgtk3-sharp!!' $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/webkitgtk3-sharp-3.0.pc

rm -rf $RPM_BUILD_ROOT%{mingw32_libdir}

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 $RPM_BUILD_ROOT%{mingw64_libdir}/mono/gac/webkitgtk3-sharp/*/*.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/

sed -i -e 's!/usr/x86_64-w64-mingw32/sys-root/mingw/lib!/usr/x86_64-w64-mingw32/sys-root/mingw/bin!' $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/webkitgtk3-sharp-3.0.pc
sed -i -e 's!/mono/webkitgtk3-sharp!!' $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/webkitgtk3-sharp-3.0.pc

rm -rf $RPM_BUILD_ROOT%{mingw64_libdir}

%clean
%{__rm} -rf %{buildroot}


%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/webkitgtk3-sharp.dll
%{mingw32_datadir}/pkgconfig/webkitgtk3-sharp-3.0.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/webkitgtk3-sharp.dll
%{mingw64_datadir}/pkgconfig/webkitgtk3-sharp-3.0.pc


%changelog
* Wed Mar 02 2012 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.4.1-2
- Remove 'webkit-1.0/webkit/WebKitDOMHTMLIsIndexElement.h' it fails to 
- register on windows.

* Sat Feb 21 2009 David Nielsen <gnomeuser@gmail.com> - 0.2-1
- Initial package
