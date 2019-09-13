include config

msi: msi32 msi64 sign32 sign64

msi32: GSharpKit.json.in make-msi32.sh.in
	cp GSharpKit.json.in GSharpKit.json
	sed -i -e 's!@VERSION@!${VERSION}!g' GSharpKit.json
	sed -i -e 's!@RELEASE@!${RELEASE}!g' GSharpKit.json
	sed -i -e 's!@ARCH_NO@!32!g' GSharpKit.json
	sed -i -e 's!@ARCH_SHORT@!x86!g' GSharpKit.json
	cp make-msi32.sh.in make-msi32.sh
	sed -i -e 's!@VERSION@!${VERSION}!g' make-msi32.sh
	sed -i -e 's!@RELEASE@!${RELEASE}!g' make-msi32.sh
	sh make-msi32.sh

sign32: GSharpKit-${VERSION}-x86.msi
	mv GSharpKit-${VERSION}-x86.msi GSharpKit-${VERSION}-x86.msi.unsigned
	osslsigncode sign -pkcs12 ~/.pki/gsharpkit.p12 -askpass -n "GSharpKit" -i http://www.gsharpkit.com -t http://time.certum.pl -h sha2 -in GSharpKit-${VERSION}-x86.msi.unsigned -out GSharpKit-${VERSION}-x86.msi && rm GSharpKit-${VERSION}-x86.msi.unsigned
	mv GSharpKit-${VERSION}-x86.msi GSharpKit-${VERSION}-x86.msi.unsigned
	osslsigncode sign -pkcs12 ~/.pki/gsharpkit.p12 -askpass -n "GSharpKit" -i http://www.gsharpkit.com -t http://time.certum.pl -nest -h sha512 -in GSharpKit-${VERSION}-x86.msi.unsigned -out GSharpKit-${VERSION}-x86.msi && rm GSharpKit-${VERSION}-x86.msi.unsigned

msi64: GSharpKit.json.in make-msi64.sh.in
	cp GSharpKit.json.in GSharpKit.json
	sed -i -e 's!@VERSION@!${VERSION}!g' GSharpKit.json
	sed -i -e 's!@RELEASE@!${RELEASE}!g' GSharpKit.json
	sed -i -e 's!@ARCH_NO@!64!g' GSharpKit.json
	sed -i -e 's!@ARCH_SHORT@!x64!g' GSharpKit.json
	cp make-msi64.sh.in make-msi64.sh
	sed -i -e 's!@VERSION@!${VERSION}!g' make-msi64.sh
	sed -i -e 's!@RELEASE@!${RELEASE}!g' make-msi64.sh
	sh make-msi64.sh

sign64: GSharpKit-${VERSION}-x64.msi
	mv GSharpKit-${VERSION}-x64.msi GSharpKit-${VERSION}-x64.msi.unsigned
	osslsigncode sign -pkcs12 ~/.pki/gsharpkit.p12 -askpass -n "GSharpKit" -i http://www.gsharpkit.com -t http://time.certum.pl -h sha2 -in GSharpKit-${VERSION}-x64.msi.unsigned -out GSharpKit-${VERSION}-x64.msi && rm GSharpKit-${VERSION}-x64.msi.unsigned
	mv GSharpKit-${VERSION}-x64.msi GSharpKit-${VERSION}-x64.msi.unsigned
	osslsigncode sign -pkcs12 ~/.pki/gsharpkit.p12 -askpass -n "GSharpKit" -i http://www.gsharpkit.com -t http://time.certum.pl -nest -h sha512 -in GSharpKit-${VERSION}-x64.msi.unsigned -out GSharpKit-${VERSION}-x64.msi && rm GSharpKit-${VERSION}-x64.msi.unsigned

pkg: make-pkg.sh.in
	cp make-pkg.sh.in make-pkg.sh
	sed -i '' 's!@VERSION@!${VERSION}!g' make-pkg.sh
	sed -i '' 's!@RELEASE@!${RELEASE}!g' make-pkg.sh
	sh make-pkg.sh


clean:
	rm *.msi
