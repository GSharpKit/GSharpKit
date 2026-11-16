%{?mingw_package_header}

Name:           ucrt-egl-headers
Version:        1.5
Release:        1%{?dist}
Summary:        Almost Native Graphics Layer Engine

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://chromium.googlesource.com/angle/angle
BuildArch:      noarch

Source0:        egl-headers-%{version}.tar.xz

%description

# Win64
%package -n ucrt64-egl-headers
Summary:        Almost Native Graphics Layer Engine for Win64

%description -n ucrt64-egl-headers 

%prep
%setup -q -n egl-headers-%{version}

%install
install -d -m755 %{buildroot}%{ucrt64_includedir}/EGL
install *.h %{buildroot}%{ucrt64_includedir}/EGL/

%files -n ucrt64-egl-headers
%{ucrt64_includedir}/EGL

%changelog
* Mon Nov 16 2026 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.5-1
- Initial release

