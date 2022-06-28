%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define libdir /lib
%define apiversion 1.50.0.0

Name:           PdfSharp.MigraDoc
Version:        1.51.16
Release:        1%{?dist}
Summary:        .NET library that easily creates documents and renders them into PDF or RTF.
Source0:	PdfSharp.MigraDoc-%{version}.tar.xz

Group:          Development/Languages
License:        MIT
URL:            http://www.pdfsharp.net
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

Obsoletes:	PDFsharp-MigraDoc

%description
MigraDoc Foundation - the Open Source .NET library that easily creates documents based on an 
object model with paragraphs, tables, styles, etc. and renders them into PDF or RTF.

%prep
%setup -q

cat > %{name}.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: %{name}
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/PdfSharp.dll -r:${libdir}/PdfSharp.Charting.dll -r:${libdir}/MigraDoc.Rendering.dll -r:${libdir}/MigraDoc.DocumentObjectModel.dll -r:${libdir}/SixLabors.ImageSharp.dll -r:${libdir}/SixLabors.Fonts.dll -r:${libdir}/System.Resources.Extensions.dll
Cflags:
EOF

%build
cd MigraDoc/src/MigraDoc.Rendering
dotnet restore
dotnet publish -c Release -o app

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 MigraDoc/src/MigraDoc.Rendering/app/MigraDoc.DocumentObjectModel.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 MigraDoc/src/MigraDoc.Rendering/app/MigraDoc.Rendering.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 MigraDoc/src/MigraDoc.Rendering/app/PdfSharp.Charting.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 MigraDoc/src/MigraDoc.Rendering/app/PdfSharp.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 MigraDoc/src/MigraDoc.Rendering/app/SixLabors.ImageSharp.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 MigraDoc/src/MigraDoc.Rendering/app/SixLabors.Fonts.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 MigraDoc/src/MigraDoc.Rendering/app/System.Resources.Extensions.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}

#install -m 644 PdfSharp.MigraDoc.Standard.DocumentObjectModel.%{version}/lib/netstandard2.0/MigraDoc.DocumentObjectModel.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
#install -m 644 PdfSharp.MigraDoc.Standard.%{version}/lib/netstandard2.0/MigraDoc.Rendering.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
#install -m 644 PDFSharp.Standard.Charting.%{version}/lib/netstandard2.0/PdfSharp.Charting.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
#install -m 644 PDFSharp.Standard.%{version}/lib/netstandard2.0/PdfSharp.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
#install -m 644 System.Resources.Extensions.5.0.0/lib/netstandard2.0/System.Resources.Extensions.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 %{name}.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/MigraDoc.DocumentObjectModel.dll
%{_prefix}%{libdir}/MigraDoc.Rendering.dll
%{_prefix}%{libdir}/PdfSharp.Charting.dll
%{_prefix}%{libdir}/PdfSharp.dll
%{_prefix}%{libdir}/SixLabors.ImageSharp.dll
%{_prefix}%{libdir}/SixLabors.Fonts.dll
%{_prefix}%{libdir}/System.Resources.Extensions.dll
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Thu Aug 02 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.50.4845-RC2a-1
- Update to 1.50.4845-RC2a

* Thu Jan 4 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.50.4740-beta5-1
- Initial version
