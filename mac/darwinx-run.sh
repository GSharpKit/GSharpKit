#!/bin/bash
WD=/usr/darwinx/usr

bundle=$WD
bundle_contents="$bundle"
bundle_res="$bundle_contents"
bundle_lib="$bundle_res"/lib
bundle_bin="$bundle_res"/bin
bundle_data="$bundle_res"/share
bundle_etc="$bundle_res"/etc

export DYLD_LIBRARY_PATH="$bundle_lib"
export XDG_CONFIG_HOME="$bundle_etc"
export XDG_CONFIG_DIRS="$bundle_etc"/xdg
export XDG_DATA_DIRS="$bundle_data"
export GTK_DATA_PREFIX="$bundle_res"
export GTK_EXE_PREFIX="$bundle_res"
export GTK_PATH="$bundle_res"

export GTK_IM_MODULE_FILE="$bundle_etc/gtk-3.0/gtk.immodules"
export GDK_PIXBUF_MODULE_FILE="$bundle_etc/gtk-3.0/gdk-pixbuf.loaders"
export PANGO_RC_FILE="$bundle_etc/pango/pangorc"

# We need a UTF-8 locale.
lang=`defaults read .GlobalPreferences AppleLocale 2>/dev/null`
if test "$?" != "0"; then
  lang=`defaults read .GlobalPreferences AppleCollationOrder 2>/dev/null | sed 's/_.*//'`
fi
if test "$?" == "0"; then
    export LANG="`grep \"\`echo $lang\`_\" /usr/share/locale/locale.alias | \
  tail -n1 | sed 's/\./ /' | awk '{print $2}'`.UTF-8"
fi

if test -f "$bundle_lib/charset.alias"; then
    export CHARSETALIASDIR="$bundle_lib"
fi

if [ -n $LD_LIBRARY_PATH ]; then
	export LD_LIBRARY_PATH=$WD/lib:/usr/lib:$LD_LIBRARY_PATH
else
	export LD_LIBRARY_PATH=$WD/lib:/usr/lib
fi

export DYLD_LIBRARY_PATH=/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/Resources:/System/Library/Frameworks/CoreData.framework/Versions/A/Resources:$WD/lib:/usr/lib 
export PATH=$WD/bin:$WD/libexec:$PATH
export GDK_PIXBUF_MODULEDIR=$WD/lib/gdk-pixbuf-2.0/2.10.0/loaders/
export GDK_PIXBUF_MODULE_FILE=$WD/etc/gtk-3.0/gdk-pixbuf.loaders
export XDG_DATA_DIRS=$WD/share
export GST_PLUGIN_PATH=$WD/lib/gstreamer-1.0
export GIO_EXTRA_MODULES=$WD/lib/gio/modules
export LANG=da_DK.UTF-8
export DICPATH=$WD/share/myspell

export MONO_PATH=$WD:$WD/lib:/usr/lib
export MONO_CONFIG=$WD/etc/mono/config
export MONO_GAC_PREFIX=$WD 

