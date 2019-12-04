%global debug_package %{nil}

%define libdir /lib
%define pkg_name Digst.OioIdws.Rest.Client

Name:           Digst.OioIdws.Rest.Client
Version:        3.0.0
Release:        1%{?dist}
Summary:        Digst.OioIdws.Rest.Client is a .Net-based reference implementation

Group:          Development/Languages
License:        Mozilla Public License Version 1.1
URL:            https://svn.softwareborsen.dk/OIOIDWS/trunk/
Prefix:		/usr
BuildArch:	noarch

Provides:	mono(Newtonsoft.Json) = 7.0.0.0

%description
Digst.OioIdws.Rest.Client is a .Net-based reference implementation of the 
OIOIDWS REST 1.1 profile. The Toolkit can be used by services to act as a
Web Service Client (WSC)

%prep
%setup -c %{name}-%{version} -T
nuget install %{pkg_name} -Version %{version}
nuget install Digst.OioIdws.Wsc -Version %{version}

cat > %{pkg_name}.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: %{pkg_name}
Description: Digst.OioIdws.Rest.Client is a .Net-based reference implementation
Requires: Newtonsoft.Json
Version: %{version}
Libs: -r:${libdir}/Side.dll -r:${libdir}/Digst.OioIdws.Common.dll -r:${libdir}/Digst.OioIdws.OioWsTrust.dll -r:${libdir}/Digst.OioIdws.Rest.Common.dll -r:${libdir}/Digst.OioIdws.Rest.Client.dll -r:${libdir}/Digst.OioIdws.Wsc.dll -r:${libdir}/Digst.OioIdws.Soap.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}

cp Digst.OioIdws.Rest.Client.%{version}/lib/net45/Digst.OioIdws.Common.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
cp Digst.OioIdws.Rest.Client.%{version}/lib/net45/Digst.OioIdws.OioWsTrust.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
cp Digst.OioIdws.Rest.Client.%{version}/lib/net45/Digst.OioIdws.Rest.Common.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
cp Digst.OioIdws.Rest.Client.%{version}/lib/net45/Digst.OioIdws.Rest.Client.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}

cp Digst.OioIdws.Wsc.%{version}/lib/net45/Digst.OioIdws.Wsc.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
cp Digst.OioIdws.Wsc.%{version}/lib/net45/Digst.OioIdws.Soap.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 %{pkg_name}.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/*.dll
%{_datadir}/pkgconfig/%{pkg_name}.pc

%changelog
* Wed Nov 27 2019 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.0.0
- Initial version
