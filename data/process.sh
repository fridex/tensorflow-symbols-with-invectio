find -iname '*.json' -exec sed -i 's|.tmp.tmp[a-z0-9_]*.||' {} \;
