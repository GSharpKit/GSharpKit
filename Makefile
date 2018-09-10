VERSION = 28.1
VERSION_BUILD = 3

msi32: GSharpKit.json.in make-msi32.sh.in
	cp GSharpKit.json.in GSharpKit.json
	sed -i -e 's!@VERSION@!${VERSION}!g' GSharpKit.json
	sed -i -e 's!@VERSION_BUILD@!${VERSION_BUILD}!g' GSharpKit.json
	sed -i -e 's!@ARCH_NO@!32!g' GSharpKit.json
	sed -i -e 's!@ARCH_SHORT@!x86!g' GSharpKit.json
	cp make-msi32.sh.in make-msi32.sh
	sed -i -e 's!@VERSION@!${VERSION}!g' make-msi32.sh
	sed -i -e 's!@VERSION_BUILD@!${VERSION_BUILD}!g' make-msi32.sh
	sh make-msi32.sh

sign32: GSharpKit-28.1-x86.msi
	mv GSharpKit-${VERSION}-x86.msi GSharpKit-${VERSION}-x86.msi.unsigned
	osslsigncode sign -pkcs12 ~/.pki/gsharpkit.p12 -askpass -n "GSharpKit" -i http://www.gsharpkit.com -t http://time.certum.pl -in GSharpKit-${VERSION}-x86.msi.unsigned -out GSharpKit-${VERSION}-x86.msi && rm GSharpKit-${VERSION}-x86.msi.unsigned


clean:
	rm *.msi
