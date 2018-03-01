%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name BouncyCastle
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /lib
%define apiversion 1.8.0.0

Name:           mingw-BouncyCastle
Version:        1.8.1
Release:        2%{?dist}
Summary:        BouncyCastle is a Crypto library written in C#

Group:          Development/Languages
License:        MIT
URL:            http://www.bouncycastle.org/csharp/

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

%description
- Generation and parsing of PKCS-12 files.
- X.509: Generators and parsers for V1 and V3 certificates, V2 CRLs and attribute certificates.
- PBE algorithms supported by PbeUtilities: PBEwithMD2andDES-CBC, PBEwithMD2andRC2-CBC, PBEwithMD5andDES-CBC, PBEwithMD5andRC2-CBC, PBEwithSHA1andDES-CBC, PBEwithSHA1andRC2-CBC, PBEwithSHA-1and128bitRC4, PBEwithSHA-1and40bitRC4, PBEwithSHA-1and3-keyDESEDE-CBC, PBEwithSHA-1and2-keyDESEDE-CBC, PBEwithSHA-1and128bitRC2-CBC, PBEwithSHA-1and40bitRC2-CBC, PBEwithHmacSHA-1, PBEwithHmacSHA-224, PBEwithHmacSHA-256, PBEwithHmacRIPEMD128, PBEwithHmacRIPEMD160, and PBEwithHmacRIPEMD256.
- Signature algorithms supported by SignerUtilities: MD2withRSA, MD4withRSA, MD5withRSA, RIPEMD128withRSA, RIPEMD160withECDSA, RIPEMD160withRSA, RIPEMD256withRSA, SHA-1withRSA, SHA-224withRSA, SHA-256withRSAandMGF1, SHA-384withRSAandMGF1, SHA-512withRSAandMGF1, SHA-1withDSA, and SHA-1withECDSA.
- Symmetric key algorithms: AES, Blowfish, Camellia, CAST5, CAST6, ChaCha, DES, DESede, GOST28147, HC-128, HC-256, IDEA, ISAAC, Noekeon, RC2, RC4, RC5-32, RC5-64, RC6, Rijndael, Salsa20, SEED, Serpent, Skipjack, TEA/XTEA, Threefish, Tnepres, Twofish, VMPC and XSalsa20.
- Symmetric key modes: CBC, CFB, CTS, GOFB, OFB, OpenPGPCFB, and SIC (or CTR).
- Symmetric key paddings: ISO10126d2, ISO7816d4, PKCS-5/7, TBC, X.923, and Zero Byte.
- Asymmetric key algorithms: ElGamal, DSA, ECDSA, NaccacheStern and RSA (with blinding).
- Asymmetric key paddings/encodings: ISO9796d1, OAEP, and PKCS-1.
- AEAD block cipher modes: CCM, EAX, GCM and OCB.
- Digests: GOST3411, Keccak, MD2, MD4, MD5, RIPEMD128, RIPEMD160, RIPEMD256, RIPEMD320, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA3, Tiger, and Whirlpool.
- XOFs: SHAKE.
- Signer mechanisms: DSA, ECDSA, ECGOST3410, ECNR, GOST3410, ISO9796d2, PSS, RSA, X9.31-1998.
- Key Agreement: Diffie-Hellman, EC-DH, EC-MQV, J-PAKE, SRP-6a.
- Macs: CBCBlockCipher, CFBBlockCipher, CMAC, GMAC, GOST28147, HMac, ISO9797 Alg. 3, Poly1305, SipHash, SkeinMac, VMPCMAC.
- PBE generators: PKCS-12, and PKCS-5 - schemes 1 and 2.
- OpenPGP (RFC 4880)
- Cryptographic Message Syntax (CMS, RFC 3852), including streaming API.
- Online Certificate Status Protocol (OCSP, RFC 2560).
- Time Stamp Protocol (TSP, RFC 3161).
- TLS/DTLS client/server up to version 1.2, with support for the most common ciphersuites and extensions, and many less common ones. Non-blocking API available.
- Elliptic Curve Cryptography: support for generic F2m and Fp curves, high-performance custom implementations for many standardized curves.
- Reading/writing of PEM files, including RSA and DSA keys, with a variety of encryptions.
- PKIX certificate path validation


# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw32-mono

