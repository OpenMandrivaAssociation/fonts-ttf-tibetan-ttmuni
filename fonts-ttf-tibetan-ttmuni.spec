Summary:	Tibetan Machine Unicode font
Name:		fonts-ttf-tibetan-ttmuni
Version:	1.1.1.1
Release:	%mkrel 0.alpha.1
License:	GPL
URL: 		http://www.thdl.org/xml/show.php?xml=/tools/tibfonts.xml&l=uva10928423419921
Group:		System/Fonts/True type
Source0:	%{name}.tar.bz2
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	freetype-tools
Requires(post):	chkfontpath fontconfig

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
(cd ${RPM_BUILD_ROOT}/%{_datadir}/fonts/ttf/ttmuni
 fc-cache . || touch fonts.cache-1
)

%post
%{_sbindir}/chkfontpath -q -a %{_datadir}/fonts/ttf/ttmuni
%{_bindir}/fc-cache %{_datadir}/fonts/ 

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
 %{_sbindir}/chkfontpath -q -r %{_datadir}/fonts/ttf/ttmuni
   %{_bindir}/fc-cache %{_datadir}/fonts/ 
fi

%clean
rm -fr ${RPM_BUILD_ROOT}

%files
%defattr(0644,root,root,0755)
%doc gpl.txt
%{_datadir}/fonts/ttf/ttmuni/
