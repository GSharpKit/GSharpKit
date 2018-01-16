Name:		darwinx-webkitgtk3-sharp
Version:	2.4.11
Release:	1%{?dist}
Summary:	.NET bindings for WebKit
Group:		Development/Languages
License:	MIT
URL:		http://ftp.novell.com/pub/mono/sources/webkit-sharp/
Source0:        webkitgtk3-sharp-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

BuildRequires:	darwinx-webkitgtk3 >= %{version}
BuildRequires:	darwinx-mono-core
BuildRequires:	darwinx-GtkSharp >= 3.14.0

Requires:  	darwinx-webkitgtk3 >= %{version}
Requires:  	darwinx-mono-core
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
%{_darwinx_makeinstall}

%clean
#{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_libdir}/mono/
%{_darwinx_datadir}/pkgconfig/webkitgtk3-sharp-3.0.pc
%{_darwinx_libdir}/monodoc/sources/webkitgtk3-sharp*

%changelog
* Sat Feb 21 2009 David Nielsen <gnomeuser@gmail.com> - 0.2-1
- Initial package
