%define tarballver %(echo %version|sed -e 's/\\./_/g')
%define tarballname xVST

Summary:	Downloading your favourite video clips
Name:		xvideoservicethief
Version: 	2.4.1
Release: 	2
Source0: 	%{tarballname}_%{tarballver}_src.zip
License: 	GPLv2+
Group: 		Networking/WWW
Url: 		https://xviservicethief.sourceforge.net
BuildRequires: 	qt4-devel
Provides:	xvst = %version
Provides:	xviservicethief = %version
Patch0:         xvideoservicethief-2.4.1-gcc47.patch

%description 
xVideoServiceThief (a.k.a xVST) is a tool for downloading your favourite
video clips from a lot of video websites.

xVideoServiceThief also provide you the ability to convert each video in
most popular formats: AVI, MPEG1, MPEG2, WMV, MP4, 3GP, MP3 file formats.

%files
%defattr(-,root,root)
%_bindir/*
%_datadir/applications/*.desktop

#--------------------------------------------------------------------
%prep
%setup -q -c -n %name-%version
%patch0 -p1

%build
%qmake_qt4
%make

%install
rm -rf %{buildroot}
install -D -m0755 bin/xvst %{buildroot}%_bindir/xvst

mkdir -p %{buildroot}/%_datadir/applications
cat > %{buildroot}/%_datadir/applications/mandriva-%name.desktop <<EOF
[Desktop Entry]
Name=xVideoServiceThief
Comment=Downloading video clips
Exec=%{_bindir}/xvst
Terminal=false
Type=Application
StartupNotify=true
Categories=Qt;Network;
EOF

%clean
rm -rf %{buildroot}



%changelog
* Mon Sep 21 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.8.2-2mdv2010.0
+ Revision: 446274
- rebuild

* Sun Oct 26 2008 Funda Wang <fundawang@mandriva.org> 1.8.2-1mdv2009.1
+ Revision: 297460
- adding virtual provides
- import xvideoservicethief


