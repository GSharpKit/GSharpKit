%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define libdir /lib
%define api_version 5.0.0.0

Name:           System.ComponentModel.Annotations
Version:        5.0.0
Release:        1%{?dist}
Summary:        Provides attributes that are used to define metadata for objects used as data sources.

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/System.ComponentModel.Annotations
Prefix:		/usr
BuildArch:	noarch

%description
Provides attributes that are used to define metadata for objects used as data sources.

Commonly Used Types:
System.ComponentModel.DataAnnotations.ValidationResult
System.ComponentModel.DataAnnotations.IValidatableObject
System.ComponentModel.DataAnnotations.ValidationAttribute
System.ComponentModel.DataAnnotations.RequiredAttribute
System.ComponentModel.DataAnnotations.StringLengthAttribute
System.ComponentModel.DataAnnotations.DisplayAttribute
System.ComponentModel.DataAnnotations.RegularExpressionAttribute
System.ComponentModel.DataAnnotations.DataTypeAttribute
System.ComponentModel.DataAnnotations.RangeAttribute
System.ComponentModel.DataAnnotations.KeyAttribute

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > %{name}.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: %{name}
Description: Provides attributes that are used to define metadata for objects used as data sources. 
Requires:
Version: %{api_version}
Libs: -r:${libdir}/%{name}.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 %{name}.%{version}/lib/netstandard2.0/%{name}.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 %{name}.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/%{name}.dll
%{_datadir}/pkgconfig/%{name}.pc


%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version