%description -n mingw32-%{mingw_pkg_name}
- Generation and parsing of PKCS-12 files.
- X.509: Generators and parsers for V1 and V3 certificates, V2 CRLs and attribute certificates.
- PBE algorithms supported by PbeUtilities: PBEwithMD2andDES-CBC, PBEwithMD2andRC2-CBC, PBEwithMD5andDES-CBC, PBEwithMD5andRC2-CBC, PBEwithSHA1andDES-CBC, PBEwithSHA1andRC2-CBC, PBEwithSHA-1and128bitRC4, PBEwithSHA-1and40bitRC4, PBEwithSHA-1and3-keyDESEDE-CBC, PBEwithSHA-1and2-keyDESEDE-CBC, PBEwithSHA-1and128bitRC2-CBC, PBEwithSHA-1and40bitRC2-CBC, PBEwithHmacSHA-1, PBEwithHmacSHA-224, PBEwithHmacSHA-256, PBEwithHmacRIPEMD128, PBEwithHmacRIPEMD160, and PBEwithHmacRIPEMD256.
- Signature algorithms supported by SignerUtilities: MD2withRSA, MD4withRSA, MD5withRSA, RIPEMD128withRSA, RIPEMD160withECDSA, RIPEMD160withRSA, RIPEMD256withRSA, SHA-1withRSA, SHA-224withRSA, SHA-256withRSAandMGF1, SHA-384withRSAandMGF1, SHA-512withRSAandMGF1, SHA-1withDSA, and SHA-1withECDSA.
- Symmetric key algorithms: AES, Blowfish, Camellia, CAST5, CAST6, ChaCha, DES, DESede, GOST28147, HC-128, HC-256, IDEA, ISAAC, Noekeon, RC2, RC4, RC5-32, RC5-64, RC6, Rijndael, Salsa20, SEED, Serpent, Skipjack, TEA/XTEA, Threefish, Tnepres, Twofish, VMPC and XSalsa20.
- Symmetric key modes: CBC, CFB, CTS, GOFB, OFB, OpenPGPCFB, and SIC (or CTR).
- Symmetric key paddings: ISO10126d2, ISO7816d4, PKCS-5/7, TBC, X.923, and Zero Byte.
- Asymmetric key algorithms: ElGamal, DSA, ECDSA, NaccacheStern and RSA (with blinding).
- Asymmetric key paddings/encodings: ISO9796d1, OAEP, and PKCS-1.
- AEAD block cipher modes: CCM, EAX, GCM and OCB.
- Digests: GOST3411, Keccak, MD2, MD4, MD5, RIPEMD128, RIPEMD160, RIPEMD256, RIPEMD320, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA3, Tiger, and Whirlpool.
- XOFs: SHAKE.
- Signer mechanisms: DSA, ECDSA, ECGOST3410, ECNR, GOST3410, ISO9796d2, PSS, RSA, X9.31-1998.
- Key Agreement: Diffie-Hellman, EC-DH, EC-MQV, J-PAKE, SRP-6a.
- Macs: CBCBlockCipher, CFBBlockCipher, CMAC, GMAC, GOST28147, HMac, ISO9797 Alg. 3, Poly1305, SipHash, SkeinMac, VMPCMAC.
- PBE generators: PKCS-12, and PKCS-5 - schemes 1 and 2.
- OpenPGP (RFC 4880)
- Cryptographic Message Syntax (CMS, RFC 3852), including streaming API.
- Online Certificate Status Protocol (OCSP, RFC 2560).
- Time Stamp Protocol (TSP, RFC 3161).
- TLS/DTLS client/server up to version 1.2, with support for the most common ciphersuites and extensions, and many less common ones. Non-blocking API available.
- Elliptic Curve Cryptography: support for generic F2m and Fp curves, high-performance custom implementations for many standardized curves.
- Reading/writing of PEM files, including RSA and DSA keys, with a variety of encryptions.
- PKIX certificate path validation

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw64-mono

