%global debug_package %{nil}

%define libdir /lib

Name:           darwinx-BouncyCastle
Version:        1.9.0
Release:        1%{?dist}
Summary:        BouncyCastle is a Crypto library written i C#

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/
Prefix:		/usr

BuildArch:	noarch

%description
BouncyCastle is a Crypto library written i C#

%prep
%setup -q -T -c BouncyCastle-%{version}
nuget install Portable.BouncyCastle -Version %{version}

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 Portable.BouncyCastle.%{version}/lib/netstandard2.0/BouncyCastle.Crypto.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/BouncyCastle.Crypto.dll


%changelog
* Wed Jul 02 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5-1
- Initial version
