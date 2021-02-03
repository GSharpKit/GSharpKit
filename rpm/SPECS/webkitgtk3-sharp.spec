%define		debug_package %{nil}

Name:		webkitgtk3-sharp
Version:	2.4.12
Release:	1%{?dist}
Summary:	.NET bindings for WebKit
Group:		Development/Languages
License:	MIT
URL:		http://ftp.novell.com/pub/mono/sources/webkit-sharp/
Source0:        webkitgtk3-sharp-%{version}.tar.xz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	webkitgtk3-devel >= %{version}
BuildRequires:	mono-devel
BuildRequires:	GtkSharp-gapi >= 3.24.24
BuildRequires:	monodoc-devel

Obsoletes:	webkit-sharp
Provides:	webkit-sharp = %{version}-%{release}

Requires:	webkitgtk3 >= %{version}
Requires:	GtkSharp >= 3.24.24

Provides:	webkitgtk3-sharp-devel

%description
webkitgtk-sharp is .NET bindings for the WebKit rendering engine.

%prep
%setup -q

%build
sh autogen.sh --prefix=/usr
# parallel build fails in mock
touch sources/generated-stamp
sed -i -e 's!webkitgtk-3.0!libwebkitgtk-3.0.so.0!g' sources/webkitgtk3-sharp-api.raw
make

%install
%{__rm} -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}/lib/webkitgtk3-sharp.dll
%{_datadir}/pkgconfig/webkitgtk3-sharp-3.0.pc

%changelog
* Fri Nov 5 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.4.11-1
- Updated to 2.4.11

* Sat May 5 2013 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.1-1
- Updated to 2.0.1 and moved to own git

* Sat Jan 5 2013 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.4.0-1
- Initial package