%description -n mingw64-%{mingw_pkg_name}
- Generation and parsing of PKCS-12 files.
- X.509: Generators and parsers for V1 and V3 certificates, V2 CRLs and attribute certificates.
- PBE algorithms supported by PbeUtilities: PBEwithMD2andDES-CBC, PBEwithMD2andRC2-CBC, PBEwithMD5andDES-CBC, PBEwithMD5andRC2-CBC, PBEwithSHA1andDES-CBC, PBEwithSHA1andRC2-CBC, PBEwithSHA-1and128bitRC4, PBEwithSHA-1and40bitRC4, PBEwithSHA-1and3-keyDESEDE-CBC, PBEwithSHA-1and2-keyDESEDE-CBC, PBEwithSHA-1and128bitRC2-CBC, PBEwithSHA-1and40bitRC2-CBC, PBEwithHmacSHA-1, PBEwithHmacSHA-224, PBEwithHmacSHA-256, PBEwithHmacRIPEMD128, PBEwithHmacRIPEMD160, and PBEwithHmacRIPEMD256.
- Signature algorithms supported by SignerUtilities: MD2withRSA, MD4withRSA, MD5withRSA, RIPEMD128withRSA, RIPEMD160withECDSA, RIPEMD160withRSA, RIPEMD256withRSA, SHA-1withRSA, SHA-224withRSA, SHA-256withRSAandMGF1, SHA-384withRSAandMGF1, SHA-512withRSAandMGF1, SHA-1withDSA, and SHA-1withECDSA.
- Symmetric key algorithms: AES, Blowfish, Camellia, CAST5, CAST6, ChaCha, DES, DESede, GOST28147, HC-128, HC-256, IDEA, ISAAC, Noekeon, RC2, RC4, RC5-32, RC5-64, RC6, Rijndael, Salsa20, SEED, Serpent, Skipjack, TEA/XTEA, Threefish, Tnepres, Twofish, VMPC and XSalsa20.
- Symmetric key modes: CBC, CFB, CTS, GOFB, OFB, OpenPGPCFB, and SIC (or CTR).
- Symmetric key paddings: ISO10126d2, ISO7816d4, PKCS-5/7, TBC, X.923, and Zero Byte.
- Asymmetric key algorithms: ElGamal, DSA, ECDSA, NaccacheStern and RSA (with blinding).
- Asymmetric key paddings/encodings: ISO9796d1, OAEP, and PKCS-1.
- AEAD block cipher modes: CCM, EAX, GCM and OCB.
- Digests: GOST3411, Keccak, MD2, MD4, MD5, RIPEMD128, RIPEMD160, RIPEMD256, RIPEMD320, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA3, Tiger, and Whirlpool.
- XOFs: SHAKE.
- Signer mechanisms: DSA, ECDSA, ECGOST3410, ECNR, GOST3410, ISO9796d2, PSS, RSA, X9.31-1998.
- Key Agreement: Diffie-Hellman, EC-DH, EC-MQV, J-PAKE, SRP-6a.
- Macs: CBCBlockCipher, CFBBlockCipher, CMAC, GMAC, GOST28147, HMac, ISO9797 Alg. 3, Poly1305, SipHash, SkeinMac, VMPCMAC.
- PBE generators: PKCS-12, and PKCS-5 - schemes 1 and 2.
- OpenPGP (RFC 4880)
- Cryptographic Message Syntax (CMS, RFC 3852), including streaming API.
- Online Certificate Status Protocol (OCSP, RFC 2560).
- Time Stamp Protocol (TSP, RFC 3161).
- TLS/DTLS client/server up to version 1.2, with support for the most common ciphersuites and extensions, and many less common ones. Non-blocking API available.
- Elliptic Curve Cryptography: support for generic F2m and Fp curves, high-performance custom implementations for many standardized curves.
- Reading/writing of PEM files, including RSA and DSA keys, with a variety of encryptions.
- PKIX certificate path validation

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > BouncyCastle32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}/mono

Name: BouncyCastle
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/BouncyCastle.Crypto/BouncyCastle.Crypto.dll
Cflags:
EOF

cat > BouncyCastle64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}/mono

Name: BouncyCastle
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/BouncyCastle.Crypto/BouncyCastle.Crypto.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/mono/gac
gacutil -i BouncyCastle.%{version}/lib/BouncyCastle.Crypto.dll -package %{mingw_pkg_name}.Crypto -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 BouncyCastle32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/BouncyCastle.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/mono/gac
gacutil -i BouncyCastle.%{version}/lib/BouncyCastle.Crypto.dll -package %{mingw_pkg_name}.Crypto -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 BouncyCastle64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/BouncyCastle.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/mono/gac
%{mingw32_prefix}%{libdir}/mono/BouncyCastle.Crypto/BouncyCastle.Crypto.dll
%{mingw32_datadir}/pkgconfig/BouncyCastle.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/mono/gac
%{mingw64_prefix}%{libdir}/mono/BouncyCastle.Crypto/BouncyCastle.Crypto.dll
%{mingw64_datadir}/pkgconfig/BouncyCastle.pc


%changelog
* Thu Sep 7 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.8.1-1
- Initial version
