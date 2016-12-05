%define device klimtlte
%define vendor samsung
%define vendor_pretty SAMSUNG
%define device_pretty KLIMTLTE
%define instalable_zip 1
%define have_droid_bin 1
%defne straggler_files\
/selinux_version\
/service_contexts\
%{nil}
%include rpm/dhd/droid-hal-device.inc
