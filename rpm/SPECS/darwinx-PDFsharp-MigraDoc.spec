%global debug_package %{nil}

%define libdir /lib

%define beta -beta5

Name:           darwinx-PDFsharp-MigraDoc
Version:        1.50.4740
Release:        beta5%{?dist}
Summary:        .NET library that easily creates documents and renders them into PDF or RTF.

Group:          Development/Languages
License:        MIT
URL:            http://www.pdfsharp.net
Prefix:		/usr

BuildArch:	noarch

Requires:	darwinx-mono-core >= 3.0

%description
MigraDoc Foundation - the Open Source .NET library that easily creates documents based on an 
object model with paragraphs, tables, styles, etc. and renders them into PDF or RTF.

%prep
%setup -c %{name}-%{version} -T
nuget install PDFsharp-MigraDoc -Version %{version}%{beta}

cat > PDFsharp-MigraDoc.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}/mono

Name: PDFsharp-MigraDoc
Description: PDFsharp-MigraDoc - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/PDFsharp-MigraDoc/PdfSharp.dll -r:${libdir}/PDFsharp-MigraDoc/PdfSharp.Charting.dll -r:${libdir}/PDFsharp-MigraDoc/MigraDoc.RtfRendering.dll -r:${libdir}/PDFsharp-MigraDoc/MigraDoc.Rendering.dll -r:${libdir}/PDFsharp-MigraDoc/MigraDoc.DocumentObjectModel.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

gacutil -i PDFsharp-MigraDoc.%{version}%{beta}/lib/net20/MigraDoc.DocumentObjectModel.dll -package PDFsharp-MigraDoc -root $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir} -gacdir mono/gac
gacutil -i PDFsharp-MigraDoc.%{version}%{beta}/lib/net20/MigraDoc.Rendering.dll -package PDFsharp-MigraDoc -root $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir} -gacdir mono/gac
gacutil -i PDFsharp-MigraDoc.%{version}%{beta}/lib/net20/MigraDoc.RtfRendering.dll -package PDFsharp-MigraDoc -root $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir} -gacdir mono/gac
gacutil -i PDFsharp-MigraDoc.%{version}%{beta}/lib/net20/PdfSharp.Charting.dll -package PDFsharp-MigraDoc -root $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir} -gacdir mono/gac
gacutil -i PDFsharp-MigraDoc.%{version}%{beta}/lib/net20/PdfSharp.dll -package PDFsharp-MigraDoc -root $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 PDFsharp-MigraDoc.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/mono/gac
%{_darwinx_prefix}%{libdir}/mono/PDFsharp-MigraDoc/MigraDoc.DocumentObjectModel.dll
%{_darwinx_prefix}%{libdir}/mono/PDFsharp-MigraDoc/MigraDoc.Rendering.dll
%{_darwinx_prefix}%{libdir}/mono/PDFsharp-MigraDoc/MigraDoc.RtfRendering.dll
%{_darwinx_prefix}%{libdir}/mono/PDFsharp-MigraDoc/PdfSharp.Charting.dll
%{_darwinx_prefix}%{libdir}/mono/PDFsharp-MigraDoc/PdfSharp.dll
%{_darwinx_datadir}/pkgconfig/PDFsharp-MigraDoc.pc

%changelog
* Thu Jan 4 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.50.4740-beta5-1
- Initial version
