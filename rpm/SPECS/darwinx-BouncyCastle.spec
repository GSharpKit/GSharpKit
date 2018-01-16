%global debug_package %{nil}

%define libdir /lib

Name:           darwinx-BouncyCastle
Version:        1.8.1
Release:        1%{?dist}
Summary:        BouncyCastle is a Crypto library written i C#

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/
Prefix:		/usr

BuildArch:	noarch

Requires:	darwinx-mono-core >= 4.8

%description
BouncyCastle is a Crypto library written i C#

%prep
%setup -q -T -c BouncyCastle-%{version}
nuget install BouncyCastle -Version %{version}

cat > BouncyCastle.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}/mono

Name: BouncyCastle
Description: BouncyCastle is a Crypto library written i C# 
Requires:
Version: %{version}
Libs: -r:${libdir}/BouncyCastle.Crypto/BouncyCastle.Crypto.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/mono/gac
gacutil -i BouncyCastle.%{version}/lib/BouncyCastle.Crypto.dll -package BouncyCastle.Crypto -root $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 BouncyCastle.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/mono/gac
%{_darwinx_prefix}%{libdir}/mono/BouncyCastle.Crypto/BouncyCastle.Crypto.dll
%{_darwinx_datadir}/pkgconfig/BouncyCastle.pc


%changelog
* Wed Jul 02 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5-1
- Initial version
