%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name DBusSharp 
%global mingw_build_win32 0
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:			mingw-DBusSharp
Epoch: 			3
Version:		0.10.1
Release:		1%{?dist}
Summary:		Managed C# implementation of DBus
License:		MIT
Group:			System Environment/Libraries
URL:			http://www.ndesk.org/DBusSharp
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:			/usr

BuildArch: 		noarch

BuildRequires:		nuget

Obsoletes:              mingw64-dbus-sharp >= 0.1

Requires:		System.Common >= 1.0.1
Requires:		System.Security >= 6.0.0

%description
Managed C# implementation of DBus

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
AutoReqProv:    no

%description -n mingw64-%{mingw_pkg_name}
Managed C# implementation of DBus

%prep
%setup -c %{name}-%{version} -T
nuget install Tmds.DBus -Version %{version}

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 Tmds.DBus.%{version}/lib/netstandard2.0/Tmds.DBus.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}/%{libdir}/Tmds.DBus.dll

%changelog
* Sun Jan 16 2022 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.9.1-1
- Update to Tmds.DBus

