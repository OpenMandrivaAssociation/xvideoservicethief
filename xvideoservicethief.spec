%define tarballver %(echo %version|sed -e 's/\\./_/g')

Summary:	Downloading your favourite video clips
Name:		xvideoservicethief
Version: 	1.8.2
Release: 	%mkrel 2
Source0: 	http://downloads.sourceforge.net/xviservicethief/xVideoServiceThief_%{tarballver}_alpha_src.zip
Patch0:		xvideoservicethief-1.8.2-gcc43.patch
License: 	GPLv2+
Group: 		Networking/WWW
Url: 		http://xviservicethief.sourceforge.net
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	qt4-devel
Provides:	xvst = %version
Provides:	xviservicethief = %version

%description 
xVideoServiceThief (a.k.a xVST) is a tool for downloading your favourite
video clips from a lot of video websites.

xVideoServiceThief also provide you the ability to convert each video in
most popular formats: AVI, MPEG1, MPEG2, WMV, MP4, 3GP, MP3 file formats.

%if %mdkversion < 200900
%post
%update_menus

%postun
%update_menus
%endif

%files
%defattr(-,root,root)
%_bindir/*
%_datadir/applications/*.desktop

#--------------------------------------------------------------------
%prep
%setup -q -c -n %name-%version
%patch0 -p0

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

