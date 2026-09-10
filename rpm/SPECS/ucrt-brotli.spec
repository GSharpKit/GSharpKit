%{?ucrt_package_header}

Name: ucrt-brotli
Version: 1.0.7
Release: 16%{?dist}
Summary: MinGW port of Lossless compression algorithm

License: MIT
URL: https://github.com/google/brotli
Source0: %{url}/archive/v%{version}/brotli-%{version}.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: cmake

BuildRequires: ucrt64-filesystem
BuildRequires: ucrt64-gcc

%description
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.

%package -n ucrt64-brotli
Summary: %{summary}

%description -n ucrt64-brotli
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.

%{?ucrt_debug_package}

%prep
%autosetup -n brotli-%{version}
# fix permissions for -debuginfo
# rpmlint will complain if I create an extra %%files section for
# -debuginfo for this so we'll put it here instead
chmod 644 c/enc/*.[ch]
chmod 644 c/include/brotli/*.h
chmod 644 c/tools/brotli.c

%build
%ucrt64_cmake
%ucrt64_make %{?_smp_mflags}

%install
%ucrt64_make install DESTDIR=$RPM_BUILD_ROOT

# Remove static libraries but DON'T remove *.dll.a files.
rm -f $RPM_BUILD_ROOT%{ucrt64_libdir}/*-static.a

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

# Manpages don't need to be bundled
rm -rf $RPM_BUILD_ROOT%{ucrt64_datadir}/man

rm -rf $RPM_BUILD_ROOT%{ucrt64_datadir}/gtk-doc

%files -n ucrt64-brotli
%{ucrt64_bindir}/brotli.exe
%{ucrt64_bindir}/libbrotlicommon.dll
%{ucrt64_bindir}/libbrotlidec.dll
%{ucrt64_bindir}/libbrotlienc.dll
%{ucrt64_includedir}/brotli
%{ucrt64_libdir}/libbrotlicommon.dll.a
%{ucrt64_libdir}/libbrotlidec.dll.a
%{ucrt64_libdir}/libbrotlienc.dll.a
%{ucrt64_libdir}/pkgconfig/libbrotlicommon.pc
%{ucrt64_libdir}/pkgconfig/libbrotlidec.pc
%{ucrt64_libdir}/pkgconfig/libbrotlienc.pc
%license LICENSE

%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.0.7-7
- Rebuild with ucrt-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 15 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.0.7-1
- Initial package
