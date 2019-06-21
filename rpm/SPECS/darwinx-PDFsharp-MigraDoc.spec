%global debug_package %{nil}

%define darwinx_pkg_name PDFsharp-MigraDoc
%define libdir /lib

Name:           darwinx-PDFsharp-MigraDoc
Version:        1.50.5147
Release:        1%{?dist}
Summary:        .NET library that easily creates documents and renders them into PDF or RTF.

Group:          Development/Languages
License:        MIT
URL:            http://www.pdfsharp.net
Prefix:		/usr

BuildArch:	noarch

%description
MigraDoc Foundation - the Open Source .NET library that easily creates documents based on an 
object model with paragraphs, tables, styles, etc. and renders them into PDF or RTF.

%prep
%setup -c %{name}-%{version} -T
nuget install PDFsharp-MigraDoc -Version %{version}

cat > PDFsharp-MigraDoc.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

Name: PDFsharp-MigraDoc
Description: PDFsharp-MigraDoc - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/PdfSharp.dll -r:${libdir}/PdfSharp.Charting.dll -r:${libdir}/MigraDoc.RtfRendering.dll -r:${libdir}/MigraDoc.Rendering.dll -r:${libdir}/MigraDoc.DocumentObjectModel.dll 
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 %{darwinx_pkg_name}.%{version}/lib/net20/MigraDoc.DocumentObjectModel.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 %{darwinx_pkg_name}.%{version}/lib/net20/MigraDoc.Rendering.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 %{darwinx_pkg_name}.%{version}/lib/net20/MigraDoc.RtfRendering.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 %{darwinx_pkg_name}.%{version}/lib/net20/PdfSharp.Charting.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 %{darwinx_pkg_name}.%{version}/lib/net20/PdfSharp.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 PDFsharp-MigraDoc.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/MigraDoc.DocumentObjectModel.dll
%{_darwinx_prefix}%{libdir}/MigraDoc.Rendering.dll
%{_darwinx_prefix}%{libdir}/MigraDoc.RtfRendering.dll
%{_darwinx_prefix}%{libdir}/PdfSharp.Charting.dll
%{_darwinx_prefix}%{libdir}/PdfSharp.dll
%{_darwinx_datadir}/pkgconfig/PDFsharp-MigraDoc.pc

%changelog
* Thu Jan 4 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.50.4740-beta5-1
- Initial version
