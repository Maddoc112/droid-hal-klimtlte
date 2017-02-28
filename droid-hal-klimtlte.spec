%define device klimtlte
%define vendor samsung
%define vendor_pretty SAMSUNG
%define device_pretty KLIMTLTE
%define instalable_zip 1
%define straggler_files\
/selinux_version\
/service_contexts\
%{nil}
%include rpm/dhd/droid-hal-device.inc
