Summary:	Tibetan Machine Unicode font
Name:		fonts-ttf-tibetan-ttmuni
Version:	1.901b
Release:	%mkrel 3
License:	GPLv2+
URL: 		http://www.thdl.org/tools/fonts/tibfonts.php
Group:		System/Fonts/True type
Source0:	TibetanMachineUnicodeFont.zip
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	freetype-tools

%description
This package provides an OpenType Unicode Tibetan font,
for writing in Tibetan, Dzongkha and Ladakhi with almost 4000 glyphs.

%prep
%setup -q -c %{name}
%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/%{_datadir}/fonts/ttf/ttmuni/
install -m 644 *.ttf ${RPM_BUILD_ROOT}%{_datadir}/fonts/ttf/ttmuni/
cd ${RPM_BUILD_ROOT}/%{_datadir}/fonts/ttf/ttmuni/
/usr/sbin/ttmkfdir > fonts.scale
cp fonts.scale fonts.dir

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/ttf/ttmuni \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-tibetan-ttmuni:pri=50


%clean
rm -fr ${RPM_BUILD_ROOT}

%files
%defattr(0644,root,root,0755)
%doc *.txt
%{_datadir}/fonts/ttf/ttmuni/
%{_sysconfdir}/X11/fontpath.d/ttf-tibetan-ttmuni:pri=50
