%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define libdir /lib
%define api_version 4.7.0.0

Name:           Microsoft.CSharp
Version:        4.7.0
Release:        1%{?dist}
Summary:        Provides support for compilation and code generation, including dynamic, using the C# language.

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/Microsoft.CSharp
Prefix:		/usr
BuildArch:	noarch

Requires:	mono-core >= 5.0.0

%description
Provides support for compilation and code generation, including dynamic, using the C# language.

Commonly Used Types:
Microsoft.CSharp.RuntimeBinder.Binder
Microsoft.CSharp.RuntimeBinder.RuntimeBinderException
Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo
Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfoFlags
Microsoft.CSharp.RuntimeBinder.CSharpBinderFlags


%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > Microsoft.CSharp.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: Microsoft.CSharp
Description: Provides support for compilation and code generation, including dynamic, using the C# language.
Requires:
Version: %{api_version}
Libs: -r:${libdir}/Microsoft.CSharp.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 Microsoft.CSharp.%{version}/lib/netstandard2.0/Microsoft.CSharp.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 Microsoft.CSharp.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/Microsoft.CSharp.dll
%{_datadir}/pkgconfig/Microsoft.CSharp.pc


%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version
