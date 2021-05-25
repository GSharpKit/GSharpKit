%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name PdfSharp.MigraDoc 
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin
%define apiversion 1.50.0.0

Name:           mingw-PdfSharp.MigraDoc
Version:        1.51.15
Release:        1%{?dist}
Summary:        .NET library that easily creates documents and renders them into PDF or RTF.

Group:          Development/Languages
License:        MIT
URL:            http://www.pdfsharp.net
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  nuget


%description
MigraDoc Foundation - the Open Source .NET library that easily creates documents based on an 
object model with paragraphs, tables, styles, etc. and renders them into PDF or RTF.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
Obsoletes:     mingw32-PDFsharp-MigraDoc

%description -n mingw32-%{mingw_pkg_name}
MigraDoc Foundation - the Open Source .NET library that easily creates documents based on an
object model with paragraphs, tables, styles, etc. and renders them into PDF or RTF.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Obsoletes:     mingw64-PDFsharp-MigraDoc

%description -n mingw64-%{mingw_pkg_name}
MigraDoc Foundation - the Open Source .NET library that easily creates documents based on an
object model with paragraphs, tables, styles, etc. and renders them into PDF or RTF.

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name}.Standard -Version %{version}
nuget install System.Drawing.Common -Version 5.0.2
nuget install System.Resources.Extensions -Version 5.0.0

cat > %{mingw_pkg_name}32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}

Name: %{mingw_pkg_name}
Description: %{mingw_pkg_name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/PdfSharp.dll -r:${libdir}/PdfSharp.Charting.dll -r:${libdir}/MigraDoc.Rendering.dll -r:${libdir}/MigraDoc.DocumentObjectModel.dll -r:${libdir}/System.Drawing.Common.dll -r:${libdir}/System.Resources.Extensions.dll
Cflags:
EOF

cat > %{mingw_pkg_name}64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: %{mingw_pkg_name}
Description: %{mingw_pkg_name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/PdfSharp.dll -r:${libdir}/PdfSharp.Charting.dll -r:${libdir}/MigraDoc.Rendering.dll -r:${libdir}/MigraDoc.DocumentObjectModel.dll -r:${libdir}/System.Drawing.Common.dll -r:${libdir}/System.Resources.Extensions.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 PdfSharp.MigraDoc.Standard.DocumentObjectModel.%{version}/lib/netstandard2.0/MigraDoc.DocumentObjectModel.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 PdfSharp.MigraDoc.Standard.%{version}/lib/netstandard2.0/MigraDoc.Rendering.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 PDFSharp.Standard.Charting.%{version}/lib/netstandard2.0/PdfSharp.Charting.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 PDFSharp.Standard.%{version}/lib/netstandard2.0/PdfSharp.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 System.Drawing.Common.5.0.2/lib/netstandard2.0/System.Drawing.Common.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 System.Resources.Extensions.5.0.0/lib/netstandard2.0/System.Resources.Extensions.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 %{mingw_pkg_name}32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/%{mingw_pkg_name}.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 PdfSharp.MigraDoc.Standard.DocumentObjectModel.%{version}/lib/netstandard2.0/MigraDoc.DocumentObjectModel.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 PdfSharp.MigraDoc.Standard.%{version}/lib/netstandard2.0/MigraDoc.Rendering.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 PDFSharp.Standard.Charting.%{version}/lib/netstandard2.0/PdfSharp.Charting.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 PDFSharp.Standard.%{version}/lib/netstandard2.0/PdfSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 System.Drawing.Common.5.0.2/lib/netstandard2.0/System.Drawing.Common.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 System.Resources.Extensions.5.0.0/lib/netstandard2.0/System.Resources.Extensions.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 %{mingw_pkg_name}64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/%{mingw_pkg_name}.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/MigraDoc.DocumentObjectModel.dll
%{mingw32_prefix}%{libdir}/MigraDoc.Rendering.dll
%{mingw32_prefix}%{libdir}/PdfSharp.Charting.dll
%{mingw32_prefix}%{libdir}/PdfSharp.dll
%{mingw32_prefix}%{libdir}/System.Drawing.Common.dll
%{mingw32_prefix}%{libdir}/System.Resources.Extensions.dll
%{mingw32_datadir}/pkgconfig/%{mingw_pkg_name}.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/MigraDoc.DocumentObjectModel.dll
%{mingw64_prefix}%{libdir}/MigraDoc.Rendering.dll
%{mingw64_prefix}%{libdir}/PdfSharp.Charting.dll
%{mingw64_prefix}%{libdir}/PdfSharp.dll
%{mingw64_prefix}%{libdir}/System.Drawing.Common.dll
%{mingw64_prefix}%{libdir}/System.Resources.Extensions.dll
%{mingw64_datadir}/pkgconfig/%{mingw_pkg_name}.pc

%changelog
* Thu Aug 02 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.50.4845-RC2a-1
- Update to 1.50.4845-RC2a

* Thu Jan 4 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.50.4740-beta5-1
- Initial version
