%global debug_package %{nil}

%define darwinx_pkg_name PdfSsharp.MigraDoc
%define libdir /lib

Name:           darwinx-PdfSharp.MigraDoc
Version:        1.51.15
Release:        1%{?dist}
Summary:        .NET library that easily creates documents and renders them into PDF or RTF.

Group:          Development/Languages
License:        MIT
URL:            http://www.pdfsharp.net
Prefix:		/usr

BuildArch:	noarch

Obsoletes:	darwinx-PDFsharp-MigraDoc >= 0
Provides:	darwinx-PDFsharp-MigraDoc

%description
MigraDoc Foundation - the Open Source .NET library that easily creates documents based on an 
object model with paragraphs, tables, styles, etc. and renders them into PDF or RTF.

%prep
%setup -c %{name}-%{version} -T
nuget install PdfSharp.MigraDoc.Standard -Version %{version}
nuget install System.Drawing.Common -Version 5.0.2
nuget install System.Resources.Extensions -Version 5.0.0

cat > PdfSharp.MigraDoc.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

Name: PdfSharp.MigraDoc
Description: PdfSharp.MigraDoc - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/PdfSharp.dll -r:${libdir}/PdfSharp.Charting.dll -r:${libdir}/MigraDoc.Rendering.dll -r:${libdir}/MigraDoc.DocumentObjectModel.dll -r:${libdir}/System.Drawing.Common.dll -r:${libdir}/System.Resources.Extensions.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 PdfSharp.MigraDoc.Standard.DocumentObjectModel.%{version}/lib/netstandard2.0/MigraDoc.DocumentObjectModel.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 PdfSharp.MigraDoc.Standard.%{version}/lib/netstandard2.0/MigraDoc.Rendering.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 PDFSharp.Standard.Charting.%{version}/lib/netstandard2.0/PdfSharp.Charting.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 PDFSharp.Standard.%{version}/lib/netstandard2.0/PdfSharp.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 System.Drawing.Common.5.0.2/lib/netstandard2.0/System.Drawing.Common.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 System.Resources.Extensions.5.0.0/lib/netstandard2.0/System.Resources.Extensions.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 PdfSharp.MigraDoc.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/MigraDoc.DocumentObjectModel.dll
%{_darwinx_prefix}%{libdir}/MigraDoc.Rendering.dll
%{_darwinx_prefix}%{libdir}/PdfSharp.Charting.dll
%{_darwinx_prefix}%{libdir}/PdfSharp.dll
%{_darwinx_prefix}%{libdir}/System.Drawing.Common.dll
%{_darwinx_prefix}%{libdir}/System.Resources.Extensions.dll

%{_darwinx_datadir}/pkgconfig/PdfSharp.MigraDoc.pc

%changelog
* Thu Jan 4 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.50.4740-beta5-1
- Initial version
