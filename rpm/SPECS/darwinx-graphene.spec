Name:           darwinx-graphene
Version:        1.10.8
Release:        1%{?dist}
Summary:        When creating graphic libraries you most likely end up dealing with points and rectangles.

License:        LGPLv2+
Group:          Development/Libraries
URL:		https://github.com/ebassi/graphene
Source0:        graphene-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext

Requires:  	darwinx-filesystem >= 18

%description
When creating graphic libraries you most likely end up dealing with points and rectangles.

%prep
%setup -q -n graphene-%{version}

%build
%darwinx_meson \
	--default-library=shared \
	-Dgobject_types=true \
	-Dintrospection=disabled \
	-Dgcc_vector=true \
	-Dsse2=true \
	-Darm_neon=true \
	-Dgtk_doc=false \
	-Dtests=false \
	-Dinstalled_tests=false

%darwinx_meson_build

%install
%darwinx_meson_install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%{_darwinx_libdir}/libgraphene-1.0.dylib
%{_darwinx_libdir}/libgraphene-1.0.*.dylib
%{_darwinx_libdir}/pkgconfig/graphene-1.0.pc
%{_darwinx_libdir}/pkgconfig/graphene-gobject-1.0.pc
%dir %{_darwinx_libdir}/graphene-1.0
%{_darwinx_libdir}/graphene-1.0/include/*.h
%dir %{_darwinx_includedir}/graphene-1.0
%{_darwinx_includedir}/graphene-1.0/*.h

%changelog
* Thu Jun 9 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.2-1
- Initial RPM release
