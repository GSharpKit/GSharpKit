%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name PdfSharp.MigraDoc 
%global mingw_build_win32 0
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin
%define apiversion 1.50.0.0

Name:           mingw-PdfSharp.MigraDoc
Version:        1.51.16
Release:        1%{?dist}
Summary:        .NET library that easily creates documents and renders them into PDF or RTF.
Source0:        PdfSharp.MigraDoc-%{version}.tar.xz

Group:          Development/Languages
License:        MIT
URL:            http://www.pdfsharp.net
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  nuget


%description
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
%setup -q -n %{mingw_pkg_name}-%{version}

cat > %{mingw_pkg_name}64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: %{mingw_pkg_name}
Description: %{mingw_pkg_name} - %{summary}
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

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 MigraDoc/src/MigraDoc.Rendering/app/MigraDoc.DocumentObjectModel.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 MigraDoc/src/MigraDoc.Rendering/app/MigraDoc.Rendering.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 MigraDoc/src/MigraDoc.Rendering/app/PdfSharp.Charting.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 MigraDoc/src/MigraDoc.Rendering/app/PdfSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 MigraDoc/src/MigraDoc.Rendering/app/SixLabors.ImageSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 MigraDoc/src/MigraDoc.Rendering/app/SixLabors.Fonts.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 MigraDoc/src/MigraDoc.Rendering/app/System.Resources.Extensions.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 %{mingw_pkg_name}64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/%{mingw_pkg_name}.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/MigraDoc.DocumentObjectModel.dll
%{mingw64_prefix}%{libdir}/MigraDoc.Rendering.dll
%{mingw64_prefix}%{libdir}/PdfSharp.Charting.dll
%{mingw64_prefix}%{libdir}/PdfSharp.dll
%{mingw64_prefix}%{libdir}/SixLabors.ImageSharp.dll
%{mingw64_prefix}%{libdir}/SixLabors.Fonts.dll
%{mingw64_prefix}%{libdir}/System.Resources.Extensions.dll
%{mingw64_datadir}/pkgconfig/%{mingw_pkg_name}.pc

%changelog
* Thu Aug 02 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.50.4845-RC2a-1
- Update to 1.50.4845-RC2a

* Thu Jan 4 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.50.4740-beta5-1
- Initial version
