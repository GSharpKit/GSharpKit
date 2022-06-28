%global debug_package %{nil}

%define libdir /lib

Name:           GirCore
Version:        0.99
Release:        3%{?dist}
Summary:        Gir.Core is a C# wrapper for GObject-based libraries like GTK for user interfaces.
Group:          System Environment/Libraries
License:        MIT
URL:            https://github.com/gircore/gir.core
Source0:        gir.core-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
AutoReqProv:    no

BuildRequires:  dotnet-sdk-6.0

%description
Gir.Core is a C# wrapper for GObject-based libraries like GTK for user interfaces.

This project aims to provide a complete set of APIs for writing rich cross-platform 
user interfaces and multimedia programs. It is built upon the well-established 
GObject Introspection framework for language bindings.

%prep
%setup -q -n gir.core-%{version}

%build
cd src
dotnet fsi GenerateLibs.fsx
dotnet publish -o ../app

%install
%{__rm} -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/Atk-1.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/cairo-1.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/Gdk-3.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/Gdk-4.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/GdkPixbuf-2.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/Gio-2.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/GLib-2.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/GObject-2.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/Graphene-1.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/Gsk-4.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/Gst-1.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/GstAudio-1.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/GstBase-1.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/GstPbutils-1.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/GStreamer.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/GstVideo-1.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/Gtk-3.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/Gtk-4.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/HarfBuzz-0.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/Pango-1.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 app/PangoCairo-1.0.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/*.dll

%changelog
* Mon Feb 21 2022 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.99-1
- Initial version
