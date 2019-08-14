Name:		darwinx-webkitgtk3-sharp
Version:	2.4.11
Release:	2%{?dist}
Summary:	.NET bindings for WebKit
Group:		Development/Languages
License:	MIT
URL:		http://ftp.novell.com/pub/mono/sources/webkit-sharp/
Source0:        webkitgtk3-sharp-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

BuildRequires:	darwinx-webkitgtk3 >= %{version}
BuildRequires:	darwinx-GtkSharp >= 3.14.0
BuildRequires:	darwinx-mono-core

Requires:  	darwinx-webkitgtk3 >= %{version}
Requires:  	darwinx-GtkSharp >= 3.14.0

%description
WebKit-sharp is .NET bindings for the WebKit rendering engine.

%prep
%setup -q -n webkitgtk3-sharp-%{version}

%build
autoreconf --verbose --install -I /usr/darwinx/usr/share/aclocal
%{_darwinx_configure}

# parallel build fails in mock
%{_darwinx_make}

%install
%{__rm} -rf %{buildroot}

mkdir -p $RPM_BUILD_ROOT%{_darwinx_libdir}
cp sources/webkitgtk3-sharp.dll $RPM_BUILD_ROOT%{_darwinx_libdir}/
cp sources/webkitgtk3-sharp.dll.config $RPM_BUILD_ROOT%{_darwinx_libdir}/

mkdir -p $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
cp sources/webkitgtk3-sharp-3.0.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
sed -i '' 's!mono/webkitgtk3-sharp/!!g' $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/webkitgtk3-sharp-3.0.pc

%clean
#{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_libdir}/webkitgtk3-sharp.dll
%{_darwinx_libdir}/webkitgtk3-sharp.dll.config
%{_darwinx_datadir}/pkgconfig/webkitgtk3-sharp-3.0.pc

%changelog
* Sat Feb 21 2009 David Nielsen <gnomeuser@gmail.com> - 0.2-1
- Initial package
