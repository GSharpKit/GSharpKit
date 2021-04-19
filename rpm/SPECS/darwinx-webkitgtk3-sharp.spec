Name:		darwinx-webkitgtk3-sharp
Version:	2.4.11
Release:	2%{?dist}
Summary:	.NET bindings for WebKit
Group:		Development/Languages
License:	MIT
URL:		http://ftp.novell.com/pub/mono/sources/webkit-sharp/
Source0:        webkitgtk3-sharp-%{version}.tar.gz
Patch0:		webkitgtk3-sharp-2.4.11-funny.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

BuildRequires:	darwinx-webkitgtk3 >= %{version}
BuildRequires:	darwinx-GtkSharp >= 3.14.0
BuildRequires:	darwinx-mono-core

Requires:  	darwinx-webkitgtk3 >= %{version}
Requires:  	darwinx-GtkSharp >= 3.14.0

%description
WebKit-sharp is .NET bindings for the WebKit rendering engine.

%prep
%setup -q -n webkitgtk3-sharp-%{version}
%patch0 -p1

sed -i '' 's!name="webkitgtk-3.0"!name="libwebkitgtk-3.0.0.dylib"!g' sources/webkitgtk3-sharp-sources.xml

sed -i '' 's!\[assembly: AssemblyDelaySign(false)\]!!g' sources/AssemblyInfo.cs.in
sed -i '' 's!\[assembly: AssemblyKeyFile("@ASSEMBLY_NAME@.snk")\]!!g' sources/AssemblyInfo.cs.in

%build
autoreconf --verbose --install -I /Library/Frameworks/GSharpKit/share/aclocal
%{_darwinx_configure}

# parallel build fails in mock
%{_darwinx_make}

%install
%{__rm} -rf %{buildroot}

mkdir -p $RPM_BUILD_ROOT%{_darwinx_libdir}
cp sources/webkitgtk3-sharp.dll $RPM_BUILD_ROOT%{_darwinx_libdir}/

#sed -i '' 's!webkitgtk-3.0.0.dylib!libwebkitgtk-3.0.0.dylib!g' sources/webkitgtk3-sharp.dll.config
#cp sources/webkitgtk3-sharp.dll.config $RPM_BUILD_ROOT%{_darwinx_libdir}/

mkdir -p $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
cp sources/webkitgtk3-sharp-3.0.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
sed -i '' 's!mono/webkitgtk3-sharp/!!g' $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/webkitgtk3-sharp-3.0.pc

%clean
#{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_libdir}/webkitgtk3-sharp.dll
#{_darwinx_libdir}/webkitgtk3-sharp.dll.config
%{_darwinx_datadir}/pkgconfig/webkitgtk3-sharp-3.0.pc

%changelog
* Sat Feb 21 2009 David Nielsen <gnomeuser@gmail.com> - 0.2-1
- Initial package
