%global debug_package %{nil}

%define libdir /lib

Name:           PushSharp
Version:        4.0.10
Release:        1%{?dist}
Summary:        A Library for Sending Server Side Push Notifications.

Group:          Development/Languages
License:        MIT
URL:            https://github.com/Redth/PushSharp
Source0:        PushSharp-%{version}.tar.gz
#Patch0:	PushSharp-2.2.1.0-nuget.patch
Prefix:		/usr
BuildArch:	noarch

BuildRequires:	Newtonsoft.Json
BuildRequires:	nuget

Requires:	Newtonsoft.Json

%description
A Library for Sending Server Side Push Notifications to iOS (iPhone/iPad APNS), 
Android (C2DM), Windows Phone, and Blackberry devices! 

%prep
%setup -q -n PushSharp-%{version}
#patch0 -p1 

cat > PushSharp.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: PushSharp
Description: A Library for Sending Server Side Push Notifications.
Requires: Newtonsoft.Json
Version: 4.0.0.0
Libs: -r:${libdir}/PushSharp.Core.dll -r:${libdir}/PushSharp.Apple.dll -r:${libdir}/PushSharp.Google.dll -r:${libdir}/PushSharp.Windows.dll
Cflags:
EOF

%build

%{__rm} -f .nuget/NuGet.targets

xbuild /tv:4.0 /p:Configuration=Release PushSharp.sln

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 PushSharp.Core/bin/Release/*.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 PushSharp.Core/bin/Release/*.dll.mdb $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 PushSharp.Apple/bin/Release/*.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 PushSharp.Apple/bin/Release/*.dll.mdb $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 PushSharp.Google/bin/Release/*.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 PushSharp.Google/bin/Release/*.dll.mdb $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 PushSharp.Windows/bin/Release/*.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 PushSharp.Windows/bin/Release/*.dll.mdb $RPM_BUILD_ROOT%{_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 PushSharp.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.md README.md
%{_prefix}%{libdir}/*.dll
%{_prefix}%{libdir}/*.dll.mdb
%{_datadir}/pkgconfig/PushSharp.pc


%changelog
* Sat Dec 23 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.2.1.0-1
- Update to 2.2.1

* Sat Dec 29 2012 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 1.0.18-1
- Initial version
