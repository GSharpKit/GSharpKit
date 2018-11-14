%define libdir /lib
%define api_version 1.0.0.0

Name:		Mono.Addins.Setup
Version:	1.3.8
Release:	1%{?dist}
Summary:	Addins for mono
Group:		Development/Languages
License:	MIT
URL:		https://www.nuget.org/packages/Mono.Addins.Setup
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr

BuildArch: 	noarch

Requires:	mono-core >= 5.14.0
Requires:	SharpZipLib >= 1.0.0
BuildRequires:	nuget

%description
Mono.Addins is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > mono-addins-setup.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}/mono

Name: %{name}
Description: Addins Setup for mono
Requires:
Version: %{api_version}
Libs: -r:${libdir}/%{name}/%{name}.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono/gac
gacutil -i %{name}.%{version}/lib/net45/%{name}.dll -package %{name} -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 mono-addins-setup.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/mono/gac
%{_prefix}%{libdir}/mono/%{name}/%{name}.dll
%{_datadir}/pkgconfig/mono-addins-setup.pc

%changelog
* Thu Nov 13 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.3.8-1
- Initial build

