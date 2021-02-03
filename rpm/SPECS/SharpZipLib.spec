%define libdir /lib
%define api_version 1.0.0.999

Name:		SharpZipLib
Version:	1.3.1
Release:	1%{?dist}
Summary:	SharpZipLib (#ziplib, formerly NZipLib) is a compression library for Zip, GZip, BZip2
Group:		Development/Languages
License:	MIT
URL:		https://www.nuget.org/packages/SharpZipLib
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr

BuildArch: 	noarch

Requires:	mono-core >= 5.14.0
BuildRequires:	nuget

%description
SharpZipLib (#ziplib, formerly NZipLib) is a compression library for Zip, GZip, 
BZip2, and Tar written entirely in C# for .NET. It is implemented as an assembly 
(installable in the GAC), and thus can easily be incorporated into other projects 
(in any .NET language)

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > %{name}.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: %{name}
Description: %{summary}
Requires:
Version: %{api_version}
Libs: -r:${libdir}/ICSharpCode.%{name}.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 %{name}.%{version}/lib/netstandard2.0/ICSharpCode.%{name}.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 %{name}.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/ICSharpCode.%{name}.dll
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Thu Nov 13 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.0.0-1
- Initial build

