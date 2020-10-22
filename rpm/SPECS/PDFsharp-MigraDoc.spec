%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define libdir /lib
%define apiversion 1.50.0.0

Name:           PDFsharp-MigraDoc
Version:        1.50.5147
Release:        1%{?dist}
Summary:        .NET library that easily creates documents and renders them into PDF or RTF.

Group:          Development/Languages
License:        MIT
URL:            http://www.pdfsharp.net
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

Requires:	mono-core >= 4.8.0

%description
MigraDoc Foundation - the Open Source .NET library that easily creates documents based on an 
object model with paragraphs, tables, styles, etc. and renders them into PDF or RTF.

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > %{name}.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}/mono

Name: %{name}
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/%{name}/PdfSharp.dll -r:${libdir}/%{name}/PdfSharp.Charting.dll -r:${libdir}/%{name}/MigraDoc.RtfRendering.dll -r:${libdir}/%{name}/MigraDoc.Rendering.dll -r:${libdir}/%{name}/MigraDoc.DocumentObjectModel.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

gacutil -i %{name}.%{version}/lib/net20/MigraDoc.DocumentObjectModel.dll -package %{name} -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac
gacutil -i %{name}.%{version}/lib/net20/MigraDoc.Rendering.dll -package %{name} -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac
gacutil -i %{name}.%{version}/lib/net20/MigraDoc.RtfRendering.dll -package %{name} -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac
gacutil -i %{name}.%{version}/lib/net20/PdfSharp.Charting.dll -package %{name} -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac
gacutil -i %{name}.%{version}/lib/net20/PdfSharp.dll -package %{name} -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 %{name}.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/mono/gac
%{_prefix}%{libdir}/mono/%{name}/MigraDoc.DocumentObjectModel.dll
%{_prefix}%{libdir}/mono/%{name}/MigraDoc.Rendering.dll
%{_prefix}%{libdir}/mono/%{name}/MigraDoc.RtfRendering.dll
%{_prefix}%{libdir}/mono/%{name}/PdfSharp.Charting.dll
%{_prefix}%{libdir}/mono/%{name}/PdfSharp.dll
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Thu Aug 02 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.50.4845-RC2a-1
- Update to 1.50.4845-RC2a

* Thu Jan 4 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.50.4740-beta5-1
- Initial version
