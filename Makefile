include config

msi: msi64 sign64

msisdk: msi64sdk sign64sdk

msi64: GSharpKit.json.in make-msi64.sh.in
	cp GSharpKit.json.in GSharpKit.json
	sed -i -e 's!@VERSION@!${VERSION}!g' GSharpKit.json
	sed -i -e 's!@RELEASE@!${RELEASE}!g' GSharpKit.json
	sed -i -e 's!@ARCH_NO@!64!g' GSharpKit.json
	sed -i -e 's!@ARCH_SHORT@!x64!g' GSharpKit.json
	sed -i -e 's!@INSTALL_SCOPE@!perMachine!g' GSharpKit.json
	cp make-msi64.sh.in make-msi64.sh
	sed -i -e 's!@VERSION@!${VERSION}!g' make-msi64.sh
	sed -i -e 's!@RELEASE@!${RELEASE}!g' make-msi64.sh
	sh make-msi64.sh

sign64: GSharpKit-${VERSION}-x64.msi
	mv GSharpKit-${VERSION}-x64.msi GSharpKit-${VERSION}-x64.msi.unsigned
	osslsigncode sign -pkcs11engine /usr/lib64/engines-3/pkcs11.so -pkcs11module /docker/keylocker/smpkcs11.so -certs /docker/keylocker/xmedicus_systems_aps.pem -key 'pkcs11:object=key_711812656;type=private' -n GSharpKit -i https://www.gsharpkit.com -t http://timestamp.digicert.com -h sha2 -in GSharpKit-${VERSION}-x64.msi.unsigned -out GSharpKit-${VERSION}-x64.msi && rm GSharpKit-${VERSION}-x64.msi.unsigned
	#mv GSharpKit-${VERSION}-x64.msi GSharpKit-${VERSION}-x64.msi.unsigned
	#osslsigncode sign -pkcs11engine /usr/lib64/engines-3/pkcs11.so -pkcs11module /docker/keylocker/smpkcs11.so -certs /docker/keylocker/xmedicus_systems_aps.pem -key 'pkcs11:object=key_711812656;type=private' -n GSharpKit -i https://www.gsharpkit.com -t http://timestamp.digicert.com -nest -h sha512 -in GSharpKit-${VERSION}-x64.msi.unsigned -out GSharpKit-${VERSION}-x64.msi && rm GSharpKit-${VERSION}-x64.msi.unsigned

msi64sdk: GSharpSdk.json.in make-msisdk.sh.in
	cp GSharpSdk.json.in GSharpSdk.json
	sed -i -e 's!@VERSION@!${SDK_VERSION}!g' GSharpSdk.json
	sed -i -e 's!@FRAMEWORK@!${FRAMEWORK}!g' GSharpSdk.json
	sed -i -e 's!@RELEASE@!${RELEASE}!g' GSharpSdk.json
	sed -i -e 's!@ARCH_NO@!64!g' GSharpSdk.json
	sed -i -e 's!@ARCH_SHORT@!x64!g' GSharpSdk.json
	sed -i -e 's!@INSTALL_SCOPE@!perMachine!g' GSharpSdk.json
	cp make-msisdk.sh.in make-msisdk.sh
	sed -i -e 's!@VERSION@!${SDK_VERSION}!g' make-msisdk.sh
	sed -i -e 's!@RELEASE@!${RELEASE}!g' make-msisdk.sh
	sed -i -e 's!@FRAMEWORK@!${FRAMEWORK}!g' make-msisdk.sh
	sh make-msisdk.sh

sign64sdk: GSharpSdk-${SDK_VERSION}-x64.msi
	mv GSharpSdk-${SDK_VERSION}-x64.msi GSharpSdk-${SDK_VERSION}-x64.msi.unsigned
	osslsigncode sign -pkcs11engine /usr/lib64/engines-3/pkcs11.so -pkcs11module /docker/keylocker/smpkcs11.so -certs /docker/keylocker/xmedicus_systems_aps.pem -key 'pkcs11:object=key_711812656;type=private' -n GSharpKit -i https://www.gsharpkit.com -t http://timestamp.digicert.com -h sha2 -in GSharpSdk-${VERSION}-x64.msi.unsigned -out GSharpSdk-${VERSION}-x64.msi && rm GSharpSdk-${VERSION}-x64.msi.unsigned
	#mv GSharpSdk-${SDK_VERSION}-x64.msi GSharpSdk-${SDK_VERSION}-x64.msi.unsigned
	#osslsigncode sign -pkcs11engine /usr/lib64/engines-3/pkcs11.so -pkcs11module /docker/keylocker/smpkcs11.so -certs /docker/keylocker/xmedicus_systems_aps.pem -key 'pkcs11:object=key_711812656;type=private' -n GSharpKit -i https://www.gsharpkit.com -t http://timestamp.digicert.com -nest -h sha512 -in GSharpSdk-${VERSION}-x64.msi.unsigned -out GSharpSdk-${VERSION}-x64.msi && rm GSharpSdk-${VERSION}-x64.msi.unsigned


pkg: pkg64

pkg-release: pkg64 notarize

pkg64: make-pkg.sh.in
	cp make-pkg.sh.in make-pkg.sh
	sed -i '' 's!@VERSION@!${VERSION}!g' make-pkg.sh
	sed -i '' 's!@RELEASE@!${RELEASE}!g' make-pkg.sh
	sh make-pkg.sh

notarize: make-pkg-notarize.sh.in
	cp make-pkg-notarize.sh.in make-pkg-notarize.sh
	sed -i '' 's!@VERSION@!${VERSION}!g' make-pkg-notarize.sh
	sed -i '' 's!@RELEASE@!${RELEASE}!g' make-pkg-notarize.sh
	sh make-pkg-notarize.sh

clean:
	-rm -f *.msi
	-rm -f *.pkg
