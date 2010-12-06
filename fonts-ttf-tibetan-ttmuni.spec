Summary:	Tibetan Machine Unicode font
Name:		fonts-ttf-tibetan-ttmuni
Version:	1.901b
Release:	%mkrel 4
License:	GPLv2+
URL: 		http://www.thdl.org/tools/fonts/tibfonts.php
Group:		System/Fonts/True type
Source0:	TibetanMachineUnicodeFont.zip
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	mkfontdir

%description
This package provides an OpenType Unicode Tibetan font,
for writing in Tibetan, Dzongkha and Ladakhi with almost 4000 glyphs.

%prep
%setup -q -c %{name}

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/%{_datadir}/fonts/ttf/ttmuni/
install -m 644 *.ttf ${RPM_BUILD_ROOT}%{_datadir}/fonts/ttf/ttmuni/
cd ${RPM_BUILD_ROOT}/%{_datadir}/fonts/ttf/ttmuni/
mkfontdir
cp fonts.dir fonts.scale

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
